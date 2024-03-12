from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.core.exceptions import ValidationError

INCOME_BALANCE = [('Income Statement','Income Statement' ),('Balance sheet', 'Balance Sheet')]
ACCOUNT_TYPE= [
	('Posting', 'Posting'),
	('Heading','Heading'),
	('Total','Total'),
	('Begin-Total','Begin-Total'),
	('End-Total','End-Total'),
]

ACCOUNT_CATEGORY=[
	('Assest', 'Assest'),
	('Liability', 'Liability'),
	('Equity', 'Equity'),
	('Income', 'Income'),
	('Expense', 'Expense')

]
DEBIT_CREDIT=[
	('Both','Both'),
	('Debit', 'Debit'),
	('Credit', 'Credit')

]
	
class Account(MPTTModel):
	code = models.CharField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,related_name='children', blank=True)
	income_balance = models.CharField(verbose_name="Income/Balance",max_length=255,choices=INCOME_BALANCE, blank=True, null=True)
	accountcategory =models.CharField(verbose_name="Account Category",max_length=255, choices=ACCOUNT_CATEGORY, null=True, blank=True)
	debit_credit = models.CharField(verbose_name="Debit/Credit", max_length=10, choices=DEBIT_CREDIT)
	accounttype = models.CharField(verbose_name='Account Type', max_length=255, choices=ACCOUNT_TYPE)
	balance = models.FloatField(verbose_name='Balance', default=0.00)

	def clean(self):
		if self.income_balance != self.parent.income_balance:
			raise ValidationError("Both parent and current account have to be the same")
		super().clean()

	def save(self, *args, **kwargs):
		self.full_clean()  # Perform full validation before saving
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.name
	# class MPTTMeta:
	# 	order_insertion_by = ['name']


class GLAccountCategories(models.Model):
	description = models.CharField(max_length=255)
	account_category = models.CharField(max_length=255,choices=ACCOUNT_CATEGORY)
	balance = models.IntegerField()

	class Meta:
		verbose_name = 'G/L Account Category'
		verbose_name_plural = 'G/L Account Categories'


	