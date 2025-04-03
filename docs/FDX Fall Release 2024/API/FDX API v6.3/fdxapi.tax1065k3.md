openapi: 3.1.0
info:
  version: '6.3.0'
  title: FDX V6.3.0 US Tax API
  description: Financial Data Exchange V6.3.0 US Tax API
  contact:
    name: Financial Data Exchange
    url: 'https://financialdataexchange.org/'
    email: fdxsupport@financialdataexchange.org
  license:
    name: FDX API License Agreement (11-13-2019)
    url: 'https://financialdataexchange.org/common/Uploaded%20files/Policies/FDX%20API%20License%20Agreement-(11-13-2019).pdf'
servers:
  - url: 'https://api.fi.com/fdx/v6'
    description: Financial Data Exchange V6 US Tax API

# paths:

components:

  schemas:
    ############################################################
    #
    # US Tax Form 1065 Schedule K-3 entities
    #
    # Unlike other FDX API files, this contains a single primary
    # entity Tax1065ScheduleK3, and all its contained entities.
    # Therefore these entity definitions are not in alphabetical
    # order, they are listed in the order in which they are first
    # referenced in a property definition.
    #
    ############################################################

    Tax1065ScheduleK3:
      title: Form 1065 Schedule K 3
      description: Partner's Share of Income, Deductions, Credits, etc. - International,
        from Partnership (boxes A, B as issuer) to Partner (boxes C, D as recipient)
      type: object
      properties:
        finalK3:
          type: boolean
          description: Final K-3 indicator
        amendedK3:
          type: boolean
          description: Amended K-3 indicator
        fiscalYearBegin:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Fiscal year begin date
        fiscalYearEnd:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Fiscal year end date
        missingSsnEinReasonCode:
          type: string
          description: Schedule K-1 Part II Line E, Missing SSN/EIN Reason
        part1Attached:
          type: boolean
          description: E1, Does Part I apply?
        part2Attached:
          type: boolean
          description: E2, Does Part II apply?
        part3Attached:
          type: boolean
          description: E3, Does Part III apply?
        part4Attached:
          type: boolean
          description: E4, Does Part IV apply?
        part5Attached:
          type: boolean
          description: E5, Does Part V apply?
        part6Attached:
          type: boolean
          description: E6, Does Part VI apply?
        part7Attached:
          type: boolean
          description: E7, Does Part VII apply?
        part8Attached:
          type: boolean
          description: E8, Does Part VIII apply?
        part9Attached:
          type: boolean
          description: E9, Does Part IX apply?
        part10Attached:
          type: boolean
          description: E10, Does Part X apply?
        part11Attached:
          type: boolean
          description: E11, Does Part XI apply?
        part13Attached:
          type: boolean
          description: E13, Does Part XIII apply?
        part1Attachments:
          $ref: '#/components/schemas/Part1Attachments'
          description: Part I, Partner's Share of Partnership's Other Current Year
            International Information
        part2ForeignTaxCreditLimitation:
          $ref: '#/components/schemas/Part2ForeignTaxCreditLimitation'
          description: Part II, Foreign Tax Credit Limitation
        part3PrepareForms1116Or1118:
          $ref: '#/components/schemas/Part3PrepareForms1116Or1118'
          description: Part III, Other Information for Preparation of Form 1116 Or 1118
        part4Section250DeductionFdii:
          $ref: '#/components/schemas/Part4Section250DeductionFdii'
          description: Part IV, Information on Partner's Section 250 Deduction
            with Respect to Foreign-Derived Intangible Income (FDII)
        part5ForeignCorpDistributionPartnership:
          description: Part V, Lines A-O, Distributions from Foreign Corporations to Partnership
          type: array
          items:
            $ref: '#/components/schemas/Part5ForeignCorpDistributionPartnership'
        part6PartnerSection951a1Inclusion:
          type: array
          description: Part VI, Lines a-b, A-K, 1, Information on Partners' Section 951(a)(1) and Section 951A Inclusions
          items:
            $ref: '#/components/schemas/Part6PartnerSection951a1Inclusion'
        part7InfoToComplete8621:
          type: array
          description: Part VII, Information Regarding Passive Foreign Investment Companies (PFICs),
            to complete Form 8621
          items:
            $ref: '#/components/schemas/Part7InfoToComplete8621'
        part8PartnershipForeignCorpIncome:
          type: array
          description: Part VIII, Partnership's Interest in Foreign Corporation Income (Section 960)
          items:
            $ref: '#/components/schemas/Part8PartnershipForeignCorpIncome'
        part9PartnerInfoBeat:
          $ref: '#/components/schemas/Part9PartnerInfoBeat'
          description: Part IX, Partner's Information for Base Erosion and Anti-Abuse Tax (BEAT), Section 59A
        part10ForeignPartnerSourceIncomeDeduction:
          $ref: '#/components/schemas/Part10ForeignPartnerSourceIncomeDeduction'
          description: Part X, Foreign Partner's Character and Source of Income and Deductions
        part11CoveredPartnerships:
          $ref: '#/components/schemas/Part11CoveredPartnerships'
          description: Part XI, Section 871(m) Covered Partnerships
        part13SharePartnershipInterestTransfer:
          type: array
          description: Part XIII, Foreign Partner's Distributive Share of Deemed Sale Items on
            Transfer of Partnership Interest
          items:
            $ref: '#/components/schemas/Part13SharePartnershipInterestTransfer'

    Part1Attachments:
      title: Part 1 Attachments
      description: Part I, Partner's Share of Partnership's Other Current Year
        International Information
      type: object
      properties:
        gainOnPersonalPropertySale:
          type: boolean
          description: Part I, Line 1, Gain on personal property sale indicator
        foreignOilAndGasTaxes:
          type: boolean
          description: Part I, Line 2, Foreign oil and gas taxes indicator
        splitterArrangements:
          type: boolean
          description: Part I, Line 3, Splitter arrangements indicator
        foreignTaxTranslation:
          type: boolean
          description: Part I, Line 4, Foreign tax translation indicator
        highTaxedIncome:
          type: boolean
          description: Part I, Line 5, High-taxed income indicator
        section267aDisallowedDeduction:
          type: boolean
          description: Part I, Line 6, Section 267A disallowed deduction indicator
        form5471Attachment:
          type: boolean
          description: Part I, Line 8, Form 5471 information indicator
        otherFormsAttachment:
          type: boolean
          description: Part I, Line 9, Other forms indicator
        partnerLoanTransactions:
          type: boolean
          description: Part I, Line 10, Partner loan transactions indicator
        dualConsolidatedLoss:
          type: boolean
          description: Part I, Line 11, Dual consolidated loss indicator
        form8865Attachment:
          type: boolean
          description: Part I, Line 12, Form 8865 information indicator
        otherInternationalItems:
          type: boolean
          description: Part I, Line 13, Other international items indicator

    Part2ForeignTaxCreditLimitation:
      title: Part 2, Foreign Tax Credit Limitation
      description: Part II, Foreign Tax Credit Limitation
      type: object
      properties:
        foreignTaxCreditGrossIncome:
          $ref: '#/components/schemas/ForeignTaxCreditGrossIncome'
          description: Part II, Section 1, Lines 1-24, Foreign Tax Credit Limitation, Gross Income
        foreignTaxCreditDeduction:
          $ref: '#/components/schemas/ForeignTaxCreditDeduction'
          description: Part II, Section 2, Lines 25-55, Foreign Tax Credit Limitation, Deductions

    ForeignTaxCreditGrossIncome:
      title: Foreign Tax Credit Gross Income
      description: Part II, Section 1, Lines 1-24, Foreign Tax Credit Limitation, Gross Income
      type: object
      properties:
        salesGrossIncome:
          type: array
          description: Part II, Section 1, Line 1, Sales
          items:
            $ref: '#/components/schemas/IncomeSourcesDetail'
        grossIncomePerfOfServices:
          type: array
          description: Part II, Section 1, Line 2, Gross income from performance of services
          items:
            $ref: '#/components/schemas/IncomeSourcesDetail'
        grossRentalRealEstateIncome:
          type: array
          description: Part II, Section 1, Line 3, Gross rental real estate income
          items:
            $ref: '#/components/schemas/IncomeSourcesDetail'
        otherGrossRentalIncome:
          type: array
          description: Part II, Section 1, Line 4, Other gross rental income
          items:
            $ref: '#/components/schemas/IncomeSourcesDetail'
        guaranteedPayments:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 1, Line 5, Guaranteed Payments
        interestIncome:
          type: array
          description: Part II, Section 1, Line 6, Interest income
          items:
            $ref: '#/components/schemas/IncomeSourcesDetail'
        ordinaryDividends:
          type: array
          description: Part II, Section 1, Line 7, Ordinary dividends (excluding amount on line 8)
          items:
            $ref: '#/components/schemas/IncomeSourcesDetail'
        qualifiedDividends:
          type: array
          description: Part II, Section 1, Line 8, Qualified dividends
          items:
            $ref: '#/components/schemas/IncomeSourcesDetail'
        royaltiesLicenseFees:
          type: array
          description: Part II, Section 1, Line 10, Royalties and license fees
          items:
            $ref: '#/components/schemas/IncomeSourcesDetail'
        netShortTermCapGain:
          type: array
          description: Part II, Section 1, Line 11, Net short-term capital gain
          items:
            $ref: '#/components/schemas/IncomeSourcesDetail'
        netLongTermCapGain:
          type: array
          description: Part II, Section 1, Line 12, Net long-term capital gain
          items:
            $ref: '#/components/schemas/IncomeSourcesDetail'
        collectiblesGain:
          type: array
          description: Part II, Section 1, Line 13, Collectibles (28%) gain
          items:
            $ref: '#/components/schemas/IncomeSourcesDetail'
        unrecapturedSection1250Gain:
          type: array
          description: Part II, Section 1, Line 14, Unrecaptured section 1250 gain
          items:
            $ref: '#/components/schemas/IncomeSourcesDetail'
        netSection1231Gain:
          type: array
          description: Part II, Section 1, Line 15, Net section 1231 gain
          items:
            $ref: '#/components/schemas/IncomeSourcesDetail'
        section986cGain:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 1, Line 16, Section 986(c) gain
        section987Gain:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 1, Line 17, Section 987 gain
        section988Gain:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 1, Line 18, Section 988 gain
        section951aInclusions:
          type: array
          description: Part II, Section 1, Line 19, Section 951(a) inclusions
          items:
            $ref: '#/components/schemas/IncomeSourcesDetail'
        otherIncome:
          type: array
          description: Part II, Section 1, Line 20, Other income
          items:
            $ref: '#/components/schemas/OtherIncome'
        totalGrossIncome:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 1, Line 24 total, Total gross income
        totalGrossIncomeByCountry:
          type: array
          description: Part II, Section 1, Line 24 detailed table rows, Total gross income by Country
          items:
            $ref: '#/components/schemas/IncomeSourcesDetail'

    IncomeSources:
      title: Income Sources
      description: Part II, Section 1, Lines 1-8, 10-20, 24, Foreign Tax Credit Limitation - Gross Income,
        and Part II, Section 2, Lines 25-31, 33-37, 39-50, 54-55, Foreign Tax Credit Limitation - Deductions,
        and Part III, Section 1, Line 1, Research and Experimental Expenses Apportionment Factors (as GrossReceiptsSicCode),
        and Part III, Section 2, Lines 1-5, 6a-6d, 7-8, Interest Expense Apportionment Factors,
        and Part III, Section 3, Lines 1-4, Foreign-Derived Intangible Income (FDII) Deduction Apportionment Factors,
        and Part III, Section 5, Lines 1-2, Other tax information (as IncomeAdjustments)
      type: object
      properties:
        usSourceIncome:
          type: number
          description: Column (a), U.S. source income,
            for Part II, Section 1, Lines 1-8, 10-20, 24 and Section 2, Lines 25-31, 33-37, 39-50, 54-55,
            and Part III, Section 1, Line 1; Section 2, Lines 1-5, 6a-6d, 7-8; Section 3, Lines 1-4; Section 5, Lines 1-2
        foreignBranchIncome:
          type: number
          description: Column (b), Foreign branch category income,
            for Part II, Section 1, Lines 1-8, 10-20, 24 and Section 2, Lines 25-31, 33-37, 39-50, 54-55,
            and Part III, Section 1, Line 1; Section 2, Lines 1-5, 6a-6d, 7-8; Section 5, Lines 1-2;
            NOT for Part III, Section 3, Lines 1-4
        passiveCategoryIncome:
          type: number
          description: Column (c), Foreign Source - Passive category income,
            for Part II, Section 1, Lines 1-8, 10-20, 24 and Section 2, Lines 25-31, 33-37, 39-50, 54-55,
            and Part III, Section 1, Line 1; Section 2, Lines 1-5, 6a-6d, 7-8; Section 3, Lines 1-4; Section 5, Lines 1-2
        generalCategoryIncome:
          type: number
          description: Column (d), Foreign Source - General category income,
            for Part II, Section 1, Lines 1-8, 10-20, 24 and Section 2, Lines 25-31, 33-37, 39-50, 54-55,
            and Part III, Section 1, Line 1; Section 2, Lines 1-5, 6a-6d, 7-8; Section 3, Lines 1-4; Section 5, Lines 1-2
        separateCategory:
          type: array
          description: Column (e), Foreign Source - Other category codes and incomes,
            for Part II, Section 1, Lines 1-8, 10-20, 24 and Section 2, Lines 25-31, 33-37, 39-50, 54-55,
            and Part III, Section 1, Line 1; Section 2, Lines 1-5, 6a-6d, 7-8; Section 3, Lines 1-4; Section 5, Lines 1-2
          items:
            $ref: '#/components/schemas/SeparateCategory'
        sourcedAtPartnerLevelIncome:
          type: number
          description: Column (f), Sourced by partner,
            for Part II, Section 1, Lines 1-8, 10-20, 24 and Section 2, Lines 25-31, 33-37, 39-50, 54-55,
            and Part III, Section 1, Line 1; Section 2, Lines 1-5, 6a-6d, 7-8; Section 3, Lines 1-4; Section 5, Lines 1-2
        total:
          type: number
          description: Column (g), Total amount,
            for Part II, Section 1, Lines 1-8, 10-20, 24 and Section 2, Lines 25-31, 33-37, 39-50, 54-55,
            and Part III, Section 1, Line 1; Section 2, Lines 1-5, 6a-6d, 7-8; Section 3, Lines 1-4; Section 5, Lines 1-2

    SeparateCategory:
      title: Separate Category
      description: Part II, Section 1, Lines 1-8, 10-20, 24, Foreign Tax Credit Limitation - Gross Income,
        and Part II, Section 2, Lines 25-31, 33-37, 39-50, 54-55, Foreign Tax Credit Limitation - Deductions,
        and Part III, Section 1, Line 1, Research and Experimental Expenses Apportionment Factors,
        and Part III, Section 2, Lines 1-5, 6a-6d, 7-8, Interest Expense Apportionment Factors,
        and Part III, Section 3, Lines 1-4, Foreign-Derived Intangible Income (FDII) Deduction Apportionment Factors,
        and Part III, Section 4, Lines 1-3, A-F, Foreign taxes income sources,
        and Part III, Section 5, Lines 1-2, Other tax information
      type: object
      properties:
        separateCategoryCode:
          type: string
          description: Column (e), Foreign Source - Separate category code
        foreignCountryOrUsPossessionCode:
          $ref: './fdxapi.components.yaml#/components/schemas/Iso3166CountryCode'
          description: Column (e), Foreign Source - Foreign country or US possession code. Not used in Part II,
            for Part III, Section 1, Line 1, Research and Experimental Expenses Apportionment Factors (as GrossReceiptsSicCode),
            and Part III, Section 2, Lines 1-5, 6a-6d, 7-8, Interest Expense Apportionment Factors,
            and Part III, Section 4, Lines 1-3, A-F, column (f) Foreign taxes income sources,
            and Part III, Section 5, Lines 1-2, Other tax information (as IncomeAdjustments).
            Use ISO-defined country codes to deliver to taxpayers and tax preparation software,
            for delivery to IRS they will need to be mapped to IRS country codes
        otherCategoryIncome:
          type: number
          description: Column (e), Foreign Source - Other category amount

    IncomeSourcesDetail:
      title: Income Sources Detail
      description: Part II, Section 1, Lines 1-4, 6-8, 10-15, 19-20, 24(A+) Foreign Tax Credit Limitation - Gross Income,
      type: object
      allOf:
        - $ref: '#/components/schemas/IncomeSources'
        - type: object
          properties:
            alphaRowId:
              type: string
              description: Part II, Section 1, Lines 1-4, 6-8, 10-15, 19-20, 24(A+) table row, Alpha identifier
            foreignUsCountryCode:
              $ref: './fdxapi.components.yaml#/components/schemas/Iso3166CountryCode'
              description: Part II, Section 1, Lines 1-4, 6-8, 10-15, 19-20, 24(A+) table row, Country code.
                Use ISO-defined country codes to deliver to taxpayers and tax preparation software,
                for delivery to IRS they will need to be mapped to IRS country codes
            otherCategoryDescriptionCode:
              type: string
              description: Part II, Section 1, Lines 1-4, 6-8, 10-15, 19-20, 24(A+) Other category description code

    OtherIncome:
      title: Other Income
      description: Part II, Section 1, Line 20, Other income
      type: object
      allOf:
        - $ref: '#/components/schemas/IncomeSourcesDetail'
        - type: object
          properties:
            otherIncomeDesc:
              type: string
              description: Part II, Section 1, Line 20, table row Other income description

    ForeignTaxCreditDeduction:
      title: Foreign Tax Credit Deduction
      description: Part II, Section 2, Lines 25-55, Foreign Tax Credit Limitation, Deductions
      type: object
      properties:
        expenseAllocableToSalesIncome:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 25, Expenses allocable to sales income
        expensesAllocableGrossIncomePerfServices:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 26, Expenses allocable to gross income from performance of services
        netShortTermCapLoss:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 27, Net short-term capital loss
        netLongTermCapLoss:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 28, Net long-term capital loss
        collectablesLoss:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 29, Collectibles loss
        netSection1231Loss:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 30, Net section 1231 loss
        otherLosses:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 31, Other losses
        researchExperimentalExpenses:
          type: array
          description: Part II, Section 2, Line 32, Research and experimental (R and E) expenses
          items:
            $ref: '#/components/schemas/ResearchExperimentalExpenses'
        allocableRentalExpenses:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 33, Allocable rental expenses -
            Depreciation, depletion, and amortization
        otherAllocableRentalExpenses:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 34, Allocable rental expenses -
            Other than depreciation, depletion, and amortization
        allocableRoyaltyLicensingExpense:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 35, Allocable royalty and licensing expenses -
            Depreciation, depletion, and amortization
        otherAllocableRoyaltyLicensingExpense:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 36, Allocable royalty and licensing expenses -
            Other than depreciation, depletion, and amortization
        otherAllocableDepreciation:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 37, Depreciation not included on lines 33 or 35
        charitableContribution:
          $ref: '#/components/schemas/CharitableContribution'
          description: Part II, Section 2, Line 38, Charitable contributions
        interestExpenseUnderSection186110e:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 39, Interest expense specifically
            allocable under Regulations section 1.861-10(e)
        otherInterestExpenseUnderSection186110t:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 40, Other interest expense specifically
            allocable under Regulations section 1.861-10T
        businessOtherInterestExpense:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 41, Other interest expense - Business
        investmentOtherInterestExpense:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 42, Other interest expense - Investment
        passiveActivityOtherInterestExpense:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 43, Other interest expense - Passive activity
        section59e2ExpendNoResearchExperimentalExpense:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 44, Section 59(e)(2) expenditures,
            excluding Research and Experimental expenses on line 32
        foreignTaxesNotCreditableDeduction:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 45, Foreign taxes not creditable but deductible
        section986cLoss:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 46, Section 986(c) loss
        section987Loss:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 47, Section 987 loss
        section988Loss:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 48, Section 988 loss
        otherAllocableDeductions:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 49, Other allocable deductions
        otherApportionedShareDeduction:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 50, Other apportioned share of deductions
        totalDeductions:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 54, Total deductions
            (combine lines 25 through 53)
        netIncomeLoss:
          $ref: '#/components/schemas/IncomeSources'
          description: Part II, Section 2, Line 55, Net income (loss)
            (subtract line 54 from line 24)

    ResearchExperimentalExpenses:
      title: Research Experimental Expenses
      description: Part II, Section 2, Line 32, Research and experimental (R and E) expenses
      type: object
      properties:
        sicCode:
          type: string
          description: Part II, Section 2, Line 32, table row SIC code
        sourcedAtPartnerLevelIncome:
          type: number
          description: Part II, Section 2, Line 32, (f), Sourced by partner
        total:
          type: number
          description: Part II, Section 2, Line 32, (g), Total amount

    CharitableContribution:
      title: Charitable Contribution
      description: Part II, Section 2, Line 38, Charitable contributions
      type: object
      properties:
        usSourceIncome:
          type: number
          description: Part II, Section 2, Line 38, (a), U.S. source income
        total:
          type: number
          description: Part II, Section 2, Line 38, (g), Total amount

    Part3PrepareForms1116Or1118:
      title: Part 3, Prepare Forms 1116 Or 1118
      description: Part III, Other Information for Preparation of Form 1116 Or 1118
      type: object
      properties:
        reExpensesApportionmentFactor:
          $ref: '#/components/schemas/ReExpensesApportionmentFactor'
          description: Part III, Section 1, Lines 1-2, Research and Experimental Expenses Apportionment Factors
        interestExpenseApportionmentFactors:
          type: array
          description: Part III, Section 2, Lines 1-5, 6a-6d, 7-8, Interest Expense Apportionment Factors
          items:
            $ref: '#/components/schemas/InterestExpenseApportionmentFactors'
        fdiiDeductionApportionmentFactors:
          $ref: '#/components/schemas/FdiiDeductionApportionmentFactors'
          description: Part III, Section 3, Lines 1-4, Foreign-Derived Intangible Income (FDII)
            Deduction Apportionment Factors
        foreignTaxes:
          $ref: '#/components/schemas/ForeignTaxes'
          description: Part III, Section 4, Lines 1-3, Foreign Taxes
        otherTaxInformation:
          $ref: '#/components/schemas/OtherTaxInformation'
          description: Part III, Section 5, Lines 1-2, Other Tax Information

    ReExpensesApportionmentFactor:
      title: Research Experimental Expenses Apportioned Factor
      description: Part III, Section 1, Research and Experimental Expenses Apportionment Factors
      type: object
      properties:
        grossReceiptsSicCode:
          type: array
          description: Part III, Section 1, Line 1, Gross receipts by SIC code
          items:
            $ref: '#/components/schemas/GrossReceiptsSicCode'
        grossReceiptsSicCodeOther:
          type: array
          description: Part III, Section 1, Line 1, Gross receipts by SIC code, Other
          items:
            $ref: '#/components/schemas/GrossReceiptsSicCodeOther'
        reExpenseActivityInsideUs:
          type: array
          description: Part III, Section 1, Line 2 A, Research and Experimental expenses
            with respect to activity performed in the U.S.
          items:
            $ref: '#/components/schemas/ResearchExperimentalExpensesBySicCode'
        reExpenseActivityOutsideUs:
          type: array
          description: Part III, Section 1, Line 2 B, Research and Experimental expenses
            with respect to activity performed outside the U.S.
          items:
            $ref: '#/components/schemas/ResearchExperimentalExpensesBySicCode'

    GrossReceiptsSicCode:
      title: Gross Receipts SIC Code
      description: Part III, Section 1, Line 1, Gross receipts by SIC code
      type: object
      allOf:
        - $ref: '#/components/schemas/IncomeSources'
        - type: object
          properties:
            sicCode:
              type: string
              description: Part III, Section 1, Line 1, table row SIC code

    GrossReceiptsSicCodeOther:
      title: Gross Receipts SIC Code Other
      description: Part III, Section 1, Line 1, Gross receipts by SIC code, Other
      type: object
      allOf:
        - $ref: '#/components/schemas/SeparateCategory'
        - type: object
          properties:
            sicCode:
              type: string
              description: Part III, Section 1, Line 1, table row SIC code

    ResearchExperimentalExpensesBySicCode:
      title: Research Experimental Expenses Activity
      description: Part III, Section 1, Line 2 B, Exclusive apportionment with respect to
        total Research and Experimental expenses entered on Part II, line 32;
        and Part IV, Section 3, Line 16 A-C, Research and Experimental Expenses By SIC Code
      type: object
      properties:
        sicCode:
          type: string
          description: Table row SIC code, Part III, Section 1, Lines 2 A and 2 B, (i)-(iii);
            and Part IV, Section 3, Line 16 A-C
        total:
          type: number
          description: Total amount, Part III, Section 1, Lines 2 A and 2 B, column (g);
            and Part IV, Section 3, Line 16 A-C, column (c), Total amount

    InterestExpenseApportionmentFactors:
      title: Interest Expense Apportionment Factors
      description: Part III, Section 2, Lines 1-5, 6a-6d, 7-8, Interest Expense Apportionment Factors
      type: object
      properties:
        totalAvgValueAssets:
          $ref: '#/components/schemas/IncomeSources'
          description: Part III, Section 2, Line 1, Total average value of assets
        section734b743bAdjustmentToAssets:
          $ref: '#/components/schemas/IncomeSources'
          description: Part III, Section 2, Line 2, Sections 734(b) and 743(b) adjustment
            to assets - average value
        assetAttractingInterestExpenseSection186110e:
          $ref: '#/components/schemas/IncomeSources'
          description: Part III, Section 2, Line 3, Assets attracting directly allocable
            interest expense under Regulations section 1.861-10T
        otherAssetAttractingInterestExpense186110t:
          $ref: '#/components/schemas/IncomeSources'
          description: Part III, Section 2, Line 4, Other assets attracting directly allocable
            interest expense under Regulations section 1.861-10T
        assetsExcludedApportioned:
          $ref: '#/components/schemas/IncomeSources'
          description: Part III, Section 2, Line 5, Assets excluded from apportionment formula
        totalAssetsUsedApportioned:
          $ref: '#/components/schemas/IncomeSources'
          description: Part III, Section 2, Line 6a, Total assets used for apportionment
            (subtract the sum of lines 3, 4, and 5 from the sum of lines 1 and 2)
        assetsAttractingBusinessInterestExpense:
          $ref: '#/components/schemas/IncomeSources'
          description: Part III, Section 2, Line 6b, Assets attracting business interest expense
        assetsAttractingInvestmentInterestExpense:
          $ref: '#/components/schemas/IncomeSources'
          description: Part III, Section 2, Line 6c, Assets attracting investment interest expense
        assetAttractingPassiveActivityInterestExpense:
          $ref: '#/components/schemas/IncomeSources'
          description: Part III, Section 2, Line 6d, Assets attracting passive activity interest expense
        basisInStockOf10PercentOwnNonCfc:
          $ref: '#/components/schemas/IncomeSources'
          description: Part III, Section 2, Line 7, Basis in stock of 10%-owned noncontrolled foreign corporations
        basisInStockOfCfc:
          $ref: '#/components/schemas/IncomeSources'
          description: Part III, Section 2, Line 8, Basis in stock of CFCs

    FdiiDeductionApportionmentFactors:
      title: Fdii Deduction Apportionment Factors
      description: Part III, Section 3, Lines 1-4, Foreign-Derived Intangible Income (FDII)
        Deduction Apportionment Factors
      type: object
      properties:
        foreignDerivedGrossReceipts:
          $ref: '#/components/schemas/IncomeSources'
          description: Part III, Section 3, Line 1, Foreign-derived gross receipts
        costOfGoodsSold:
          $ref: '#/components/schemas/IncomeSources'
          description: Part III, Section 3, Line 2, Cost of goods sold (COGS)
        partnershipDeductionAllocableForeignGrossReceipts:
          $ref: '#/components/schemas/IncomeSources'
          description: Part III, Section 3, Line 3, Partnership deductions allocable
            to foreign-derived gross receipts
        partnershipDeductionApportionedForeignGrossReceipts:
          $ref: '#/components/schemas/IncomeSources'
          description: Part III, Section 3, Line 4, Other partnership deductions
            apportioned to foreign-derived gross receipts

    ForeignTaxes:
      title: Foreign Taxes
      description: Part III, Section 4, Lines 1-3, Foreign Taxes
      type: object
      properties:
        foreignTaxesPaid:
          type: boolean
          description: Part III, Section 4, Line 1, Direct (section 901 or 903) foreign taxes paid
        foreignTaxesAccrued:
          type: boolean
          description: Part III, Section 4, Line 1, Direct (section 901 or 903) foreign taxes accrued
        directSection901Or903ForeignTaxes:
          type: array
          description: Part III, Section 4, Line 1 A-F, Direct (section 901 or 903) foreign taxes
          items:
            $ref: '#/components/schemas/ForeignTaxIncomeSources'
        directSection901Or903ForeignTaxesOther:
          type: array
          description: Part III, Section 4, Line 1 A-F, Direct (section 901 or 903) Other foreign taxes
          items:
            $ref: '#/components/schemas/DirectSection901Or903ForeignTaxesOther'
        foreignTaxReductions:
          $ref: '#/components/schemas/ForeignTaxReductions'
          description: Part III, Section 4, Line 2 A-G, Reduction of foreign taxes
        totalForeignTaxReductions:
          $ref: '#/components/schemas/ForeignTaxIncomeSources'
          description: Part III, Section 4, Line 2, Total reduction of foreign taxes
        foreignTaxRedeterminations:
          type: array
          description: Part III, Section 4, Line 3, A-C, Foreign tax redeterminations
          items:
            $ref: '#/components/schemas/ForeignTaxRedeterminations'

    CategoryIncome:
      title: Category Income
      description: Part III, Section 4, Lines 1-3, Foreign Taxes
      type: object
      properties:
        usIncome:
          type: number
          description: Columns (b)-(e), U.S. category income
        foreignIncome:
          type: number
          description: Columns (b)-(e), Foreign category income
        partnerIncome:
          type: number
          description: Columns (c)-(e), Partner category income

    ForeignTaxIncomeSources:
      title: Foreign Tax Income Sources
      description: Part III, Section 4, Lines 1-3, A-F, Foreign taxes income sources table
      type: object
      properties:
        alphaRowId:
          type: string
          description: Lines 1-3, A-F, table row Alpha identifier
        foreignCountryOrUsPossessionCode:
          $ref: './fdxapi.components.yaml#/components/schemas/Iso3166CountryCode'
          description: Lines 1-3, A-F, table row Country code.
            Use ISO-defined country codes to deliver to taxpayers and tax preparation software,
            for delivery to IRS they will need to be mapped to IRS country codes
        otherCategoryDescriptionCode:
          type: string
          description: Lines 1-3, A-F, table row Other category description code
        taxTypeCode:
          type: string
          description: Lines 1-3, A-F, column (a), Type of tax
        section951aCategory:
          $ref: '#/components/schemas/CategoryIncome'
          description: Lines 1-3, A-F, column (b), Section 951A category income
        foreignBranchCategory:
          $ref: '#/components/schemas/CategoryIncome'
          description: Lines 1-3, A-F, column (c), Foreign branch category income
        passiveCategory:
          $ref: '#/components/schemas/CategoryIncome'
          description: Lines 1-3, A-F, column (d), Passive category income
        generalCategory:
          $ref: '#/components/schemas/CategoryIncome'
          description: Lines 1-3, A-F, column (e), General category income
        separateCategory:
          type: array
          description: Lines 1-3, A-F, column (f), Other category code
          items:
            $ref: '#/components/schemas/SeparateCategory'
        total:
          type: number
          description: Lines 1-3, A-F, column (g), Total amount"

    DirectSection901Or903ForeignTaxesOther:
      title: Direct Section 901 Or 903 Foreign Taxes Other
      description: Part III, Section 4, Line 1, A-F, Direct Section 901 Or 903 Foreign Taxes Other
      type: object
      allOf:
        - $ref: '#/components/schemas/SeparateCategory'
        - type: object
          properties:
            alphaRowId:
              type: string
              description: Line 1, A-F, table row Alpha identifier
            otherCategoryDescriptionCode:
              type: string
              description: Line 1, A-F, table row Other category description code

    ForeignTaxReductions:
      title: Foreign Tax Reductions
      description: Part III, Section 4, Line 2 A-G, Reduction of foreign taxes
      type: object
      properties:
        taxesOnForeignMineralIncome:
          $ref: '#/components/schemas/ForeignTaxIncomeSources'
          description: Line 2A, columns (a)-(g), Taxes on foreign mineral income
        internationalBoycottProvisions:
          $ref: '#/components/schemas/ForeignTaxIncomeSources'
          description: Line 2C, columns (a)-(g), International boycott provisions
        failureToFilePenalty:
          $ref: '#/components/schemas/ForeignTaxIncomeSources'
          description: Line 2D, columns (a)-(g), Failure-to-file penalties
        splitterArrangementTax:
          $ref: '#/components/schemas/ForeignTaxIncomeSources'
          description: Line 2E, columns (a)-(g), Taxes with respect to splitter arrangements
        taxesOnForeignCorpDistributions:
          $ref: '#/components/schemas/ForeignTaxIncomeSources'
          description: Line 2F, columns (a)-(g), Taxes on foreign corporate distributions
        otherTaxReductions:
          $ref: '#/components/schemas/ForeignTaxIncomeSources'
          description: Line 2G, columns (a)-(g), Other reductions of taxes

    ForeignTaxRedeterminations:
      title: Foreign Tax Redeterminations
      description: Part III, Section 4, Line 3, A-C, Foreign tax redeterminations
      type: object
      allOf:
        - $ref: '#/components/schemas/ForeignTaxIncomeSources'
        - type: object
          properties:
            relatedTaxYear:
              type: string
              description: Line 3, A-C, Related Tax Year
            taxPaidDate:
              type: array
              description: Line 3, A-C, Date Tax Paid
              items:
                $ref: './fdxapi.components.yaml#/components/schemas/DateString'
            contestedTax:
              type: boolean
              description: Line 3, A-C, Contested Tax

    OtherTaxInformation:
      title: Other Tax Information
      description: Part III, Section 5, Lines 1-2, Other Tax Information
      type: object
      properties:
        section743bPositiveIncomeAdjustment:
          $ref: '#/components/schemas/IncomeAdjustments'
          description: Part III, Section 5, Line 1, Section 743(b) positive income adjustment
        section743bNegativeIncomeAdjustment:
          $ref: '#/components/schemas/IncomeAdjustments'
          description: Part III, Section 5, Line 2, Section 743(b) negative income adjustment

    IncomeAdjustments:
      title: Income Adjustments
      description: Part III, Section 5, Lines 1-2, Other Tax Information
      type: object
      allOf:
        - $ref: '#/components/schemas/IncomeSources'
        - type: object
          properties:
            section951aCategoryIncome:
              type: number
              description: Column (b), Section 951A category income

    Part4Section250DeductionFdii:
      title: Part 4, Partner Section 250 Deduction FDII
      description: Part IV, Information on Partner's Section 250 Deduction
        with Respect to Foreign-Derived Intangible Income (FDII),
        Section 1, Information to determine Deduction Eligible Income (DEI) and
        Qualified Business Asset Investment (QBAI) on Form 8993,
        Section 2, Information to determine Foreign Derived Deduction Eligible Income (FDDEI) on Form 8993,
        Section 3, Other information for preparation of Form 8993
      type: object
      properties:
        netIncomeLoss:
          type: number
          description: Section 1, Line 1, Net income (loss)
        grossDei:
          type: number
          description: Section 1, Line 2a, Deduction Eligible Income (DEI) gross receipts
        costOfGoodsSold:
          type: number
          description: Section 1, Line 2b, Deduction Eligible Income (DEI) cost of goods sold (COGS)
        properlyAllocatedDeduction:
          type: number
          description: Section 1, Line 2c, DEI properly allocated and apportioned deductions
        section951a1Income:
          type: number
          description: Section 1, Line 3, Section 951(a) inclusions
        cfcDividendsReceived:
          type: number
          description: Section 1, Line 4, Controlled Foreign Corporation (CFC) dividends
        financialServicesIncome:
          type: number
          description: Section 1, Line 5, Financial services income
        domesticOilGasExtractionIncome:
          type: number
          description: Section 1, Line 6, Domestic oil and gas extraction income
        foreignBranchIncome:
          type: number
          description: Section 1, Line 7, Foreign branch income
        partnershipQbai:
          type: number
          description: Section 1, Line 8, Partnership Qualified Business Asset Investment (QBAI)
        grossReceiptsForFddei:
          $ref: '#/components/schemas/ForeignDerivedDeductionEligibleIncome'
          description: Section 2, Line 9, Gross receipts for Foreign Derived Deduction Eligible Income (FDDEI)
        costOfGoodsSoldForFddei:
          $ref: '#/components/schemas/ForeignDerivedDeductionEligibleIncome'
          description: Section 2, Line 10, Cost of goods sold (COGS) for FDDEI
        allocableDeductionForFddei:
          $ref: '#/components/schemas/ForeignDerivedDeductionEligibleIncome'
          description: Section 2, Line 11, Allocable deductions for FDDEI
        otherApportionedDeductionForFddei:
          type: number
          description: Section 2, Line 12, Other apportioned deductions for FDDEI
        interestExpenseSection186110e:
          $ref: '#/components/schemas/InterestDeductionAndExpenseInfo'
          description: Section 3, Line 13A, Interest expense specifically allocable
            under Regulations section 1.861-10(e)
        otherInterestExpense186110t:
          $ref: '#/components/schemas/InterestDeductionAndExpenseInfo'
          description: Section 3, Line 13B, Other interest expense specifically allocable
            under Regulations section 1.861-10T
        otherInterestExpenseTotal:
          type: number
          description: Section 3, Line 13C, Column (c), Other interest expense Form for 8993, Total amount
        totalAvgValueOfAssets:
          $ref: '#/components/schemas/InterestDeductionAndExpenseInfo'
          description: Section 3, Line 14A, Total average value of assets
        section734b743bAdjustmentAsset:
          $ref: '#/components/schemas/InterestDeductionAndExpenseInfo'
          description: Section 3, Line 14B, Sections 734(b) and 743(b) adjustment to assets — average value
        assetInterestExpense186110e:
          $ref: '#/components/schemas/InterestDeductionAndExpenseInfo'
          description: Section 3, Line 14C, Assets attracting directly allocable interest expense under
            Regulations section 1.861-10(e)
        otherAssetInterestExpense186110t:
          $ref: '#/components/schemas/InterestDeductionAndExpenseInfo'
          description: Section 3, Line 14D, Other assets attracting directly allocable interest expense
            under Regulations section 1.861-10T
        assetsExcludedApportionment:
          $ref: '#/components/schemas/InterestDeductionAndExpenseInfo'
          description: Section 3, Line 14E, Assets excluded from apportionment formula
        totalAssetsUsedApportionment:
          $ref: '#/components/schemas/InterestDeductionAndExpenseInfo'
          description: Section 3, Line 14F, Total assets used for apportionment
            (the sum of lines 14C, 14D, and 14E subtracted from the sum of lines 14A and 14B)
        grossReceiptsSicCode:
          type: array
          description: Section 3, Line 15, A-C, R&E expenses apportionment, Gross receipts by SIC code
          items:
            $ref: '#/components/schemas/ReGrossReceiptsBySicCode'
        reExpensesSicCode:
          type: array
          description: Section 3, Line 16, A-C, R&E expenses apportionment, R&E expenses by SIC code
          items:
            $ref: '#/components/schemas/ResearchExperimentalExpensesBySicCode'

    ForeignDerivedDeductionEligibleIncome:
      title: Foreign Derived Deduction Eligible Income
      description: Part IV, Section 2, Lines 9-11, Information to determine
        Foreign Derived Deduction Eligible Income (FDDEI) on Form 8993
      type: object
      properties:
        fdiAllSalesGeneralProperty:
          type: number
          description: Column (a), Foreign-derived income from all sales of general property
        fdiAllSalesIntangibleProperty:
          type: number
          description: Column (b), Foreign-derived income from all sales of intangible property
        fdiAllServices:
          type: number
          description: Column (c), Foreign-derived income from all services
        total:
          type: number
          description: Column (d), Total amount (add columns (a) through (c))

    InterestDeductionAndExpenseInfo:
      title: Interest Deduction And Expense Info
      description: Part IV, Section 3, Lines 13 A-C, 14 A-F, 15 A-C, Interest deductions and expense info
      type: object
      properties:
        deductionEligibleIncome:
          type: number
          description: Column (a), Deduction Eligible Income (DEI) amount
        fddei:
          type: number
          description: Column (b), Foreign Derived Deduction Eligible Income (FDDEI) amount
        total:
          type: number
          description: Column (c), Total amount

    ReGrossReceiptsBySicCode:
      title: Research and Experimental Gross Receipts By SIC Code
      description: Part IV, Section 3, Line 15 A-C, Research and Experimental Gross Receipts by SIC code
      type: object
      allOf:
        - $ref: '#/components/schemas/InterestDeductionAndExpenseInfo'
        - type: object
          properties:
            sicCode:
              type: string
              description: Part IV, Section 3, Line 15 A-C, SIC code

    Part5ForeignCorpDistributionPartnership:
      title: Part 5, Foreign Corp Distribution Partnership
      description: Part V, Lines A-O, Distributions from Foreign Corporations to Partnership
      type: object
      properties:
        alphaRowId:
          type: string
          description: Table row identifier
        name:
          $ref: './fdxapi.components.yaml#/components/schemas/BusinessName'
          description: Column (a), Name of distributing foreign corporation
        ein:
          type: string
          description: Column (b), EIN
        foreignEntityId:
          type: array
          description: Column (b), Reference ID
          items:
            type: string
        distributionDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Column (c), Date of distribution
        functionalCurrencyCode:
          $ref: './fdxapi.components.yaml#/components/schemas/Iso4217CurrencyCode'
          description: Column (d), Functional currency of distributing foreign corporation
        distributionFunctionalCurrency:
          type: number
          description: Column (e), Amount of distribution in functional currency - Foreign
        distributionFromEpFunctionalCurrency:
          type: number
          description: Column (f), Amount of Earnings and Profits distribution in functional currency - Foreign
        spotRate:
          type: number
          description: Column (g), Spot rate (functional currency to U.S. dollars)
        distribution:
          type: number
          description: Column (h), Amount of distribution in U.S. dollars
        epDistribution:
          type: number
          description: Column (i), Amount of Earnings and Profits distribution in U.S. dollars
        qualifiedForeignCorporation:
          type: boolean
          description: Column (j), Qualified foreign corporation

    Part6PartnerSection951a1Inclusion:
      title: Part 6 Partner Section 951(a)(1) Inclusion
      description: Part VI, Lines a-b, A-K, 1, Information on Partners' Section 951(a)(1) and Section 951A Inclusions
      type: object
      properties:
        separateCategoryCode:
          type: string
          description: Line a, Separate category code
        usSourceIncome:
          type: boolean
          description: Line b, U.S. Source indicator
        partnershipCfcOwnerInfo:
          type: array
          description: Detail lines, Part VI, Lines A-K, table columns (a)-(n)
          items:
            $ref: '#/components/schemas/PartnershipCfcOwnerInfo'
        totalPartnershipCfcOwnerInfo:
          description: Totals, Part VI, Line 1, Columns (e)-(n)
          $ref: '#/components/schemas/PartnershipCfcOwnerInfo'

    PartnershipCfcOwnerInfo:
      title: Partnership Cfc Owner Info
      description: Information on Partners' Section 951(a)(1) and Section 951A Inclusions,
        for Part VI, Lines A-K, Columns (a)-(n); and Totals, Part VI, Line 1, Columns (e)-(n)
      type: object
      properties:
        alphaRowId:
          type: string
          description: Lines A-K, Table row identifier
        name:
          $ref: './fdxapi.components.yaml#/components/schemas/BusinessName'
          description: Lines A-K, column (a), Name of Controlled Foreign Corporation (CFC)
        ein:
          type: string
          description: Lines A-K, column (b), Foreign corporation EIN
        foreignEntityId:
          type: array
          description: Lines A-K, column (b), Reference ID
          items:
            type: string
        cfcTaxYearEndDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Lines A-K, column (c), Ending of Controlled Foreign Corporation (CFC) tax year
        aggregateShareCfcItemsPartnershipOwnerRate:
          type: number
          description: Lines A-K, column (d), Partner's share of CFC items through its ownership in the partnership
            (aggregate share)
        aggregateShareSubpartFIncome:
          type: number
          description: Lines A-K and 1, column (e), Partner's share of subpart F income
        aggregateSection951a1bInclusion:
          type: number
          description: Lines A-K and 1, column (f), Partner's section 951(a)(1)(B) inclusion
        testedIncome:
          type: number
          description: Lines A-K and 1, column (g), Tested income
        testedLoss:
          type: number
          description: Lines A-K and 1, column (h), Tested loss
        aggregateShareTestedIncome:
          type: number
          description: Lines A-K and 1, column (i), Partner's share of tested income
        aggregateShareTestedLoss:
          type: number
          description: Lines A-K and 1, column (j), Partner's share of tested loss
        aggregateShareQbai:
          type: number
          description: Lines A-K and 1, column (k), Partner's share of Qualified Business Asset Investment (QBAI)
        aggregateShareTestedLossQbai:
          type: number
          description: Lines A-K and 1, column (l), Partner's share of the tested loss QBAI amount
        aggregateShareTestedInterestIncome:
          type: number
          description: Lines A-K and 1, column (m), Partner's share of tested interest income
        aggregateShareTestedInterestExpense:
          type: number
          description: Lines A-K and 1, column (n), Partner's share of tested interest expense

    Part7InfoToComplete8621:
      title: Part 7, Info To Complete 8621
      description: Part VII, Information Regarding Passive Foreign Investment Companies (PFICs),
        to complete Form 8621; Section 1, General Information, and Section 2,
        Additional Information on PFIC or Qualified Electing Fund (QEF)
      type: object
      properties:
        alphaRowId:
          type: string
          description: Table row identifier
        name:
          description: Sections 1 and 2, column (a), Name of Passive Foreign Investment Company (PFIC)
          $ref: './fdxapi.components.yaml#/components/schemas/BusinessName'
        ein:
          type: string
          description: Sections 1 and 2, column (b), Employer identification number (EIN)
        foreignEntityId:
          type: array
          description: Sections 1 and 2, column (b), Reference ID
          items:
            type: string
        usAddress:
          $ref: './fdxapi.components.yaml#/components/schemas/Address'
          description: Section 1, column (c), Address of Passive Foreign Investment Company (PFIC)
        foreignAddress:
          $ref: './fdxapi.components.yaml#/components/schemas/Address'
          description: Section 1, column (c), Address of Passive Foreign Investment Company (PFIC)
        taxYearBegin:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Section 1, column (d), Beginning of PFIC tax year
        taxYearEnd:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Section 1, column (e), Ending of PFIC tax year
        classOfShareCode:
          type: string
          description: Section 1, column (f), Description of each class of PFIC shares
        dateSharesAcquired:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Section 1, column (g), Dates PFIC shares acquired during tax year
        totalPficSharesTaxYearEndCount:
          type: number
          description: Section 1, column (h), Partner's share of total number of PFIC shares
            held by partnership at end of tax year
        totalPficSharesTaxYearEnd:
          type: number
          description: Section 1, column (i), Partner's share of total value of PFIC shares
            held by partnership at end of tax year
        partnershipElectionCode:
          type: string
          description: Section 1, column (j), Election made by partnership (enter code)
        qualifiedInsuranceCorpElection:
          type: boolean
          description: Section 1, column (k), Qualified insurance corporation election -
            Foreign corporation has documented its eligibility to be treated as
            a qualifying insurance corporation under section 1297(f)(2)
        pficSharesMarketableStock:
          type: boolean
          description: Section 1, column (l), PFIC has indicated its shares
            are "marketable stock" within the meaning of section 1296(e)
        pficCfcUnderSection957:
          type: boolean
          description: Section 1, column (m), PFIC is also a CFC within the meaning of section 957
        pficIncomeAssetTestMetSection1297a:
          type: boolean
          description: Section 1, column (n), PFIC meets the income test
            or asset test of section 1297(a) for the final tax year
        ordinaryEarnings:
          type: number
          description: Section 2, column (c), Partner's share of ordinary earnings
        netCapitalGain:
          type: number
          description: Section 2, column (d), Partner's share of net capital gain
        fmvOfPficSharesTaxYearBegin:
          type: number
          description: Section 2, column (e), Partner's share of Fair Market Value (FMV) of PFIC
            shares held by partnership at beginning of tax year
        fmvOfPficSharesTaxYearEnd:
          type: number
          description: Section 2, column (f), Partner's share of FMV of PFIC
            shares held by partnership at end of tax year
        sharesAcquiredDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Section 2, column (g), Date PFIC shares were acquired
        pficCashDistributedPropertyFmv:
          type: number
          description: Section 2, column (h), Amount of cash and fair market
            value of property distributed by PFIC during the current tax year
        distributionDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Section 2, column (i), Dates of distribution
        totalPficCreditableForeignTaxesDistribution:
          type: number
          description: Section 2, column (j), Partner's share of total creditable foreign
            taxes attributable to distribtion by PFIC
        totalPficDistributionPrior3TaxYears:
          type: number
          description: Section 2, column (k), Partner's share of total distributions from
            PFIC in preceding 3 tax years
        dispositionDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Section 2, column (l), Date PFIC shares disposed of during tax year
        pficSharesDispositionRealized:
          type: number
          description: Section 2, column (m), Partner's share of amount realized by partnership
            on disposition of PFIC shares
        pficSharesTaxBasis:
          type: number
          description: Section 2, column (n), Partner's share of partnership's tax basis in PFIC shares
            on dates of disposition (including partner-specific adjustments)
        pficSharesDispositionGainLoss:
          type: number
          description: Section 2, column (o), Partner's share of gain (loss) on disposition
            by partnership of PFIC shares

    Part8PartnershipForeignCorpIncome:
      title: Part 8, Partnership Foreign Corp Income
      description: Part VIII, Partnership's Interest in Foreign Corporation Income (Section 960)
      type: object
      properties:
        ein:
          type: string
          description: Part VIII, Line A, EIN of Controlled Foreign Corporation (CFC)
        foreignEntityId:
          type: array
          description: Part VIII, Line A, Reference ID of Controlled Foreign Corporation (CFC)
          items:
            type: string
        separateCategoryCode:
          type: string
          description: Part VIII, Line B, Separate category code
        passiveCategoryIncomeGroupCode:
          type: string
          description: Part VIII, Line C, Passive Grouping Code under Regulations section 1.904-4(c),
            if category code "PAS" was entered on line B
        multipleSourceCountry:
          type: boolean
          description: Part VIII, Line D, Multiple source countries present for a line
        usSourceIncome:
          type: boolean
          description: Part VIII, Line E, U.S. Source indicator
        fogeiOrFori:
          type: boolean
          description: Part VIII, Line F, Foreign Oil Related Income (FORI) or
            Foreign Oil and Gas Extraction Income (FOGEI) indicator
        functionalCurrencyCode:
          $ref: './fdxapi.components.yaml#/components/schemas/Iso4217CurrencyCode'
          description: Part VIII, Line G, Functional currency of foreign corporation
        totalDividendInterestRentsRoyaltiesAnnuities:
          $ref: '#/components/schemas/SubpartFForeignCorpIncome'
          description: Part VIII, Line 1 a, Total Dividends, Interest, Rents, Royalties, and Annuities
        dividendInterestRentsRoyaltiesAnnuities:
          type: array
          description: Part VIII, Line 1 a, Dividends, interest, rents, royalties, and annuities
          items:
            $ref: '#/components/schemas/SubpartFForeignCorpIncomeDetail'
        totalNetGainCertainProperties:
          $ref: '#/components/schemas/SubpartFForeignCorpIncome'
          description: Part VIII, Line 1 b, Total net gain from certain property transactions
        netGainCertainProperties:
          type: array
          description: Part VIII, Line 1 b, Net gain from certain property transactions
          items:
            $ref: '#/components/schemas/SubpartFForeignCorpIncomeDetail'
        totalNetGainCommodities:
          $ref: '#/components/schemas/SubpartFForeignCorpIncome'
          description: Part VIII, Line 1 c, Total net gain from commodities transactions
        netGainCommodities:
          type: array
          description: Part VIII, Line 1 c, Net gain from commodities transactions
          items:
            $ref: '#/components/schemas/SubpartFForeignCorpIncomeDetail'
        totalNetForeignCurrencyGain:
          $ref: '#/components/schemas/SubpartFForeignCorpIncome'
          description: Part VIII, Line 1 d, Total net foreign currency gain
        netForeignCurrencyGain:
          type: array
          description: Part VIII, Line 1 d, Net foreign currency gain
          items:
            $ref: '#/components/schemas/SubpartFForeignCorpIncomeDetail'
        totalIncomeEquivalentInterest:
          $ref: '#/components/schemas/SubpartFForeignCorpIncome'
          description: Part VIII, Line 1 e, Total income equivalent to interest
        incomeEquivalentInterest:
          type: array
          description: Part VIII, Line 1 e, Income equivalent to interest
          items:
            $ref: '#/components/schemas/SubpartFForeignCorpIncomeDetail'
        subpartFOther:
          type: array
          description: Part VIII, Line 1 f, Totals with descriptions, Other Foreign Personal Holding Company Income
          items:
            $ref: '#/components/schemas/SubpartFOther'
        other:
          type: array
          description: Part VIII, Line 1 f, Other Foreign Personal Holding Company Income
          items:
            $ref: '#/components/schemas/SubpartFForeignCorpIncomeDetail'
        totalForeignBaseCorpSalesIncome:
          $ref: '#/components/schemas/SubpartFForeignCorpIncome'
          description: Part VIII, Line 1 g, Total foreign base company sales income
        foreignBaseCorpSalesIncome:
          type: array
          description: Part VIII, Line 1 g, Foreign base company sales income
          items:
            $ref: '#/components/schemas/SubpartFForeignCorpIncomeDetail'
        totalForeignBaseCorpServicesIncome:
          $ref: '#/components/schemas/SubpartFForeignCorpIncome'
          description: Part VIII, Line 1 h, Total foreign base company services income
        foreignBaseCorpServicesIncome:
          type: array
          description: Part VIII, Line 1 h, Foreign base company services income
          items:
            $ref: '#/components/schemas/SubpartFForeignCorpIncomeDetail'
        totalInclusionForeignBaseCorpIncome:
          $ref: '#/components/schemas/SubpartFForeignCorpIncome'
          description: Part VIII, Line 1 i, Total full inclusion foreign base company income
        inclusionForeignBaseCorpIncome:
          type: array
          description: Part VIII, Line 1 i, Full inclusion foreign base company income
          items:
            $ref: '#/components/schemas/SubpartFForeignCorpIncomeDetail'
        totalInsuranceIncome:
          $ref: '#/components/schemas/SubpartFForeignCorpIncome'
          description: Part VIII, Line 1 j, Total insurance income
        insuranceIncome:
          type: array
          description: Part VIII, Line 1 j, Insurance income
          items:
            $ref: '#/components/schemas/SubpartFForeignCorpIncomeDetail'
        totalInternationalBoycottIncome:
          $ref: '#/components/schemas/SubpartFForeignCorpIncome'
          description: Part VIII, Line 1 k, Total International boycott income
        totalBribesKickbacksPayments:
          $ref: '#/components/schemas/SubpartFForeignCorpIncome'
          description: Part VIII, Line 1 k, Total bribes, kickbacks, and other payments
        totalSection901jIncome:
          $ref: '#/components/schemas/SubpartFForeignCorpIncome'
          description: Part VIII, Line 1 k, Total section 901(j) income
        recapturedSubpartFIncome:
          $ref: '#/components/schemas/SubpartFForeignCorpIncome'
          description: Part VIII, Line 2, Total recaptured subpart F income
        totalTestedIncome:
          $ref: '#/components/schemas/SubpartFForeignCorpIncome'
          description: Part VIII, Line 3, Total tested income group
        testedIncome:
          type: array
          description: Part VIII, Line 3, Tested income group
          items:
            $ref: '#/components/schemas/SubpartFForeignCorpIncomeDetail'
        totalResidualIncome:
          $ref: '#/components/schemas/SubpartFForeignCorpIncome'
          description: Part VIII, Line 4, Total residual income group
        residualIncome:
          type: array
          description: Part VIII, Line 4, Residual income group
          items:
            $ref: '#/components/schemas/SubpartFForeignCorpIncomeDetail'
        cfcTotalIncome:
          $ref: '#/components/schemas/SubpartFForeignCorpIncome'
          description: Part VIII, Line 5, Total CFC income

    SubpartFForeignCorpIncome:
      title: Total Subpart F Foreign Corp Income
      description: Part VIII, Partnership's Interest in Foreign Corporation Income (Section 960),
        Total of Subpart F Foreign Corporation Income
      type: object
      properties:
        foreignUsCountryCode:
          $ref: './fdxapi.components.yaml#/components/schemas/Iso3166CountryCode'
          description: Part VIII, Detail lines 1a-1j & 3-4, Total lines 1k-1m & 2, column (i), row Country code.
            Use ISO-defined country codes to deliver to taxpayers and tax preparation software,
            for delivery to IRS they will need to be mapped to IRS country codes
        netIncome:
          type: number
          description: Part VIII, Lines 1-5, column (ii), Partner's share of foreign corporation's net income
            (in functional currency)
        cfcTotalNetIncome:
          type: number
          description: Part VIII, Lines 1 & 3-5, column (iii), Foreign corporation's total net income
            (in functional currency)
        cfcCurrentYearForeignTaxesCreditAllowed:
          type: number
          description: Part VIII, Lines 1, 3 & 5, column (iv), Foreign corporation's current year foreign taxes
            for which credit allowed (in US dollars)

    SubpartFForeignCorpIncomeDetail:
      title: Subpart F Foreign Corp Income Detail
      description: Part VIII, Partnership's Interest in Foreign Corporation Income (Section 960),
        Details of Subpart F Foreign Corporation Income
      type: object
      allOf:
        - $ref: '#/components/schemas/SubpartFForeignCorpIncome'
        - type: object
          properties:
            numericRowId:
              type: number
              description: Part VIII, Detail lines 1a-1j & 3-4, table row identifier
            name:
              $ref: './fdxapi.components.yaml#/components/schemas/BusinessName'
              description: Part VIII, Detail lines 1a-1j & 3-4, row Qualified Business Unit Name

    SubpartFOther:
      title: Subpart F Other
      description: Part VIII, Partnership's Interest in Foreign Corporation Income (Section 960),
        Details of Subpart F Foreign Corporation Income
      type: object
      allOf:
        - $ref: '#/components/schemas/SubpartFForeignCorpIncome'
        - type: object
          properties:
            otherIncomeDesc:
              type: string
              description: Other Income Description

    Part9PartnerInfoBeat:
      title: Part 9, Partner Info BEAT
      description: Part IX, Partner's Information for Base Erosion and Anti-Abuse Tax (BEAT), Section 59A
      type: object
      properties:
        grossReceiptsSection59Ae:
          $ref: '#/components/schemas/GrossReceiptsTotal'
          description: Part IX, Section 1, Line 1, Gross receipts for section 59A(e)
        grossReceipts1stPriorYear:
          $ref: '#/components/schemas/GrossReceiptsTotal'
          description: Part IX, Section 1, Line 2, Gross receipts for the first preceding year
        grossReceipts2ndPriorYear:
          $ref: '#/components/schemas/GrossReceiptsTotal'
          description: Part IX, Section 1, Line 3, Gross receipts for the second preceding year
        grossReceipts3rdPriorYear:
          $ref: '#/components/schemas/GrossReceiptsTotal'
          description: Part IX, Section 1, Line 4, Gross receipts for the third preceding year
        totalBaseErosionPercentSection159a2:
          type: number
          description: Part IX, Section 1, Line 5, Column (a), Total amounts included in the
            denomnator of the base percentage as described in Regulations section 1.59A-2(e)(3)
        purchaseCreationPropertyRightsIntangible:
          $ref: '#/components/schemas/BaseErosionTotal'
          description: Part IX, Section 2, Line 8, Purchase or creations of property rights for intangibles
            (patents, trademarks, etc.)
        rentsRoyaltiesLicenseFees:
          $ref: '#/components/schemas/BaseErosionTotal'
          description: Part IX, Section 2, Line 9, Rents, royalties, and license fees
        compPaidServicesNotExceptSection59ad5:
          $ref: '#/components/schemas/BaseErosionTotal'
          description: Part IX, Section 2, Line 10a, Compensation/consideration paid for services
            NOT excepted by section 59A(d)(5)
        totalCompPaidServicesExceptSection59ad5:
          type: number
          description: Part IX, Section 2, Line 10b, Column (a), Total - Compensation/consideration
            paid for services EXCEPTED by section 59A(d)(5)
        baseErosionInterestExpense:
          $ref: '#/components/schemas/BaseErosionTotal'
          description: Part IX, Section 2, Line 11, Interest expense
        paymentForPurchaseTangiblePersonalProperty:
          description: Part IX, Section 2, Line 12, Payments for the purchase of tangible personal property
          $ref: '#/components/schemas/BaseErosionTotal'
        premiumPaidOrAccruedForInsuranceSection59a:
          description: Part IX, Section 2, Line 13, Premiums and/or other considerations paid or accrued
            for insurance and reinsurance as covered by sections 59A(d)(3) and 59A(c)(2)(A)(iii)
          $ref: '#/components/schemas/BaseErosionTotal'
        nonQualifyingDerivativePayments:
          $ref: '#/components/schemas/BaseErosionTotal'
          description: Part IX, Section 2, Line 14a, Non-qualified derivative payments
        qualifiedDerivativePaymentExceptSection59:
          type: number
          description: Part IX, Section 2, Line 14b, Column (a), Total - Qualified derivative
            payments EXCEPTED by section 59A(h)
        paymentReduceGrossReceiptsSurrogateForeignCorp:
          description: Part IX, Section 2, Line 15, Payments reducing gross receipts made to
            surrogate foreign corporations
          $ref: '#/components/schemas/BaseErosionTotal'
        baseErosionOtherPayments:
          type: array
          description: Part IX, Section 2, Line 16, Other payments
          items:
            $ref: '#/components/schemas/BaseErosionOther'
        baseErosionTaxBenefit:
          type: number
          description: Part IX, Section 2, Line 17, column (c), Base Erosion Tax Benefits,
            related to payments reported on lines 6 through 16, on which tax is imposed by
            section 871 or 881, with respect to which tax has been withheld under
            section 1441 or 1442 at the 30% (0.30) statutory withholding tax rate
        portionBaseErosionTaxBenefit:
          type: number
          description: Part IX, Section 2, Line 18, column (c), Portion of base erosion tax benefits,
            reported on lines 6 through 16, on which tax is imposed by section 871 or 881,
            with respect to which tax has been withheld under section 1441 or 1442 at reduced
            withholding rate pursuant to income tax treaty.
            Multiply ratio of percentage withheld divided by 30% (0.30) times tax benefit
        totalBaseErosionTaxBenefit:
          type: number
          description: Part IX, Section 2, Line 19, Column (c), Total base erosion tax benefits
            (subtract the sum of lines 17 and 18 from the sum of lines 8 through 16)

    GrossReceiptsTotal:
      title: Gross Receipts Total
      description: Part IX, Section 1, Lines 1-4, Gross Receipts Totals
      type: object
      properties:
        total:
          type: number
          description: Lines 1-4, column (a), Total amount
        totalEciGrossReceipts:
          type: number
          description: Lines 1-4, column (b), Total ECI gross receipts
        totalNonEciGrossReceipts:
          type: number
          description: Lines 1-4, column (c), Total non-ECI gross receipts

    BaseErosionTotal:
      title: Base Erosion Total
      description: Part IX, Section 2, Lines 8-16, Base Erosion Payments and Base Erosion Tax Benefits
      type: object
      properties:
        total:
          type: number
          description: Lines 8-16, column (a), Total amount
        totalBaseErosionPayment:
          type: number
          description: Lines 8-16, column (b), Total base erosion payments
        totalBaseErosionTaxBenefit:
          type: number
          description: Lines 8-16, column (c), Total base erosion tax benefits

    BaseErosionOther:
      title: Base Erosion Other
      description: Part IX, Section 2, Line 16, Base Erosion Other Payments
      type: object
      allOf:
        - $ref: '#/components/schemas/BaseErosionTotal'
        - type: object
          properties:
            otherPaymentsDesc:
              type: string
              description: Section 2, Line 16, Other payments description
            partnerRelationshipDesc:
              type: string
              description: Section 2, Line 16, Partner relationship description

    Part10ForeignPartnerSourceIncomeDeduction:
      title: Part 10, Foreign Partner Source Income Deduction
      description: Part X, Foreign Partner's Character and Source of Income and Deductions,
        Section 1, Lines 1-14 & 20-21, Gross Income,
        and Section 2, Lines 1-18 & 24-25, Deductions, Losses, and Net Income,
        and Section 3, Lines 1-5 & 7-8, Allocation and Apportionment Methods for Deductions
      type: object
      properties:
        ordinaryBusinessIncomeGross:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 1, Line 1, Ordinary business income (gross)
        grossRentalRealEstateIncome:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 1, Line 2, Gross rental real estate income
        otherGrossRentalIncome:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 1, Line 3, Other gross rental income
        guaranteedPaymentsForServices:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 1, Line 4, Guaranteed payments for services
        guaranteedPaymentForUseOfCap:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 1, Line 5, Guaranteed payments for use of capital
        interestIncome:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 1, Line 6, Interest income
        dividends:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 1, Line 7, Dividends
        dividendEquivalents:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 1, Line 8, Dividend equivalents
        royaltiesAndLicenseFees:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 1, Line 9, Royalties and license fees
        netShortTermCapGain:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 1, Line 10, Net short-term capital gain
        netLongTermCapGain:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 1, Line 11, Net long-term capital gain
        collectible28PercentGain:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 1, Line 12, Collectibles (28%) gain
        grossIncomeUnrecapturedSection1250Gain:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 1, Line 13, Unrecaptured section 1250 gain
        netSection1231Gain:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 1, Line 14, Net section 1231 gain
        otherIncomeLoss:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 1, Line 20, Other income (loss) not included on lines 1-19
        grossIncomeTotal:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 1, Line 21, Gross income (sum of lines 1-20)
        expensesRelatedOrdinaryBusinessIncomeGross:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 2, Line 1, Expenses related to ordinary business income (gross)
        researchExperimentalExpenses:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 2, Line 2, Research and Experimental expenses
        expensesFromRentalRealEstate:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 2, Line 3, Expenses from rental real estate
        expensesFromOtherRentalActivity:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 2, Line 4, Expenses from other rental activities
        royaltyAndLicensingExpenses:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 2, Line 5, Royalty and licensing expenses
        section179Deduction:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 2, Line 6, Section 179 deduction
        interestExpenseUsBookedLiabilities:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 2, Line 7, Interest expense on US-booked liabilities
        interestExpenseDirectAllocableUnderRegs:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 2, Line 8, Interest expense directly allocable under
            Regulations sections 1.882-5(a)(1)(ii)(B) and 1.861-10T
        otherInterestExpense:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 2, Line 9, Other interest expense
        section59e2Expenditures:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 2, Line 10, Section 59(e)(2) expenditures
        netShortTermCapLoss:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 2, Line 11, Net short-term capital loss
        netLongTermCapLoss:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 2, Line 12, Net long-term capital loss
        collectiblesLoss:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 2, Line 13, Collectibles loss
        netSection1231Loss:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 2, Line 14, Net section 1231 loss
        otherLosses:
          type: array
          description: Section 2, Line 15, Other losses
          items:
            $ref: '#/components/schemas/OtherLossOrDeduction'
        charitableContributions:
          $ref: '#/components/schemas/Contribution'
          description: Section 2, Line 16, Charitable contributions
        otherDeductions:
          type: array
          description: Section 2, Lines 17-18, Other deductions
          items:
            $ref: '#/components/schemas/OtherLossOrDeduction'
        totalDeductionsLossesNetIncome:
          $ref: '#/components/schemas/PartnershipDetermination'
          description: Section 2, Line 24, Total (sum of lines 1-23)
        totalNetIncomeLoss:
          type: number
          description: Section 2, Line 25, Net income (loss)
            (Section 1 line 21 minus Section 2 line 24)
        grossEci:
          type: number
          description: Section 3, Line 1a, Gross ECI income
        worldwideGrossIncome:
          type: number
          description: Section 3, Line 1b, Worldwide gross income
        averageUsAssets:
          type: number
          description: Section 3, Line 2a, Average U.S. assets (inside basis)
        worldwideAssets:
          type: number
          description: Section 3, Line 2b, Worldwide assets
        usBookedLiabilities:
          type: number
          description: Section 3, Line 3a, US-booked liabilities of partnership
        directlyAllocatedPartnershipDebt:
          type: number
          description: Section 3, Line 3b, Directly allocated partnership indebtedness
        personnelWithinUsCount:
          type: number
          description: Section 3, Line 4a, Personnel of US trade or business
        worldwidePersonnelCount:
          type: number
          description: Section 3, Line 4b, Worldwide personnel
        grossReceiptsBySicCode:
          type: array
          description: Section 3, Line 5, Gross receipts from sales or services by SIC code
          items:
            $ref: '#/components/schemas/GrossReceiptsBySicCode'
        otherAllocationAndApportionmentKey1:
          type: array
          description: Section 3, Line 7, Other allocation and apportionment key
          items:
            $ref: '#/components/schemas/OtherAllocationAndApportionmentKey'
        otherAllocationAndApportionmentKey2:
          type: array
          description: Section 3, Line 8, Other allocation and apportionment key
          items:
            $ref: '#/components/schemas/OtherAllocationAndApportionmentKey'

    PartnershipDetermination:
      title: Partnership Determination
      description: Part X, Section 1, Lines 1-14 & 20-21, Partnership Determination Gross Income
        and Part X, Section 2, Lines 1-15, 17-18 & 24, Partnership Determination Deductions, Losses, and Net Income
      type: object
      properties:
        total:
          type: number
          description: Column (a), Total amount
        partnerDetermination:
          type: number
          description: Column (b), Partner determination
        eciUsSource:
          type: number
          description: Column (c), ECI - U.S. source
        eciForeignSource:
          type: number
          description: Column (d), ECI - Foreign source
        nonEciUsSourceFdap:
          type: number
          description: Column (e), Non-ECI - U.S. source (FDAP)
        nonEciUsSourceOther:
          type: number
          description: Column (f), Non-ECI - U.S. source (other)
        nonEciForeignSource:
          type: number
          description: Column (g), Non-ECI - Foreign source

    OtherLossOrDeduction:
      title: Other Loss
      description: Part X, Section 2, Lines 15 & 17-18, Partnership Determination,
        Other Losses and Deductions
      type: object
      allOf:
        - $ref: '#/components/schemas/PartnershipDetermination'
        - type: object
          properties:
            otherDescription:
              type: string
              description: Line 15, Other losses type, and Lines 17-18, Other deductions type

    Contribution:
      title: Contribution
      description: Part X, Section 2, Line 16, Partnership Determination, Charitable contributions
      type: object
      properties:
        total:
          type: number
          description: Line 16, column (a), Total amount
        eciUsSource:
          type: number
          description: Line 16, column (c), ECI - U.S. source

    GrossReceiptsBySicCode:
      title: Gross Receipts By SIC Code
      description: Part X, Section 3, Line 5, Gross Receipts from sales or services by SIC code
      type: object
      properties:
        sicCode:
          type: string
          description: Column (i), SIC code
        eci:
          type: number
          description: Column (ii), ECI gross receipts
        worldwideGrossReceiptsFromSales:
          type: number
          description: Column (iii), Worldwide gross receipts

    OtherAllocationAndApportionmentKey:
      title: Other Allocation And Apportionment Key
      description: Part X, Section 3, Lines 7-8, Other allocation and apportionment key
      type: object
      properties:
        alphaRowId:
          type: string
          description: Table row identifier
        keyFactor:
          type: string
          description: Lines 7-8, Column (i), Apportionment Key/Factor
        allocation:
          type: number
          description: Lines 7-8, Column (ii), Allocation

    Part11CoveredPartnerships:
      title: Part 11, Covered Partnerships
      description: Part XI, Section 871(m) Covered Partnerships
      type: object
      properties:
        coveredPartnership:
          type: boolean
          description: Part XI, Line 1, Partnership is a publicly
            traded partnership as defined in section 7704(b) and the partnership
            is (a) a covered partnership as defined in Regulations section 1.871-15(m)(1)
            or (b) directly or indirectly holds an interest in a lower-tier partnership
            that is a covered partnership
        unitsHeldByPartnerCount:
          type: number
          description: Part XI, Line 2, Number of units held by the partner
        dividendsPerAllocationPeriod:
          type: array
          description: Part XI, Line 3, Table of dividends for each allocation period
          items:
            $ref: '#/components/schemas/DividendsPerAllocationPeriod'

    DividendsPerAllocationPeriod:
      title: Dividends Per Allocation Period
      description: Part XI, Line 3, Table of dividends for each allocation period
      type: object
      properties:
        allocationPeriodBeginDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Part XI, Line 3, column (i), Beginning of allocation period
        allocationPeriodEndDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Part XI, Line 3, column (ii), End of allocation period
        dividends:
          type: number
          description: Part XI, Line 3, column (iii), Dividends (enter four decimal places)
        dividendEquivalents:
          type: number
          description: Part XI, Line 3, column (iv), Dividend Equivalents (enter four decimal places)
        total:
          type: number
          description: Part XI, Line 3, column (v), Total amount (enter four decimal places)

    Part13SharePartnershipInterestTransfer:
      title: Part 13, Share Partnership Interest Transfer
      description: Part XIII, Foreign Partner's Distributive Share of Deemed Sale Items on
        Transfer of Partnership Interest
      type: object
      properties:
        partnershipInterestTransferredDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Part XIII, Line A, Date of transfer of the partnership interest
        partnershipInterestTransferredPercent:
          type: number
          description: Part XIII, Line B1, Percentage interest in the partnership transferred
        partnershipUnitsTransferred:
          type: number
          description: Part XIII, Line B2, Number of units in the partnership transferred
        capital:
          type: boolean
          description: Part XIII, Line C1, Check if Capital
        preferred:
          type: boolean
          description: Part XIII, Line C2, Check if Preferred
        profits:
          type: boolean
          description: Part XIII, Line C3, Check if Profits
        other:
          type: boolean
          description: Part XIII, Line C4, Check if Other
        totalOrdinaryGainLossSection751:
          type: number
          description: Part XIII, Line 1, Total ordinary gain (loss) that would be
            recognized on the deemed sale of section 751 property
        totalEffectivelyConnectedOrdinaryGain751:
          type: number
          description: Part XIII, Line 2, Aggregate effectively connected ordinary gain (loss)
            that would be recognized on the deemed sale of section 751 property
        totalEffectivelyConnectedCapGainNon751:
          type: number
          description: Part XIII, Line 3, Aggregate effectively connected capital gain (loss)
            that would be recognized on the deemed sale of non-section 751 property
        totalEffectivelyConnectedSection1h5Assets:
          type: number
          description: Part XIII, Line 4, Aggregate effectively connected gain (loss)
            that would be recognized on the deemed sale of section 1(h)(5) collectible assets
        totalEffectivelyConnectedSection1h6Section1250:
          type: number
          description: Part XIII, Line 5, Aggregate effectively connected gain that would be
            recognized on the deemed sale of section 1(h)(6) unrecaptured section 1250 gain assets
        regsSection1864c81c2iie:
          type: boolean
          description: Part XIII, Line 6, Any amount on lines 2-5 is determined (in whole or in part)
            under Regulations section 1.864(c)(8)-1(c)(2)(ii)(E) (material change in circumstances
            rule for a deemed sale of the partnership's inventory property or intangibles)
        gainLossSection897g:
          type: number
          description: Part XIII, Line 7, Capital Gain (loss) that would be recognized
            under section 897(g) on the deemed sale of U.S. real proerty interests
        gainRecognizedSection897gSection1250:
          type: number
          description: Part XIII, Line 8, Gain that would be recognized under section 897(g)
            on the deemed sale of section 1(h)(6) unrecaptured section 1250 gain assets
