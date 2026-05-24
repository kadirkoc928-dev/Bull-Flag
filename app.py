import streamlit as st
import pandas as pd
from scanner import scan_all


# =========================
# TICKER LISTE
# =========================
def get_all_tickers():

    # =========================
    # S&P 500
    # =========================
    SP500 = [
        "A","AAL","AAPL","ABBV","ABNB","ABT","ACGL","ACN","ADBE","ADI","ADM","ADP","ADSK","AEE","AEP","AES",
        "AFL","AIG","AIZ","AJG","AKAM","ALB","ALGN","ALK","ALL","ALLE","AMAT","AMCR","AMD","AME","AMGN",
        "AMP","AMT","AMZN","ANET","ANSS","AON","AOS","APA","APD","APH","APTV","ARE","ATO","AVB","AVGO",
        "AVY","AWK","AXP","AZO","BA","BAC","BALL","BAX","BBWI","BBY","BDX","BEN","BF.B","BG","BIIB","BIO",
        "BK","BKNG","BKR","BLDR","BLK","BMY","BR","BRK.B","BRO","BSX","BWA","BXP","C","CAG","CAH","CARR",
        "CAT","CB","CBOE","CBRE","CCI","CCL","CDNS","CDW","CE","CEG","CF","CFG","CHD","CHRW","CHTR","CI",
        "CINF","CL","CLX","CMA","CMCSA","CME","CMG","CMI","CMS","CNC","CNP","COF","COO","COP","COR","COST",
        "CPAY","CPB","CPRT","CPT","CRL","CRM","CSCO","CSGP","CSX","CTAS","CTLT","CTRA","CTSH","CTVA","CVS",
        "CVX","CZR","D","DAL","DD","DE","DFS","DG","DGX","DHI","DHR","DIS","DLR","DLTR","DOV","DOW","DPZ",
        "DRI","DTE","DUK","DVA","DVN","DXCM","EA","EBAY","ECL","ED","EFX","EIX","EL","ELV","EMN","EMR",
        "ENPH","EOG","EPAM","EQIX","EQR","EQT","ES","ESS","ETN","ETR","ETSY","EVRG","EW","EXC","EXPD",
        "EXPE","EXR","F","FANG","FAST","FCX","FDS","FDX","FE","FFIV","FICO","FIS","FITB","FMC","FOX",
        "FOXA","FRT","FSLR","FTNT","FTV","GD","GE","GEHC","GEN","GILD","GIS","GL","GLW","GM","GNRC",
        "GOOG","GOOGL","GPC","GPN","GRMN","GS","GWW","HAL","HAS","HBAN","HCA","HD","HES","HIG","HII",
        "HLT","HOLX","HON","HPE","HPQ","HRL","HSIC","HST","HSY","HUBB","HUM","HWM","IBM","ICE","IDXX",
        "IEX","IFF","ILMN","INCY","INTC","INTU","INVH","IP","IPG","IQV","IR","IRM","ISRG","IT","ITW",
        "IVZ","J","JBHT","JBL","JCI","JKHY","JNJ","JNPR","JPM","K","KDP","KEY","KEYS","KHC","KIM",
        "KLAC","KMB","KMI","KMX","KO","KR","KVUE","L","LDOS","LEN","LH","LHX","LIN","LKQ","LLY","LMT",
        "LNC","LNT","LOW","LRCX","LULU","LUV","LVS","LW","LYB","LYV","MA","MAA","MAR","MAS","MCD",
        "MCHP","MCK","MCO","MDLZ","MDT","MET","META","MGM","MHK","MKC","MLM","MMC","MMM","MNST","MO",
        "MOH","MOS","MPC","MPWR","MRK","MRNA","MRO","MS","MSCI","MSFT","MSI","MTB","MTCH","MTD","MU",
        "NCLH","NDAQ","NDSN","NEE","NEM","NFLX","NI","NKE","NOC","NOW","NRG","NSC","NTAP","NTRS",
        "NUE","NVDA","NVR","NWL","NWS","NWSA","NXPI","O","ODFL","OKE","OMC","ON","ORCL","ORLY",
        "OTIS","OXY","PANW","PARA","PAYC","PAYX","PCAR","PCG","PEG","PEP","PFE","PFG","PG","PGR",
        "PH","PHM","PKG","PLD","PM","PNC","PNR","PNW","PODD","POOL","PPG","PPL","PRU","PSA","PSX",
        "PTC","PWR","PYPL","QCOM","QRVO","RCL","REG","REGN","RF","RHI","RJF","RL","RMD","ROK",
        "ROL","ROP","ROST","RSG","RTX","RVTY","SBAC","SBUX","SCHW","SHW","SJM","SLB","SMCI","SNA",
        "SNPS","SO","SPG","SPGI","SRE","STE","STLD","STT","STX","STZ","SWK","SWKS","SYF","SYK",
        "SYY","T","TAP","TDG","TDY","TECH","TEL","TER","TFC","TFX","TGT","TJX","TMO","TMUS","TPR",
        "TRGP","TRMB","TROW","TRV","TSCO","TSLA","TSN","TT","TTWO","TXN","TXT","TYL","UA","UAL",
        "UBER","UDR","UHS","ULTA","UNH","UNP","UPS","URI","USB","V","VFC","VICI","VLO","VLTO",
        "VMC","VRSK","VRSN","VRTX","VTR","VTRS","VZ","WAB","WAT","WBA","WBD","WDC","WEC","WELL",
        "WFC","WHR","WM","WMB","WMT","WRB","WST","WTW","WY","WYNN","XEL","XOM","XRAY","XYL",
        "YUM","ZBH","ZBRA","ZION","ZTS"
    ]

    # =========================
    # NASDAQ 100
    # =========================
    NASDAQ100 = [
        "AAPL","ABNB","ADBE","ADI","ADP","ADSK","AEP","AMAT","AMD","AMGN","AMZN","ANSS","ASML","AVGO",
        "AZN","BIIB","BKNG","BKR","CDNS","CDW","CEG","CHTR","CMCSA","COST","CPRT","CRWD","CSCO","CSGP",
        "CSX","CTAS","CTSH","DASH","DDOG","DLTR","DXCM","EA","EBAY","EXC","FANG","FAST","FTNT","GEHC",
        "GFS","GILD","GOOG","GOOGL","HON","IDXX","ILMN","INTC","INTU","ISRG","JD","KDP","KHC","KLAC",
        "LRCX","LULU","MAR","MCHP","MDB","MDLZ","MELI","META","MNST","MRNA","MRVL","MSFT","MU","NFLX",
        "NVDA","NXPI","ODFL","ON","ORLY","PANW","PAYX","PCAR","PDD","PEP","PYPL","QCOM","REGN","ROP",
        "ROST","SBUX","SWKS","TEAM","TMUS","TSLA","TXN","VRSK","VRTX","WBA","WBD","WDAY","XEL","ZS"
    ]

    # =========================
    # RUSSELL (gekürzt)
    # =========================
    RUSSELL = [
        "AAON","AAN","AAWW","ABCB","ABG","ABM","ABR","ACAD","ACCD","ACCO","ACEL","ACHC","ACIW",
    "ACLS","ACMR","ACRE","ACVA","ADMA","ADNT","ADUS","AEIS","AEO","AGIO","AGM","AGNC",
    "AGX","AHCO","AHH","AIRS","AIT","AIZ","AKRO","ALDX","ALEC","ALGM","ALIT","ALKS",
    "ALKT","ALRM","ALTR","ALVO","AMBA","AMCX","AMKR","AMPL","ANDE","ANIP","ANIX",
    "AORT","AOSL","APGE","APLS","APOG","APPF","APPN","AQST","ARCB","ARCT","ARDX",
    "ARHS","ARLO","ARQT","ARRY","ARVN","ASLE","ASPN","ASTE","ATGE","ATKR","ATRC",
    "ATRO","AVAV","AVNS","AVPT","AXGN","AXSM","AXTI","AZTA","BAND","BANF","BBIO",
    "BCPC","BCYC","BDSX","BECN","BELFB","BHE","BHF","BHRB","BIGC","BILL","BIOC",
    "BJRI","BKD","BLBD","BLFS","BLMN","BLNK","BLUE","BMI","BMRC","BNFT","BOC",
    "BOH","BPMC","BRKL","BRKR","BRP","BRY","BSIG","BSRR","BTBT","BTU","BWMN",
    "BYND","CARG","CASH","CATY","CBRL","CBSH","CCOI","CCRN","CDMO","CDNA","CDRE",
    "CEIX","CENT","CENTA","CERT","CEVA","CFB","CFFN","CGNX","CHCO","CHRD","CHRS",
    "CHX","CIO","CIVB","CLBK","CLDT","CLFD","CLMT","CLOV","CMBM","CMC","CMCO",
    "CNK","CNMD","CNOB","CNSL","CNTA","CORT","COST","COWN","CPRX","CPSI","CRAI",
    "CRBP","CRCT","CREE","CRK","CRMD","CRNX","CRSR","CSGS","CSQ","CTBI","CTLP",
    "CTMX","CTRE","CTRN","CTS","CVBF","CVCO","CVGW","CWBC","CWST","CYRX","DCPH",
    "DDI","DGII","DIOD","DKL","DLX","DNLI","DOCN","DOMO","DRQ","DSGN","DVAX",
    "DXPE","DYN","EBC","EBF","EBIX","EBS","ECPG","EDAP","EEFT","EGBN","EGHT",
    "EHTH","ELF","ENFN","ENR","ENS","ENTA","EOLS","EPAC","EPAM","EPC","EPRT",
    "EPZM","EQBK","ERAS","ERIE","ESCA","ETNB","ETON","EVC","EVER","EVH","EVRI",
    "EVTC","EXEL","EXPI","EXTR","EYE","FARO","FCBC","FCEL","FCFS","FDP","FELE",
    "FFBC","FFIN","FGEN","FHB","FIBK","FIVN","FLGT","FLIC","FLWS","FMBH","FNCB",
    "FORM","FOUR","FPI","FPRX","FRG","FRME","FROG","FRPT","FSLY","FSRV","FSS",
    "FTDR","FTRE","FULC","FULT","FWRD","GABC","GAIN","GCI","GDEN","GDRX","GEF",
    "GERN","GFF","GH","GIII","GLDD","GLNG","GLRE","GLUE","GMED","GNK","GNL",
    "GNTX","GO","GOOD","GOSS","GPI","GPK","GPOR","GRBK","GRPN","GSAT","GSHD",
    "GTLS","GVA","HAFC","HAIN","HALO","HAYN","HBI","HBNC","HCSG","HEAR","HEES",
    "HELE","HFWA","HI","HIBB","HIMX","HLIO","HLNE","HMN","HMST","HOPE","HSTM",
    "HTBI","HTBK","HTGC","HUBG","HURN","HVT","HWC","HWKN","HZO","IBEX","IBKR",
    "ICFI","ICHR","ICUI","IDCC","IDYA","IEA","IIIN","IMAX","IMGN","IMKTA","IMMR",
    "INDB","INMD","INN","INOD","INSM","INST","INTA","IONS","IOSP","IPAR","IRBT",
    "IRDM","IRTC","ISDR","ITGR","ITRI","IVAC","JACK","JAMF","JBGS","JBSS","JBT",
    "JELD","JOAN","JRVR","KAI","KALU","KARO","KBH","KELYB","KEX","KFRC","KFY",
    "KLIC","KMT","KNSA","KOP","KPTI","KRUS","KSS","KTOS","KURA","KVHI","KWR",
    "KZR","LAZR","LBRDA","LBTYA","LCII","LECO","LEG","LFUS","LGIH","LHCG","LIVN",
    "LMAT","LMNR","LNN","LPRO","LSTR","LTH","LTHM","LUMN","LXP","LYEL","LYTS",
    "MANH","MARPS","MASI","MATW","MCRI","MCS","MDGL","MDU","MEI","MERC","MGEE",
    "MGPI","MHO","MIK","MLAB","MLI","MLKN","MLR","MMI","MMSI","MNRO","MNSO",
    "MODV","MPB","MRCY","MRP","MSEX","MTCH","MTDR","MTX","MUR","MVIS","MYGN",
    "MYRG","NABL","NARI","NATL","NAVI","NBHC","NBTB","NCBS","NCMI","NDAQ","NFE",
    "NGVC","NKTR","NMIH","NOG","NOVT","NR","NRIM","NSIT","NSTG","NTCT","NTRA",
    "NUS","NVCR","NVEE","NVRO","NWPX","NXST","NYMT","OAS","OCFC","ODP","OFG",
    "OGS","OI","OII","OIS","OLED","OLN","OMCL","OMI","ONB","OPCH","OPK","ORGO",
    "ORI","OSIS","OSPN","OSUR","OTTR","OUT","OXM","PACB","PAG","PARR","PATK",
    "PBH","PBYI","PCVX","PDCE","PDFS","PENN","PEBO","PFBC","PFS","PGNY","PINC",
    "PK","PLAB","PLMR","PLPC","PLUS","PMT","PNFP","PNNT","POWI","PPBI","PRAA",
    "PRCT","PRDO","PRG","PRIM","PRK","PRLB","PRO","PRTA","PRTH","PRVA","PSMT",
    "PTCT","PTEN","PTGX","PTVE","PUMP","PVH","PWOD","PXLW","PZN","QDEL","QLYS",
    "QMCO","QRTEA","QRTEB","QRVO","RAMP","RBBN","RCKT","RCM","RCUS","RDNT",
    "REZI","RGEN","RGP","RH","RIGL","RILY","RLJ","RMAX","RMR","RNST","ROCK",
    "ROIC","RPAY","RPD","RRBI","RRGB","RUTH","RVLV","RVMD","RWT","RXST","RYAM",
    "RYI","SAFM","SAFT","SAGE","SAH","SAM","SANA","SATS","SBFG","SBH","SBSI",
    "SCSC","SEAS","SELB","SEM","SFBS","SFNC","SGC","SGEN","SGH","SHEN","SHLS",
    "SHOO","SIGI","SIRI","SITC","SJI","SKYW","SLAB","SLGN","SMCI","SMPL","SMTC",
    "SNBR","SNEX","SNV","SOI","SONO","SPFI","SPNT","SPWR","SPXC","SRCE","SRCL",
    "SRI","SRRK","SSB","SSNC","SSTI","STAA","STBA","STEP","STKL","STRA","STRO",
    "STRS","STRT","STXS","SUM","SUPN","SVC","SWBI","SXC","SXI","SYBT","SYNA",
    "SYNH","SYRS","TBBK","TCBI","TCBK","TCMD","TCRX","TDW","TDS","TDW","TECH",
    "TELA","TENB","TEX","TGH","THRM","TILE","TIPT","TNC","TNK","TOL","TPC","TR",
    "TRC","TRDA","TREE","TRIP","TRMB","TRMK","TRN","TROX","TRS","TRST","TSLX",
    "TTMI","TTC","TTEK","TTGT","TTMI","TWI","TXRH","TYL","UA","UAA","UBSI",
    "UFPT","UGI","UHT","ULH","UNFI","UNTY","URBN","USLM","USPH","UTL","UVSP",
    "VBTX","VCEL","VCRA","VECO","VERX","VG","VGR","VHI","VIAV","VICR","VLY",
    "VMI","VNDA","VPG","VRE","VRNT","VRTS","VSAT","VSEC","VSH","VVV","WABC",
    "WAFD","WASH","WERN","WGO","WHG","WINA","WIRE","WNC","WOR","WSFS","WTBA",
    "WTS","WWW","XERS","XFOR","XNCR","XPEL","XPOF","YELP","ZEUS","ZUMZ"
    ]

    # =========================
    # DAX 40
    # =========================
    DAX40 = [
        "ADS.DE","AIR.DE","ALV.DE","BAS.DE","BAYN.DE","BMW.DE","CON.DE","DTE.DE","DBK.DE",
    "SAP.DE","SIE.DE","VOW3.DE","IFX.DE","RWE.DE",
    "HEN3.DE","HEI.DE","MRK.DE","FRE.DE","PUM.DE","SY1.DE","VNA.DE","BEI.DE",
    "1COV.DE","EOAN.DE","MTX.DE","CBK.DE","ZAL.DE","PAH3.DE","BNR.DE""AIXA.DE","AOX.DE","ARL.DE","BOSS.DE","COK.DE","DHL.DE","EVT.DE","FIE.DE",
    "G1A.DE","HAG.DE","HLE.DE","HOT.DE","KRN.DE","LEG.DE","LXS.DE","MTX.DE",
    "NDA.DE","PNE3.DE","RHK.DE","RRTL.DE","SDF.DE","SHA.DE","SGL.DE","SIX2.DE",
    "SZU.DE","TEG.DE","TKA.DE","UTDI.DE","WCH.DE","WUW.DE"
    ]

    all_tickers = list(set(SP500 + NASDAQ100 + RUSSELL + DAX40))

    return all_tickers


# =========================
# UI
# =========================
st.set_page_config(page_title="Bull Flag Scanner", layout="wide")

st.title("🐂 Bull Flag Scanner (Daily)")

if st.button("Scan Market"):

    tickers = get_all_tickers()

    with st.spinner("Scanning stocks..."):
        results = scan_all(tickers)

    if results:
        df = pd.DataFrame(results)
        df = df.sort_values("Score", ascending=False)

        st.success(f"{len(df)} Bull Flags gefunden")

        st.dataframe(df, use_container_width=True)

    else:
        st.warning("Keine Bull Flags gefunden")
