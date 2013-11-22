
def Met(): # TODO: add mitochondrium, add missing reactions and species
	'''
	Model for yeast metabolism by Stanford/Lubitz et al. 2013.
	Adapted for the whole cell model by Katja, Timo, Jens, David and Max S.
	'''
	module_dict = {}

	module_dict['sp_annotations'] = {'s_1005': 'CHEBI:15531',
						 's_1277': 'CHEBI:15361',
						 's_0042': 'CHEBI:49256',
						 's_1000': 'CHEBI:18059',
						 's_1430': 'CHEBI:46398',
						 's_1228': 'CHEBI:49183',
						 's_1160': 'CHEBI:15379',
						 's_0265': 'CHEBI:16001',
						 's_0320': 'CHEBI:15934',
						 's_0325': 'CHEBI:18381',
						 's_0521': 'CHEBI:37563',
						 's_1209_b': 'CHEBI:43474',
						 's_0328': 'CHEBI:18608',
						 's_0010': 'CHEBI:17214',
						 's_0481': 'CHEBI:17239',
						 's_0529': 'CHEBI:16292',
						 's_0079': 'CHEBI:18302',
						 's_0078': 'CHEBI:29112',
						 's_0894': 'CHEBI:17798',
						 's_0400': 'CHEBI:16761',
						 's_1087': 'CHEBI:16908',
						 's_0247': 'CHEBI:52977',
						 's_1082': 'CHEBI:15846',
						 's_1080': 'CHEBI:52961',
						 's_0800': 'CHEBI:30904',
						 's_0873': 'CHEBI:16467',
						 's_0877': 'CHEBI:17196',
						 's_0641': 'CHEBI:52320',
						 's_0463': 'ECO:0000035',
						 's_1073': 'CHEBI:32814',
						 's_1070': 'CHEBI:16878',
						 's_1071': 'CHEBI:44337',
						 's_0001': 'CHEBI:37671',
						 's_0582': 'CHEBI:28493',
						 's_0553': 'CHEBI:35374',
						 's_0046': 'CHEBI:52976',
						 's_0397': 'CHEBI:17985',
						 's_0040': 'CHEBI:15441',
						 's_0319': 'CHEBI:18247',
						 's_0554': 'CHEBI:17369',
						 's_0315': 'CHEBI:27735',
						 's_0316': 'CHEBI:28843',
						 's_0317': 'CHEBI:18406',
						 's_0798': 'CHEBI:36457',
						 's_0410': 'CHEBI:15954',
						 's_0416': 'CHEBI:16551',
						 's_0393': 'CHEBI:16335',
						 's_0167': 'CHEBI:35129',
						 's_0254': 'CHEBI:50571',
						 's_0257': 'CHEBI:15491',
						 's_0007': 'CHEBI:49258',
						 's_0163': 'CHEBI:50606',
						 's_0925': 'CHEBI:15603',
						 's_0659': 'CHEBI:17877',
						 's_0712': 'CHEBI:17211',
						 's_0963': 'CHEBI:16521',
						 's_0128': 'CHEBI:18297',
						 's_0960': 'CHEBI:16414',
						 's_0146': 'CHEBI:52957',
						 's_0650': 'CHEBI:16236',
						 's_0847': 'CHEBI:16087',
						 's_0419': 'CHEBI:18283',
						 's_0657': 'CHEBI:16238',
						 's_0968': 'CHEBI:18262',
						 's_0193': 'CHEBI:17835',
						 's_0828': 'CHEBI:53004',
						 's_0195': 'CHEBI:17407',
						 's_0824': 'CHEBI:53005',
						 's_1293': 'CHEBI:15414',
						 's_1290': 'CHEBI:16680',
						 's_0052': 'CHEBI:27402',
						 's_0309': 'CHEBI:20506',
						 's_1215': 'CHEBI:16337',
						 's_0545': 'CHEBI:17634',
						 's_1455': 'CHEBI:52388',
						 's_0055': 'CHEBI:27466',
						 's_0485': 'CHEBI:17962',
						 's_0303': 'CHEBI:50591',
						 's_0302': 'CHEBI:1949',
						 's_1342': 'CHEBI:15380',
						 's_0058': 'CHEBI:35146',
						 's_0307': 'CHEBI:12071',
						 's_0306': 'CHEBI:15652',
						 's_0987': 'CHEBI:31014',
						 's_0304': 'CHEBI:17709',
						 's_0268': 'CHEBI:17813',
						 's_0710': 'CHEBI:15820',
						 's_0118': 'CHEBI:27391',
						 's_0380': 'CHEBI:15351',
						 's_0386': 'CHEBI:17984',
						 's_0335': 'CHEBI:17601',
						 's_0663': 'CHEBI:35366',
						 's_0261': 'CHEBI:28726',
						 's_1156': 'CHEBI:16452',
						 's_0264': 'CHEBI:17794',
						 's_0669': 'CHEBI:17038',
						 's_0267': 'CHEBI:17052',
						 's_0859': 'CHEBI:18005',
						 's_0911': 'CHEBI:15971',
						 's_0916': 'CHEBI:16996',
						 's_0917': 'CHEBI:17588',
						 's_0915': 'CHEBI:16255',
						 's_1411': 'CHEBI:17659',
						 's_0706': 'CHEBI:17552',
						 's_0850': 'CHEBI:16584',
						 's_0468': 'CHEBI:17516',
						 's_0469': 'CHEBI:17672',
						 's_0181': 'CHEBI:15753',
						 's_0170': 'CHEBI:17275',
						 's_0183': 'CHEBI:16763',
						 's_0511': 'CHEBI:17361',
						 's_0185': 'CHEBI:16810',
						 's_1521': 'CHEBI:15967',
						 's_0431_b': 'CHEBI:28938',
						 's_1219': 'CHEBI:18303',
						 's_0458': 'CHEBI:17544',
						 's_1051': 'CHEBI:16543',
						 's_1052': 'CHEBI:18272',
						 's_1053': 'CHEBI:15919',
						 's_1339_b': 'CHEBI:30031',
						 's_1207': 'CHEBI:43474',
						 's_1283': 'CHEBI:17015',
						 's_1447': 'CHEBI:18252',
						 's_0031': 'CHEBI:36464',
						 's_1117': 'CHEBI:16288',
						 's_0438': 'CHEBI:28102',
						 's_0464_b': 'ECO:0000035',
						 's_0022': 'CHEBI:17436',
						 's_0021': 'CHEBI:15899',
						 's_0374': 'CHEBI:15345',
						 's_0217': 'CHEBI:16630',
						 's_0434': 'CHEBI:16027',
						 's_0331': 'CHEBI:17111',
						 's_0905': 'CHEBI:17232',
						 's_0470': 'CHEBI:16526',
						 's_0907': 'CHEBI:18050',
						 's_1348_b': 'CHEBI:16189',
						 's_1162_b': 'CHEBI:15379',
						 's_0216': 'CHEBI:32364',
						 's_1048': 'CHEBI:18349',
						 's_0919': 'CHEBI:15699',
						 's_1327': 'CHEBI:15440',
						 's_1325': 'CHEBI:16566',
						 's_1060': 'CHEBI:52371',
						 's_0801': 'CHEBI:16240',
						 's_1329': 'CHEBI:25629',
						 's_0805': 'CHEBI:16136',
						 's_1044': 'CHEBI:15532',
						 's_0574': 'CHEBI:27689',
						 's_0569': 'CHEBI:15918',
						 's_1233': 'CHEBI:16038',
						 's_0206': 'CHEBI:17980',
						 's_0886': 'CHEBI:13086',
						 's_0887': 'CHEBI:16349',
						 's_0888': 'CHEBI:17482',
						 's_0889': 'CHEBI:17561',
						 's_1122': 'CHEBI:15961',
						 's_0209': 'CHEBI:36242',
						 's_0566': 'CHEBI:16284',
						 's_0564': 'CHEBI:17713',
						 's_0369': 'CHEBI:30089',
						 's_0533': 'CHEBI:16897',
						 's_1132': 'CHEBI:25646',
						 's_0689': 'CHEBI:15740',
						 's_0212': 'CHEBI:16426',
						 's_0366': 'CHEBI:15343',
						 's_0562': 'CHEBI:16174',
						 's_1243': 'CHEBI:18021',
						 's_0605': 'CHEBI:18361',
						 's_0939': 'CHEBI:17203',
						 's_0446': 'CHEBI:30616',
						 's_0601': 'CHEBI:15633',
						 's_1355': 'CHEBI:52974',
						 's_0180': 'CHEBI:7814',
						 's_0936': 'CHEBI:17295',
						 's_0218': 'CHEBI:17862',
						 's_0933': 'CHEBI:16643',
						 's_1334': 'CHEBI:15541',
						 's_0539': 'CHEBI:15946',
						 's_1338': 'CHEBI:30031',
						 's_0561': 'CHEBI:16332',
						 's_0955': 'CHEBI:17895',
						 's_0952': 'CHEBI:16828',
						 's_0088': 'CHEBI:18299',
						 's_0122': 'CHEBI:15637',
						 's_0120': 'CHEBI:15893',
						 's_0215': 'CHEBI:50593',
						 's_0472_b': 'CHEBI:16526',
						 's_0899': 'CHEBI:29985',
						 's_0124': 'CHEBI:18364',
						 's_0080': 'CHEBI:37522',
						 's_1226': 'CHEBI:15958',
						 's_1225': 'CHEBI:52332',
						 's_0083': 'CHEBI:16975',
						 's_0015': 'CHEBI:15638',
						 's_0755': 'CHEBI:37565',
						 's_0752': 'CHEBI:17345',
						 's_1349': 'CHEBI:17359',
						 's_0008': 'CHEBI:35121',
						 's_0009': 'CHEBI:18319',
						 's_0514': 'CHEBI:15346',
						 's_0766_b': 'CHEBI:24636',
						 's_0356': 'CHEBI:18150',
						 's_1434_b': 'CHEBI:15377',
						 's_0615': 'CHEBI:15809',
						 's_0929': 'CHEBI:18019',
						 's_0616': 'CHEBI:16214',
						 's_0593': 'CHEBI:16192',
						 's_0591': 'CHEBI:28862',
						 's_0455': 'CHEBI:17719',
						 's_0920': 'CHEBI:17191',
						 's_0619': 'CHEBI:17013',
						 's_0532': 'CHEBI:17805',
						 's_0297': 'CHEBI:17865',
						 's_1415': 'CHEBI:18066',
						 's_1140': 'CHEBI:15533',
						 's_1417': 'CHEBI:16695',
						 's_0949': 'CHEBI:16857',
						 's_1456': 'CHEBI:52615',
						 's_0090': 'CHEBI:16749',
						 's_1304': 'CHEBI:15721',
						 's_0149': 'CHEBI:29123',
						 's_1306': 'CHEBI:36208',
						 's_1457': 'CHEBI:52389',
						 's_0943': 'CHEBI:17115',
						 's_0942': 'CHEBI:16927',
						 's_1458': 'CHEBI:52386',
						 's_1258': 'CHEBI:29934',
						 's_1028': 'CHEBI:30807',
						 's_0225': 'CHEBI:11814',
						 's_0301': 'CHEBI:30407',
						 's_0651_b': 'CHEBI:16236',
						 's_0743': 'CHEBI:28087',
						 's_0740': 'CHEBI:15428',
						 's_0150': 'CHEBI:16444',
						 's_0018': 'CHEBI:49072',
						 's_0017': 'CHEBI:15682',
						 's_0749': 'CHEBI:36655',
						 's_0501': 'CHEBI:16383',
						 's_0500': 'CHEBI:29748',
						 's_0158': 'CHEBI:18413',
						 's_1020': 'CHEBI:17268',
						 's_0816': 'CHEBI:17202',
						 's_0622': 'CHEBI:28850',
						 's_0735': 'CHEBI:16108',
						 's_0624': 'CHEBI:17622',
						 's_1517': 'CHEBI:18191',
						 's_0627': 'CHEBI:23929',
						 's_1347': 'CHEBI:16189',
						 's_1066': 'CHEBI:18277',
						 's_0427': 'CHEBI:18189',
						 's_0596': 'CHEBI:18035',
						 's_1151': 'CHEBI:18257',
						 's_1170': 'CHEBI:29889',
						 's_1155': 'CHEBI:15842',
						 's_1154': 'CHEBI:30839',
						 's_0507': 'CHEBI:16947',
						 's_1187': 'CHEBI:15525',
						 's_0318': 'CHEBI:28413',
						 's_1315': 'CHEBI:15978',
						 's_0977': 'CHEBI:15521',
						 's_0333': 'CHEBI:37737',
						 's_0330': 'CHEBI:16257',
						 's_0238': 'CHEBI:11851',
						 's_0334': 'CHEBI:20629',
						 's_0430': 'CHEBI:28938',
						 's_1011': 'CHEBI:28808',
						 's_1399': 'CHEBI:17855',
						 's_1013': 'CHEBI:25168',
						 's_0692': 'CHEBI:29806',
						 's_0234': 'CHEBI:50583',
						 's_0145': 'CHEBI:29114',
						 's_1091': 'CHEBI:18009',
						 's_0069': 'CHEBI:15589',
						 's_1096': 'CHEBI:16474',
						 's_0547_b': 'CHEBI:17634',
						 's_0530': 'CHEBI:17108',
						 's_0549': 'CHEBI:16077',
						 's_0763_b': 'CHEBI:24636',
						 's_0881': 'CHEBI:29991',
						 's_0064': 'CHEBI:30864',
						 's_0537': 'CHEBI:16905',
						 's_0439': 'CHEBI:16567',
						 's_0863': 'CHEBI:16977',
						 's_0734': 'CHEBI:16016',
						 's_0861': 'CHEBI:17082',
						 's_0732': 'CHEBI:17754',
						 's_0867': 'CHEBI:17917',
						 's_0731': 'CHEBI:17138',
						 's_1257': 'CHEBI:16057',
						 's_1379': 'CHEBI:18095',
						 's_0635': 'CHEBI:16933',
						 's_0632': 'CHEBI:18249',
						 's_0557': 'CHEBI:17363'}
	module_dict['name'] = 'Yeast metabolic network'
	module_dict['vars'] = ['s_0001',
						 's_0007',
						 's_0008',
						 's_0009',
						 's_0010',
						 's_0015',
						 's_0017',
						 's_0018',
						 's_0021',
						 's_0022',
						 's_0031',
						 's_0040',
						 's_0042',
						 's_0046',
						 's_0052',
						 's_0055',
						 's_0058',
						 's_0064',
						 's_0069',
						 's_0078',
						 's_0079',
						 's_0080',
						 's_0083',
						 's_0088',
						 's_0090',
						 's_0118',
						 's_0120',
						 's_0122',
						 's_0124',
						 's_0128',
						 's_0145',
						 's_0146',
						 's_0149',
						 's_0150',
						 's_0158',
						 's_0163',
						 's_0167',
						 's_0170',
						 's_0180',
						 's_0181',
						 's_0183',
						 's_0185',
						 's_0193',
						 's_0195',
						 's_0206',
						 's_0209',
						 's_0212',
						 's_0215',
						 's_0216',
						 's_0217',
						 's_0218',
						 's_0225',
						 's_0234',
						 's_0238',
						 's_0247',
						 's_0254',
						 's_0257',
						 's_0261',
						 's_0264',
						 's_0265',
						 's_0267',
						 's_0268',
						 's_0297',
						 's_0301',
						 's_0302',
						 's_0303',
						 's_0304',
						 's_0306',
						 's_0307',
						 's_0309',
						 's_0315',
						 's_0316',
						 's_0317',
						 's_0318',
						 's_0319',
						 's_0320',
						 's_0325',
						 's_0328',
						 's_0330',
						 's_0331',
						 's_0333',
						 's_0334',
						 's_0335',
						 's_0356',
						 's_0366',
						 's_0369',
						 's_0374',
						 's_0380',
						 's_0386',
						 's_0393',
						 's_0397',
						 's_0400',
						 's_0410',
						 's_0416',
						 's_0419',
						 's_0427',
						 's_0430',
						 's_0434',
						 's_0438',
						 's_0439',
						 's_0446',
						 's_0455',
						 's_0458',
						 's_0463',
						 's_0468',
						 's_0469',
						 's_0470',
						 's_0481',
						 's_0485',
						 's_0500',
						 's_0501',
						 's_0507',
						 's_0511',
						 's_0514',
						 's_0521',
						 's_0529',
						 's_0530',
						 's_0532',
						 's_0533',
						 's_0537',
						 's_0539',
						 's_0545',
						 's_0549',
						 's_0553',
						 's_0554',
						 's_0557',
						 's_0561',
						 's_0562',
						 's_0564',
						 's_0566',
						 's_0569',
						 's_0574',
						 's_0582',
						 's_0591',
						 's_0593',
						 's_0596',
						 's_0601',
						 's_0605',
						 's_0615',
						 's_0616',
						 's_0619',
						 's_0622',
						 's_0624',
						 's_0627',
						 's_0632',
						 's_0635',
						 's_0641',
						 's_0650',
						 's_0657',
						 's_0659',
						 's_0663',
						 's_0669',
						 's_0689',
						 's_0692',
						 's_0706',
						 's_0710',
						 's_0712',
						 's_0731',
						 's_0732',
						 's_0734',
						 's_0735',
						 's_0740',
						 's_0743',
						 's_0749',
						 's_0752',
						 's_0755',
						 's_0798',
						 's_0800',
						 's_0801',
						 's_0805',
						 's_0816',
						 's_0824',
						 's_0828',
						 's_0847',
						 's_0850',
						 's_0859',
						 's_0861',
						 's_0863',
						 's_0867',
						 's_0873',
						 's_0877',
						 's_0881',
						 's_0886',
						 's_0887',
						 's_0888',
						 's_0889',
						 's_0894',
						 's_0899',
						 's_0905',
						 's_0907',
						 's_0911',
						 's_0915',
						 's_0916',
						 's_0917',
						 's_0919',
						 's_0920',
						 's_0925',
						 's_0929',
						 's_0933',
						 's_0936',
						 's_0939',
						 's_0942',
						 's_0943',
						 's_0949',
						 's_0952',
						 's_0955',
						 's_0960',
						 's_0963',
						 's_0968',
						 's_0977',
						 's_0987',
						 's_1000',
						 's_1005',
						 's_1011',
						 's_1013',
						 's_1020',
						 's_1028',
						 's_1044',
						 's_1048',
						 's_1051',
						 's_1052',
						 's_1053',
						 's_1060',
						 's_1066',
						 's_1070',
						 's_1071',
						 's_1073',
						 's_1080',
						 's_1082',
						 's_1087',
						 's_1091',
						 's_1096',
						 's_1117',
						 's_1122',
						 's_1132',
						 's_1140',
						 's_1151',
						 's_1154',
						 's_1155',
						 's_1156',
						 's_1160',
						 's_1170',
						 's_1187',
						 's_1207',
						 's_1215',
						 's_1219',
						 's_1225',
						 's_1226',
						 's_1228',
						 's_1233',
						 's_1243',
						 's_1257',
						 's_1258',
						 's_1277',
						 's_1283',
						 's_1290',
						 's_1293',
						 's_1304',
						 's_1306',
						 's_1315',
						 's_1325',
						 's_1327',
						 's_1329',
						 's_1334',
						 's_1338',
						 's_1342',
						 's_1347',
						 's_1349',
						 's_1355',
						 's_1379',
						 's_1399',
						 's_1411',
						 's_1415',
						 's_1417',
						 's_1430',
						 's_1447',
						 's_1455',
						 's_1456',
						 's_1457',
						 's_1458',
						 's_1517',
						 's_1521',
						 's_0763_b',
						 's_1434_b',
						 's_0431_b',
						 's_0464_b',
						 's_0472_b',
						 's_0547_b',
						 's_0651_b',
						 's_0766_b',
						 's_1162_b',
						 's_1209_b',
						 's_1339_b',
						 's_1348_b']
	module_dict['sp_compartment'] = {'s_1005': 'intracellular',
						 's_0430': 'intracellular',
						 's_0899': 'intracellular',
						 's_0554': 'intracellular',
						 's_1000': 'intracellular',
						 's_1122': 'intracellular',
						 's_0124': 'intracellular',
						 's_1160': 'intracellular',
						 's_0669': 'intracellular',
						 's_0320': 'intracellular',
						 's_1277': 'intracellular',
						 's_0325': 'intracellular',
						 's_0521': 'intracellular',
						 's_1226': 'intracellular',
						 's_0328': 'intracellular',
						 's_0464_b': 'extracellular',
						 's_1080': 'intracellular',
						 's_0481': 'intracellular',
						 's_0529': 'intracellular',
						 's_0069': 'intracellular',
						 's_0079': 'intracellular',
						 's_0078': 'intracellular',
						 's_0083': 'intracellular',
						 's_0400': 'intracellular',
						 's_1087': 'intracellular',
						 's_0247': 'intracellular',
						 's_1325': 'intracellular',
						 's_1082': 'intracellular',
						 's_0749': 'intracellular',
						 's_1379': 'intracellular',
						 's_0873': 'intracellular',
						 's_0911': 'intracellular',
						 's_1209_b': 'extracellular',
						 's_0877': 'intracellular',
						 's_0801': 'intracellular',
						 's_0641': 'intracellular',
						 's_1447': 'intracellular',
						 's_0917': 'intracellular',
						 's_1073': 'intracellular',
						 's_1070': 'intracellular',
						 's_1071': 'intracellular',
						 's_0763_b': 'intracellular',
						 's_0755': 'intracellular',
						 's_0627': 'intracellular',
						 's_0553': 'intracellular',
						 's_0046': 'intracellular',
						 's_0410': 'intracellular',
						 's_0040': 'intracellular',
						 's_0319': 'intracellular',
						 's_0042': 'intracellular',
						 's_0315': 'intracellular',
						 's_0316': 'intracellular',
						 's_0317': 'intracellular',
						 's_0798': 'intracellular',
						 's_0397': 'intracellular',
						 's_0416': 'intracellular',
						 's_0393': 'intracellular',
						 's_0167': 'intracellular',
						 's_0254': 'intracellular',
						 's_0257': 'intracellular',
						 's_0163': 'intracellular',
						 's_1456': 'intracellular',
						 's_0659': 'intracellular',
						 's_0712': 'intracellular',
						 's_1434_b': 'intracellular',
						 's_0963': 'intracellular',
						 's_1342': 'intracellular',
						 's_0960': 'intracellular',
						 's_0650': 'intracellular',
						 's_0847': 'intracellular',
						 's_1349': 'intracellular',
						 's_0419': 'intracellular',
						 's_0657': 'intracellular',
						 's_0968': 'intracellular',
						 's_0193': 'intracellular',
						 's_0828': 'intracellular',
						 's_0195': 'intracellular',
						 's_0824': 'intracellular',
						 's_1293': 'intracellular',
						 's_1290': 'intracellular',
						 's_0052': 'intracellular',
						 's_0309': 'intracellular',
						 's_1215': 'intracellular',
						 's_0545': 'intracellular',
						 's_1455': 'intracellular',
						 's_0055': 'intracellular',
						 's_0485': 'intracellular',
						 's_0303': 'intracellular',
						 's_0302': 'intracellular',
						 's_0301': 'intracellular',
						 's_0058': 'intracellular',
						 's_0307': 'intracellular',
						 's_0306': 'intracellular',
						 's_0987': 'intracellular',
						 's_0304': 'intracellular',
						 's_0268': 'intracellular',
						 's_0615': 'intracellular',
						 's_0118': 'intracellular',
						 's_0380': 'intracellular',
						 's_0386': 'intracellular',
						 's_0663': 'intracellular',
						 's_0261': 'intracellular',
						 's_0894': 'intracellular',
						 's_0264': 'intracellular',
						 's_0265': 'intracellular',
						 's_0267': 'intracellular',
						 's_0859': 'intracellular',
						 's_0692': 'intracellular',
						 's_0916': 'intracellular',
						 's_0463': 'intracellular',
						 's_1334': 'intracellular',
						 's_0915': 'intracellular',
						 's_0706': 'intracellular',
						 's_0850': 'intracellular',
						 's_0468': 'intracellular',
						 's_0469': 'intracellular',
						 's_0181': 'intracellular',
						 's_0170': 'intracellular',
						 's_0183': 'intracellular',
						 's_0185': 'intracellular',
						 's_1521': 'intracellular',
						 's_0431_b': 'extracellular',
						 's_0591': 'intracellular',
						 's_1051': 'intracellular',
						 's_1052': 'intracellular',
						 's_1053': 'intracellular',
						 's_1339_b': 'extracellular',
						 's_1207': 'intracellular',
						 's_1283': 'intracellular',
						 's_0574': 'intracellular',
						 's_0369': 'intracellular',
						 's_1117': 'intracellular',
						 's_0889': 'intracellular',
						 's_0455': 'intracellular',
						 's_0863': 'intracellular',
						 's_0022': 'intracellular',
						 's_1228': 'intracellular',
						 's_0021': 'intracellular',
						 's_0374': 'intracellular',
						 's_0632': 'intracellular',
						 's_0238': 'intracellular',
						 's_0905': 'intracellular',
						 's_0470': 'intracellular',
						 's_0907': 'intracellular',
						 's_1348_b': 'extracellular',
						 's_1162_b': 'extracellular',
						 's_1048': 'intracellular',
						 's_1327': 'intracellular',
						 's_1060': 'intracellular',
						 's_0800': 'intracellular',
						 's_0710': 'intracellular',
						 's_1329': 'intracellular',
						 's_1347': 'intracellular',
						 's_0805': 'intracellular',
						 's_1458': 'intracellular',
						 's_1044': 'intracellular',
						 's_0881': 'intracellular',
						 's_0569': 'intracellular',
						 's_1233': 'intracellular',
						 's_0206': 'intracellular',
						 's_0886': 'intracellular',
						 's_0887': 'intracellular',
						 's_0888': 'intracellular',
						 's_0562': 'intracellular',
						 's_0561': 'intracellular',
						 's_0209': 'intracellular',
						 's_0566': 'intracellular',
						 's_0564': 'intracellular',
						 's_0031': 'intracellular',
						 's_0689': 'intracellular',
						 's_1187': 'intracellular',
						 's_0366': 'intracellular',
						 's_0605': 'intracellular',
						 's_0939': 'intracellular',
						 's_0446': 'intracellular',
						 's_0601': 'intracellular',
						 's_1355': 'intracellular',
						 's_0936': 'intracellular',
						 's_0933': 'intracellular',
						 's_0919': 'intracellular',
						 's_1091': 'intracellular',
						 's_1338': 'intracellular',
						 's_0955': 'intracellular',
						 's_0952': 'intracellular',
						 's_0088': 'intracellular',
						 's_0122': 'intracellular',
						 's_0120': 'intracellular',
						 's_0215': 'intracellular',
						 's_0472_b': 'extracellular',
						 's_0217': 'intracellular',
						 's_0216': 'intracellular',
						 's_0080': 'intracellular',
						 's_0218': 'intracellular',
						 's_1225': 'intracellular',
						 's_0128': 'intracellular',
						 's_0001': 'intracellular',
						 's_0752': 'intracellular',
						 's_0007': 'intracellular',
						 's_0008': 'intracellular',
						 's_0009': 'intracellular',
						 's_0514': 'intracellular',
						 's_0766_b': 'extracellular',
						 's_0356': 'intracellular',
						 's_0511': 'intracellular',
						 's_0596': 'intracellular',
						 's_0929': 'intracellular',
						 's_0616': 'intracellular',
						 's_0651_b': 'extracellular',
						 's_0593': 'intracellular',
						 's_0458': 'intracellular',
						 's_0180': 'intracellular',
						 's_0920': 'intracellular',
						 's_0619': 'intracellular',
						 's_0297': 'intracellular',
						 's_1415': 'intracellular',
						 's_1140': 'intracellular',
						 's_1417': 'intracellular',
						 's_0949': 'intracellular',
						 's_1411': 'intracellular',
						 's_0090': 'intracellular',
						 's_1304': 'intracellular',
						 's_1306': 'intracellular',
						 's_1457': 'intracellular',
						 's_0943': 'intracellular',
						 's_0942': 'intracellular',
						 's_0861': 'intracellular',
						 's_0549': 'intracellular',
						 's_1258': 'intracellular',
						 's_1028': 'intracellular',
						 's_0225': 'intracellular',
						 's_1020': 'intracellular',
						 's_1132': 'intracellular',
						 's_0743': 'intracellular',
						 's_0740': 'intracellular',
						 's_0150': 'intracellular',
						 's_0018': 'intracellular',
						 's_0017': 'intracellular',
						 's_0015': 'intracellular',
						 's_1399': 'intracellular',
						 's_0501': 'intracellular',
						 's_0500': 'intracellular',
						 's_0158': 'intracellular',
						 's_0010': 'intracellular',
						 's_0816': 'intracellular',
						 's_0622': 'intracellular',
						 's_0735': 'intracellular',
						 's_0624': 'intracellular',
						 's_1517': 'intracellular',
						 's_0582': 'intracellular',
						 's_1219': 'intracellular',
						 's_1066': 'intracellular',
						 's_0427': 'intracellular',
						 's_0507': 'intracellular',
						 's_1151': 'intracellular',
						 's_1170': 'intracellular',
						 's_1155': 'intracellular',
						 's_1154': 'intracellular',
						 's_0925': 'intracellular',
						 's_1156': 'intracellular',
						 's_1315': 'intracellular',
						 's_0977': 'intracellular',
						 's_1430': 'intracellular',
						 's_0333': 'intracellular',
						 's_0330': 'intracellular',
						 's_0331': 'intracellular',
						 's_0334': 'intracellular',
						 's_0335': 'intracellular',
						 's_1011': 'intracellular',
						 's_1243': 'intracellular',
						 's_1013': 'intracellular',
						 's_0234': 'intracellular',
						 's_0145': 'intracellular',
						 's_0539': 'intracellular',
						 's_0146': 'intracellular',
						 's_1096': 'intracellular',
						 's_0547_b': 'extracellular',
						 's_0530': 'intracellular',
						 's_0532': 'intracellular',
						 's_0533': 'intracellular',
						 's_0149': 'intracellular',
						 's_0064': 'intracellular',
						 's_0537': 'intracellular',
						 's_0439': 'intracellular',
						 's_0438': 'intracellular',
						 's_0734': 'intracellular',
						 's_0212': 'intracellular',
						 's_0732': 'intracellular',
						 's_0867': 'intracellular',
						 's_0731': 'intracellular',
						 's_1257': 'intracellular',
						 's_0318': 'intracellular',
						 's_0635': 'intracellular',
						 's_0434': 'intracellular',
						 's_0557': 'intracellular'}
	module_dict['com_annotations'] = {'intracellular': 'GO:0005622',
						 'extracellular': 'GO:0005576'}
	module_dict['pars'] = ['r_0005__Keq_r_0005',
						 'r_0005__Vmax_r_0005',
						 'r_0005__kmp_s_0001r_0005',
						 'r_0005__kmp_s_0763_br_0005',
						 'r_0005__kmp_s_1411r_0005',
						 'r_0005__kms_s_1415r_0005',
						 'r_0006__Keq_r_0006',
						 'r_0006__Vmax_r_0006',
						 'r_0006__kmp_s_0743r_0006',
						 'r_0006__kmp_s_1434_br_0006',
						 'r_0006__kms_s_0438r_0006',
						 'r_0008__Keq_r_0008',
						 'r_0008__Vmax_r_0008',
						 'r_0008__kmp_s_0315r_0008',
						 'r_0008__kms_s_0079r_0008',
						 'r_0009__Keq_r_0009',
						 'r_0009__Vmax_r_0009',
						 'r_0009__kmp_s_0514r_0009',
						 'r_0009__kmp_s_0763_br_0009',
						 'r_0009__kmp_s_1215r_0009',
						 'r_0009__kms_s_0083r_0009',
						 'r_0009__kms_s_0386r_0009',
						 'r_0014__Keq_r_0014',
						 'r_0014__Vmax_r_0014',
						 'r_0014__kmp_s_0319r_0014',
						 'r_0014__kmp_s_0430r_0014',
						 'r_0014__kms_s_0146r_0014',
						 'r_0014__kms_s_0763_br_0014',
						 'r_0014__kms_s_1434_br_0014',
						 'r_0015__Keq_r_0015',
						 'r_0015__Vmax_r_0015',
						 'r_0015__kmp_s_0146r_0015',
						 'r_0015__kmp_s_1091r_0015',
						 'r_0015__kms_s_0145r_0015',
						 'r_0015__kms_s_0763_br_0015',
						 'r_0015__kms_s_1096r_0015',
						 'r_0016__Keq_r_0016',
						 'r_0016__Vmax_r_0016',
						 'r_0016__kmp_s_0042r_0016',
						 'r_0016__kmp_s_0470r_0016',
						 'r_0016__kms_s_0183r_0016',
						 'r_0016__kms_s_0763_br_0016',
						 'r_0016__kms_s_1277r_0016',
						 'r_0018__Keq_r_0018',
						 'r_0018__Vmax_r_0018',
						 'r_0018__kmp_s_0185r_0018',
						 'r_0018__kmp_s_0861r_0018',
						 'r_0018__kms_s_0181r_0018',
						 'r_0018__kms_s_0899r_0018',
						 'r_0021__Keq_r_0021',
						 'r_0021__Vmax_r_0021',
						 'r_0021__kmp_s_0356r_0021',
						 'r_0021__kmp_s_1207r_0021',
						 'r_0021__kms_s_0533r_0021',
						 'r_0021__kms_s_1243r_0021',
						 'r_0021__kms_s_1434_br_0021',
						 'r_0025__Keq_r_0025',
						 'r_0025__Vmax_r_0025',
						 'r_0025__kmp_s_0170r_0025',
						 'r_0025__kmp_s_1434_br_0025',
						 'r_0025__kms_s_0167r_0025',
						 'r_0026__Keq_r_0026',
						 'r_0026__Vmax_r_0026',
						 'r_0026__kmp_s_0167r_0026',
						 'r_0026__kmp_s_0514r_0026',
						 'r_0026__kmp_s_0763_br_0026',
						 'r_0026__kms_s_0238r_0026',
						 'r_0026__kms_s_0380r_0026',
						 'r_0026__kms_s_1434_br_0026',
						 'r_0029__Keq_r_0029',
						 'r_0029__Vmax_r_0029',
						 'r_0029__kmp_s_0468r_0029',
						 'r_0029__kmp_s_1434_br_0029',
						 'r_0029__kms_s_0798r_0029',
						 'r_0031__Keq_r_0031',
						 'r_0031__Vmax_r_0031',
						 'r_0031__kmp_s_0297r_0031',
						 'r_0031__kmp_s_0470r_0031',
						 'r_0031__kms_s_0010r_0031',
						 'r_0031__kms_s_0763_br_0031',
						 'r_0034__Keq_r_0034',
						 'r_0034__Vmax_r_0034',
						 'r_0034__kmp_s_0434r_0034',
						 'r_0034__kmp_s_1207r_0034',
						 'r_0034__kms_s_0397r_0034',
						 'r_0034__kms_s_1434_br_0034',
						 'r_0040__Keq_r_0040',
						 'r_0040__Vmax_r_0040',
						 'r_0040__kmp_s_0163r_0040',
						 'r_0040__kmp_s_0689r_0040',
						 'r_0040__kmp_s_0763_br_0040',
						 'r_0040__kms_s_0557r_0040',
						 'r_0042__Keq_r_0042',
						 'r_0042__Vmax_r_0042',
						 'r_0042__kmp_s_0217r_0042',
						 'r_0042__kmp_s_1434_br_0042',
						 'r_0042__kms_s_0216r_0042',
						 'r_0043__Keq_r_0043',
						 'r_0043__Vmax_r_0043',
						 'r_0043__kmp_s_0216r_0043',
						 'r_0043__kmp_s_1207r_0043',
						 'r_0043__kms_s_0356r_0043',
						 'r_0044__Keq_r_0044',
						 'r_0044__Vmax_r_0044',
						 'r_0044__kmp_s_1091r_0044',
						 'r_0044__kmp_s_1325r_0044',
						 'r_0044__kms_s_0218r_0044',
						 'r_0044__kms_s_0763_br_0044',
						 'r_0044__kms_s_1096r_0044',
						 'r_0057__Keq_r_0057',
						 'r_0057__Vmax_r_0057',
						 'r_0057__kmp_s_0046r_0057',
						 'r_0057__kmp_s_1082r_0057',
						 'r_0057__kms_s_0247r_0057',
						 'r_0057__kms_s_0763_br_0057',
						 'r_0057__kms_s_1087r_0057',
						 'r_0058__Keq_r_0058',
						 'r_0058__Vmax_r_0058',
						 'r_0058__kmp_s_0052r_0058',
						 'r_0058__kmp_s_1082r_0058',
						 'r_0058__kms_s_0257r_0058',
						 'r_0058__kms_s_0763_br_0058',
						 'r_0058__kms_s_1087r_0058',
						 'r_0059__Keq_r_0059',
						 'r_0059__Vmax_r_0059',
						 'r_0059__kmp_s_0234r_0059',
						 'r_0059__kmp_s_1082r_0059',
						 'r_0059__kms_s_0254r_0059',
						 'r_0059__kms_s_0763_br_0059',
						 'r_0059__kms_s_1087r_0059',
						 'r_0060__Keq_r_0060',
						 'r_0060__Vmax_r_0060',
						 'r_0060__kmp_s_0055r_0060',
						 'r_0060__kmp_s_1082r_0060',
						 'r_0060__kms_s_0261r_0060',
						 'r_0060__kms_s_0763_br_0060',
						 'r_0060__kms_s_1087r_0060',
						 'r_0063__Keq_r_0063',
						 'r_0063__Vmax_r_0063',
						 'r_0063__kmp_s_0008r_0063',
						 'r_0063__kms_s_0170r_0063',
						 'r_0063__kms_s_1434_br_0063',
						 'r_0064__Keq_r_0064',
						 'r_0064__Vmax_r_0064',
						 'r_0064__kmp_s_0010r_0064',
						 'r_0064__kmp_s_0763_br_0064',
						 'r_0064__kmp_s_1087r_0064',
						 'r_0064__kms_s_0008r_0064',
						 'r_0064__kms_s_1082r_0064',
						 'r_0068__Keq_r_0068',
						 'r_0068__Vmax_r_0068',
						 'r_0068__kmp_s_0330r_0068',
						 'r_0068__kmp_s_1207r_0068',
						 'r_0068__kms_s_0267r_0068',
						 'r_0068__kms_s_1243r_0068',
						 'r_0093__Keq_r_0093',
						 'r_0093__Vmax_r_0093',
						 'r_0093__kmp_s_0328r_0093',
						 'r_0093__kmp_s_1091r_0093',
						 'r_0093__kms_s_0307r_0093',
						 'r_0093__kms_s_0763_br_0093',
						 'r_0093__kms_s_1096r_0093',
						 'r_0111__Keq_r_0111',
						 'r_0111__Vmax_r_0111',
						 'r_0111__kmp_s_0018r_0111',
						 'r_0111__kmp_s_1091r_0111',
						 'r_0111__kms_s_0150r_0111',
						 'r_0111__kms_s_0763_br_0111',
						 'r_0111__kms_s_1096r_0111',
						 'r_0112__Keq_r_0112',
						 'r_0112__Vmax_r_0112',
						 'r_0112__kmp_s_0150r_0112',
						 'r_0112__kmp_s_0470r_0112',
						 'r_0112__kms_s_0763_br_0112',
						 'r_0112__kms_s_1277r_0112',
						 'r_0118__Keq_r_0118',
						 'r_0118__Vmax_r_0118',
						 'r_0118__kmp_s_0374r_0118',
						 'r_0118__kmp_s_0514r_0118',
						 'r_0118__kms_s_0380r_0118',
						 'r_0123__Keq_r_0123',
						 'r_0123__Vmax_r_0123',
						 'r_0123__kmp_s_0400r_0123',
						 'r_0123__kmp_s_0763_br_0123',
						 'r_0123__kmp_s_1005r_0123',
						 'r_0123__kmp_s_1207r_0123',
						 'r_0123__kms_s_0380r_0123',
						 'r_0123__kms_s_0446r_0123',
						 'r_0123__kms_s_0458r_0123',
						 'r_0125__Keq_r_0125',
						 'r_0125__Vmax_r_0125',
						 'r_0125__kmp_s_0380r_0125',
						 'r_0125__kmp_s_1434_br_0125',
						 'r_0125__kms_s_0369r_0125',
						 'r_0125__kms_s_0514r_0125',
						 'r_0125__kms_s_0763_br_0125',
						 'r_0127__Keq_r_0127',
						 'r_0127__Vmax_r_0127',
						 'r_0127__kmp_s_0369r_0127',
						 'r_0127__kmp_s_0446r_0127',
						 'r_0127__kmp_s_0514r_0127',
						 'r_0127__kms_s_0380r_0127',
						 'r_0127__kms_s_0434r_0127',
						 'r_0127__kms_s_0605r_0127',
						 'r_0130__Keq_r_0130',
						 'r_0130__Vmax_r_0130',
						 'r_0130__kmp_s_0400r_0130',
						 'r_0130__kmp_s_1070r_0130',
						 'r_0130__kms_s_0446r_0130',
						 'r_0130__kms_s_1071r_0130',
						 'r_0133__Keq_r_0133',
						 'r_0133__Vmax_r_0133',
						 'r_0133__kmp_s_0185r_0133',
						 'r_0133__kmp_s_1051r_0133',
						 'r_0133__kms_s_0149r_0133',
						 'r_0133__kms_s_0899r_0133',
						 'r_0157__Keq_r_0157',
						 'r_0157__Vmax_r_0157',
						 'r_0157__kmp_s_0400r_0157',
						 'r_0157__kmp_s_0434r_0157',
						 'r_0157__kmp_s_0763_br_0157',
						 'r_0157__kms_s_0393r_0157',
						 'r_0157__kms_s_0446r_0157',
						 'r_0159__Keq_r_0159',
						 'r_0159__Vmax_r_0159',
						 'r_0159__kmp_s_0393r_0159',
						 'r_0159__kmp_s_0917r_0159',
						 'r_0159__kms_s_1290r_0159',
						 'r_0159__kms_s_1434_br_0159',
						 'r_0163__Keq_r_0163',
						 'r_0163__Vmax_r_0163',
						 'r_0163__kmp_s_0434r_0163',
						 'r_0163__kmp_s_0446r_0163',
						 'r_0163__kms_s_0400r_0163',
						 'r_0165__Keq_r_0165',
						 'r_0165__Vmax_r_0165',
						 'r_0165__kmp_s_0434r_0165',
						 'r_0165__kmp_s_0755r_0165',
						 'r_0165__kms_s_0400r_0165',
						 'r_0165__kms_s_0706r_0165',
						 'r_0169__Keq_r_0169',
						 'r_0169__Vmax_r_0169',
						 'r_0169__kmp_s_0317r_0169',
						 'r_0169__kmp_s_0692r_0169',
						 'r_0169__kms_s_0009r_0169',
						 'r_0170__Keq_r_0170',
						 'r_0170__Vmax_r_0170',
						 'r_0170__kmp_s_0706r_0170',
						 'r_0170__kmp_s_0763_br_0170',
						 'r_0170__kmp_s_1053r_0170',
						 'r_0170__kmp_s_1207r_0170',
						 'r_0170__kms_s_0755r_0170',
						 'r_0170__kms_s_0816r_0170',
						 'r_0170__kms_s_0881r_0170',
						 'r_0171__Keq_r_0171',
						 'r_0171__Vmax_r_0171',
						 'r_0171__kmp_s_0434r_0171',
						 'r_0171__kmp_s_0692r_0171',
						 'r_0171__kms_s_1053r_0171',
						 'r_0172__Keq_r_0172',
						 'r_0172__Vmax_r_0172',
						 'r_0172__kmp_s_0206r_0172',
						 'r_0172__kmp_s_0400r_0172',
						 'r_0172__kmp_s_0763_br_0172',
						 'r_0172__kms_s_0304r_0172',
						 'r_0172__kms_s_0446r_0172',
						 'r_0174__Keq_r_0174',
						 'r_0174__Vmax_r_0174',
						 'r_0174__kmp_s_0740r_0174',
						 'r_0174__kmp_s_1277r_0174',
						 'r_0174__kms_s_0749r_0174',
						 'r_0174__kms_s_0863r_0174',
						 'r_0183__Keq_r_0183',
						 'r_0183__Vmax_r_0183',
						 'r_0183__kmp_s_0650r_0183',
						 'r_0183__kmp_s_1082r_0183',
						 'r_0183__kms_s_0366r_0183',
						 'r_0183__kms_s_0763_br_0183',
						 'r_0183__kms_s_1087r_0183',
						 'r_0191__Keq_r_0191',
						 'r_0191__Vmax_r_0191',
						 'r_0191__kmp_s_0369r_0191',
						 'r_0191__kmp_s_0763_br_0191',
						 'r_0191__kmp_s_1096r_0191',
						 'r_0191__kms_s_0366r_0191',
						 'r_0191__kms_s_1091r_0191',
						 'r_0191__kms_s_1434_br_0191',
						 'r_0213__Keq_r_0213',
						 'r_0213__Vmax_r_0213',
						 'r_0213__kmp_s_0419r_0213',
						 'r_0213__kmp_s_0763_br_0213',
						 'r_0213__kmp_s_1411r_0213',
						 'r_0213__kms_s_0410r_0213',
						 'r_0213__kms_s_1415r_0213',
						 'r_0220__Keq_r_0220',
						 'r_0220__Vmax_r_0220',
						 'r_0220__kmp_s_0605r_0220',
						 'r_0220__kmp_s_1066r_0220',
						 'r_0220__kms_s_0331r_0220',
						 'r_0220__kms_s_0439r_0220',
						 'r_0221__Keq_r_0221',
						 'r_0221__Vmax_r_0221',
						 'r_0221__kmp_s_0439r_0221',
						 'r_0221__kmp_s_0763_br_0221',
						 'r_0221__kmp_s_0899r_0221',
						 'r_0221__kmp_s_1277r_0221',
						 'r_0221__kms_s_0500r_0221',
						 'r_0221__kms_s_0907r_0221',
						 'r_0225__Keq_r_0225',
						 'r_0225__Vmax_r_0225',
						 'r_0225__kmp_s_0692r_0225',
						 'r_0225__kmp_s_0873r_0225',
						 'r_0225__kms_s_0017r_0225',
						 'r_0226__Keq_r_0226',
						 'r_0226__Vmax_r_0226',
						 'r_0226__kmp_s_0017r_0226',
						 'r_0226__kmp_s_0434r_0226',
						 'r_0226__kmp_s_0605r_0226',
						 'r_0226__kmp_s_0763_br_0226',
						 'r_0226__kms_s_0446r_0226',
						 'r_0226__kms_s_0881r_0226',
						 'r_0226__kms_s_0887r_0226',
						 'r_0229__Keq_r_0229',
						 'r_0229__Vmax_r_0229',
						 'r_0229__kmp_s_0434r_0229',
						 'r_0229__kmp_s_0605r_0229',
						 'r_0229__kmp_s_0763_br_0229',
						 'r_0229__kmp_s_0877r_0229',
						 'r_0229__kmp_s_0899r_0229',
						 'r_0229__kms_s_0446r_0229',
						 'r_0229__kms_s_0881r_0229',
						 'r_0229__kms_s_0907r_0229',
						 'r_0229__kms_s_1434_br_0229',
						 'r_0232__Keq_r_0232',
						 'r_0232__Vmax_r_0232',
						 'r_0232__kmp_s_0763_br_0232',
						 'r_0232__kmp_s_1073r_0232',
						 'r_0232__kmp_s_1207r_0232',
						 'r_0232__kms_s_0469r_0232',
						 'r_0232__kms_s_0881r_0232',
						 'r_0233__Keq_r_0233',
						 'r_0233__Vmax_r_0233',
						 'r_0233__kmp_s_0301r_0233',
						 'r_0233__kmp_s_0400r_0233',
						 'r_0233__kms_s_0446r_0233',
						 'r_0233__kms_s_0881r_0233',
						 'r_0235__Keq_r_0235',
						 'r_0235__Vmax_r_0235',
						 'r_0235__kmp_s_0185r_0235',
						 'r_0235__kmp_s_0881r_0235',
						 'r_0235__kms_s_0899r_0235',
						 'r_0235__kms_s_1156r_0235',
						 'r_0238__Keq_r_0238',
						 'r_0238__Vmax_r_0238',
						 'r_0238__kmp_s_0886r_0238',
						 'r_0238__kmp_s_1091r_0238',
						 'r_0238__kmp_s_1207r_0238',
						 'r_0238__kms_s_0301r_0238',
						 'r_0238__kms_s_0763_br_0238',
						 'r_0238__kms_s_1096r_0238',
						 'r_0245__Keq_r_0245',
						 'r_0245__Vmax_r_0245',
						 'r_0245__kmp_s_0334r_0245',
						 'r_0245__kmp_s_0605r_0245',
						 'r_0245__kms_s_0331r_0245',
						 'r_0245__kms_s_0446r_0245',
						 'r_0246__Keq_r_0246',
						 'r_0246__Vmax_r_0246',
						 'r_0246__kmp_s_0446r_0246',
						 'r_0246__kmp_s_0763_br_0246',
						 'r_0246__kmp_s_1434_br_0246',
						 'r_0246__kms_s_0400r_0246',
						 'r_0246__kms_s_0763_br_0246',
						 'r_0246__kms_s_1207r_0246',
						 'r_0249__Keq_r_0249',
						 'r_0249__Vmax_r_0249',
						 'r_0249__kmp_s_0400r_0249',
						 'r_0249__kmp_s_0766_br_0249',
						 'r_0249__kmp_s_1207r_0249',
						 'r_0249__kms_s_0446r_0249',
						 'r_0249__kms_s_1434_br_0249',
						 'r_0251__Keq_r_0251',
						 'r_0251__Vmax_r_0251',
						 'r_0251__kmp_s_0458r_0251',
						 'r_0251__kmp_s_0763_br_0251',
						 'r_0251__kms_s_0470r_0251',
						 'r_0251__kms_s_1434_br_0251',
						 'r_0258__Keq_r_0258',
						 'r_0258__Vmax_r_0258',
						 'r_0258__kmp_s_0124r_0258',
						 'r_0258__kmp_s_1091r_0258',
						 'r_0258__kms_s_0268r_0258',
						 'r_0258__kms_s_0763_br_0258',
						 'r_0258__kms_s_1096r_0258',
						 'r_0261__Keq_r_0261',
						 'r_0261__Vmax_r_0261',
						 'r_0261__kmp_s_0470r_0261',
						 'r_0261__kmp_s_0763_br_0261',
						 'r_0261__kmp_s_1096r_0261',
						 'r_0261__kmp_s_1458r_0261',
						 'r_0261__kms_s_1091r_0261',
						 'r_0261__kms_s_1457r_0261',
						 'r_0262__Keq_r_0262',
						 'r_0262__Vmax_r_0262',
						 'r_0262__kmp_s_0215r_0262',
						 'r_0262__kmp_s_0470r_0262',
						 'r_0262__kmp_s_0763_br_0262',
						 'r_0262__kmp_s_1087r_0262',
						 'r_0262__kms_s_0303r_0262',
						 'r_0262__kms_s_1082r_0262',
						 'r_0263__Keq_r_0263',
						 'r_0263__Vmax_r_0263',
						 'r_0263__kmp_s_0302r_0263',
						 'r_0263__kmp_s_1091r_0263',
						 'r_0263__kms_s_0215r_0263',
						 'r_0263__kms_s_0763_br_0263',
						 'r_0263__kms_s_1096r_0263',
						 'r_0264__Keq_r_0264',
						 'r_0264__Vmax_r_0264',
						 'r_0264__kmp_s_1091r_0264',
						 'r_0264__kmp_s_1447r_0264',
						 'r_0264__kms_s_0763_br_0264',
						 'r_0264__kms_s_1096r_0264',
						 'r_0264__kms_s_1458r_0264',
						 'r_0265__Keq_r_0265',
						 'r_0265__Vmax_r_0265',
						 'r_0265__kmp_s_1091r_0265',
						 'r_0265__kmp_s_1434_br_0265',
						 'r_0265__kmp_s_1455r_0265',
						 'r_0265__kms_s_0302r_0265',
						 'r_0265__kms_s_0763_br_0265',
						 'r_0265__kms_s_1096r_0265',
						 'r_0265__kms_s_1160r_0265',
						 'r_0266__Keq_r_0266',
						 'r_0266__Vmax_r_0266',
						 'r_0266__kmp_s_1091r_0266',
						 'r_0266__kmp_s_1434_br_0266',
						 'r_0266__kmp_s_1456r_0266',
						 'r_0266__kms_s_0763_br_0266',
						 'r_0266__kms_s_1096r_0266',
						 'r_0266__kms_s_1160r_0266',
						 'r_0266__kms_s_1455r_0266',
						 'r_0267__Keq_r_0267',
						 'r_0267__Vmax_r_0267',
						 'r_0267__kmp_s_1091r_0267',
						 'r_0267__kmp_s_1434_br_0267',
						 'r_0267__kmp_s_1457r_0267',
						 'r_0267__kms_s_0763_br_0267',
						 'r_0267__kms_s_1096r_0267',
						 'r_0267__kms_s_1160r_0267',
						 'r_0267__kms_s_1456r_0267',
						 'r_0268__Keq_r_0268',
						 'r_0268__Vmax_r_0268',
						 'r_0268__kmp_s_0303r_0268',
						 'r_0268__kmp_s_1091r_0268',
						 'r_0268__kmp_s_1434_br_0268',
						 'r_0268__kms_s_0124r_0268',
						 'r_0268__kms_s_0763_br_0268',
						 'r_0268__kms_s_1096r_0268',
						 'r_0268__kms_s_1160r_0268',
						 'r_0270__Keq_r_0270',
						 'r_0270__Vmax_r_0270',
						 'r_0270__kmp_s_0627r_0270',
						 'r_0270__kms_s_0669r_0270',
						 'r_0271__Keq_r_0271',
						 'r_0271__Vmax_r_0271',
						 'r_0271__kmp_s_0635r_0271',
						 'r_0271__kmp_s_1091r_0271',
						 'r_0271__kms_s_0632r_0271',
						 'r_0271__kms_s_0763_br_0271',
						 'r_0271__kms_s_1096r_0271',
						 'r_0277__Keq_r_0277',
						 'r_0277__Vmax_r_0277',
						 'r_0277__kmp_s_0400r_0277',
						 'r_0277__kmp_s_0469r_0277',
						 'r_0277__kmp_s_0763_br_0277',
						 'r_0277__kmp_s_0899r_0277',
						 'r_0277__kmp_s_1207r_0277',
						 'r_0277__kms_s_0446r_0277',
						 'r_0277__kms_s_0458r_0277',
						 'r_0277__kms_s_0907r_0277',
						 'r_0277__kms_s_1434_br_0277',
						 'r_0282__Keq_r_0282',
						 'r_0282__Vmax_r_0282',
						 'r_0282__kmp_s_1160r_0282',
						 'r_0282__kmp_s_1434_br_0282',
						 'r_0282__kms_s_0801r_0282',
						 'r_0284__Keq_r_0284',
						 'r_0284__Vmax_r_0284',
						 'r_0284__kmp_s_0485r_0284',
						 'r_0284__kmp_s_0605r_0284',
						 'r_0284__kms_s_0521r_0284',
						 'r_0284__kms_s_0763_br_0284',
						 'r_0284__kms_s_1215r_0284',
						 'r_0287__Keq_r_0287',
						 'r_0287__Vmax_r_0287',
						 'r_0287__kmp_s_1060r_0287',
						 'r_0287__kmp_s_1091r_0287',
						 'r_0287__kmp_s_1434_br_0287',
						 'r_0287__kms_s_0763_br_0287',
						 'r_0287__kms_s_1080r_0287',
						 'r_0287__kms_s_1096r_0287',
						 'r_0287__kms_s_1160r_0287',
						 'r_0290__Keq_r_0290',
						 'r_0290__Vmax_r_0290',
						 'r_0290__kmp_s_0514r_0290',
						 'r_0290__kmp_s_0763_br_0290',
						 'r_0290__kmp_s_1080r_0290',
						 'r_0290__kms_s_1325r_0290',
						 'r_0290__kms_s_1355r_0290',
						 'r_0298__Keq_r_0298',
						 'r_0298__Vmax_r_0298',
						 'r_0298__kmp_s_0632r_0298',
						 'r_0298__kmp_s_0763_br_0298',
						 'r_0298__kmp_s_1290r_0298',
						 'r_0298__kmp_s_1434_br_0298',
						 'r_0298__kms_s_1160r_0298',
						 'r_0298__kms_s_1293r_0298',
						 'r_0298__kms_s_1447r_0298',
						 'r_0304__Keq_r_0304',
						 'r_0304__Vmax_r_0304',
						 'r_0304__kmp_s_1258r_0304',
						 'r_0304__kms_s_0500r_0304',
						 'r_0306__Keq_r_0306',
						 'r_0306__Vmax_r_0306',
						 'r_0306__kmp_s_0500r_0306',
						 'r_0306__kmp_s_1207r_0306',
						 'r_0306__kms_s_0330r_0306',
						 'r_0307__Keq_r_0307',
						 'r_0307__Vmax_r_0307',
						 'r_0307__kmp_s_0847r_0307',
						 'r_0307__kms_s_0501r_0307',
						 'r_0307__kms_s_1434_br_0307',
						 'r_0328__Keq_r_0328',
						 'r_0328__Vmax_r_0328',
						 'r_0328__kmp_s_0507r_0328',
						 'r_0328__kmp_s_0514r_0328',
						 'r_0328__kmp_s_0763_br_0328',
						 'r_0328__kms_s_0380r_0328',
						 'r_0328__kms_s_1156r_0328',
						 'r_0328__kms_s_1434_br_0328',
						 'r_0330__Keq_r_0330',
						 'r_0330__Vmax_r_0330',
						 'r_0330__kmp_s_0501r_0330',
						 'r_0330__kmp_s_1434_br_0330',
						 'r_0330__kms_s_0507r_0330',
						 'r_0336__Keq_r_0336',
						 'r_0336__Vmax_r_0336',
						 'r_0336__kmp_s_0400r_0336',
						 'r_0336__kmp_s_0521r_0336',
						 'r_0336__kmp_s_0763_br_0336',
						 'r_0336__kmp_s_1207r_0336',
						 'r_0336__kms_s_0430r_0336',
						 'r_0336__kms_s_0446r_0336',
						 'r_0336__kms_s_1430r_0336',
						 'r_0338__Keq_r_0338',
						 'r_0338__Vmax_r_0338',
						 'r_0338__kmp_s_0888r_0338',
						 'r_0338__kmp_s_1434_br_0338',
						 'r_0338__kms_s_0917r_0338',
						 'r_0338__kms_s_0943r_0338',
						 'r_0339__Keq_r_0339',
						 'r_0339__Vmax_r_0339',
						 'r_0339__kmp_s_0183r_0339',
						 'r_0339__kmp_s_0430r_0339',
						 'r_0339__kmp_s_0889r_0339',
						 'r_0339__kms_s_0888r_0339',
						 'r_0339__kms_s_1434_br_0339',
						 'r_0340__Keq_r_0340',
						 'r_0340__Vmax_r_0340',
						 'r_0340__kmp_s_0369r_0340',
						 'r_0340__kmp_s_0763_br_0340',
						 'r_0340__kmp_s_0888r_0340',
						 'r_0340__kms_s_0889r_0340',
						 'r_0340__kms_s_1117r_0340',
						 'r_0345__Keq_r_0345',
						 'r_0345__Vmax_r_0345',
						 'r_0345__kmp_s_0446r_0345',
						 'r_0345__kmp_s_0511r_0345',
						 'r_0345__kms_s_0400r_0345',
						 'r_0345__kms_s_0481r_0345',
						 'r_0347__Keq_r_0347',
						 'r_0347__Vmax_r_0347',
						 'r_0347__kmp_s_0268r_0347',
						 'r_0347__kmp_s_0689r_0347',
						 'r_0347__kmp_s_1082r_0347',
						 'r_0347__kmp_s_1434_br_0347',
						 'r_0347__kms_s_0763_br_0347',
						 'r_0347__kms_s_0963r_0347',
						 'r_0347__kms_s_1087r_0347',
						 'r_0347__kms_s_1160r_0347',
						 'r_0351__Keq_r_0351',
						 'r_0351__Vmax_r_0351',
						 'r_0351__kmp_s_0530r_0351',
						 'r_0351__kmp_s_1082r_0351',
						 'r_0351__kms_s_0529r_0351',
						 'r_0351__kms_s_0763_br_0351',
						 'r_0351__kms_s_1087r_0351',
						 'r_0352__Keq_r_0352',
						 'r_0352__Vmax_r_0352',
						 'r_0352__kmp_s_0529r_0352',
						 'r_0352__kmp_s_0763_br_0352',
						 'r_0352__kmp_s_1096r_0352',
						 'r_0352__kms_s_0530r_0352',
						 'r_0352__kms_s_1091r_0352',
						 'r_0357__Keq_r_0357',
						 'r_0357__Vmax_r_0357',
						 'r_0357__kmp_s_0569r_0357',
						 'r_0357__kmp_s_0763_br_0357',
						 'r_0357__kmp_s_1434_br_0357',
						 'r_0357__kms_s_0430r_0357',
						 'r_0357__kms_s_0624r_0357',
						 'r_0360__Keq_r_0360',
						 'r_0360__Vmax_r_0360',
						 'r_0360__kmp_s_0446r_0360',
						 'r_0360__kmp_s_0564r_0360',
						 'r_0360__kms_s_0400r_0360',
						 'r_0360__kms_s_0562r_0360',
						 'r_0362__Keq_r_0362',
						 'r_0362__Vmax_r_0362',
						 'r_0362__kmp_s_0446r_0362',
						 'r_0362__kmp_s_0593r_0362',
						 'r_0362__kms_s_0400r_0362',
						 'r_0362__kms_s_0591r_0362',
						 'r_0370__Keq_r_0370',
						 'r_0370__Vmax_r_0370',
						 'r_0370__kmp_s_0514r_0370',
						 'r_0370__kmp_s_0763_br_0370',
						 'r_0370__kmp_s_1399r_0370',
						 'r_0370__kms_s_0386r_0370',
						 'r_0370__kms_s_0596r_0370',
						 'r_0371__Keq_r_0371',
						 'r_0371__Vmax_r_0371',
						 'r_0371__kmp_s_0596r_0371',
						 'r_0371__kmp_s_0763_br_0371',
						 'r_0371__kmp_s_1207r_0371',
						 'r_0371__kms_s_1215r_0371',
						 'r_0371__kms_s_1434_br_0371',
						 'r_0374__Keq_r_0374',
						 'r_0374__Vmax_r_0374',
						 'r_0374__kmp_s_0801r_0374',
						 'r_0374__kmp_s_1154r_0374',
						 'r_0374__kms_s_0064r_0374',
						 'r_0374__kms_s_1160r_0374',
						 'r_0375__Keq_r_0375',
						 'r_0375__Vmax_r_0375',
						 'r_0375__kmp_s_0309r_0375',
						 'r_0375__kmp_s_1091r_0375',
						 'r_0375__kms_s_0601r_0375',
						 'r_0375__kms_s_0763_br_0375',
						 'r_0375__kms_s_1096r_0375',
						 'r_0381__Keq_r_0381',
						 'r_0381__Vmax_r_0381',
						 'r_0381__kmp_s_0064r_0381',
						 'r_0381__kmp_s_1434_br_0381',
						 'r_0381__kms_s_0763_br_0381',
						 'r_0381__kms_s_1073r_0381',
						 'r_0384__Keq_r_0384',
						 'r_0384__Vmax_r_0384',
						 'r_0384__kmp_s_0238r_0384',
						 'r_0384__kmp_s_1434_br_0384',
						 'r_0384__kms_s_0018r_0384',
						 'r_0385__Keq_r_0385',
						 'r_0385__Vmax_r_0385',
						 'r_0385__kmp_s_0058r_0385',
						 'r_0385__kmp_s_1434_br_0385',
						 'r_0385__kms_s_0007r_0385',
						 'r_0386__Keq_r_0386',
						 'r_0386__Vmax_r_0386',
						 'r_0386__kmp_s_0400r_0386',
						 'r_0386__kmp_s_0735r_0386',
						 'r_0386__kmp_s_0763_br_0386',
						 'r_0386__kms_s_0446r_0386',
						 'r_0386__kms_s_0734r_0386',
						 'r_0387__Keq_r_0387',
						 'r_0387__Vmax_r_0387',
						 'r_0387__kmp_s_0605r_0387',
						 'r_0387__kmp_s_0712r_0387',
						 'r_0387__kms_s_0850r_0387',
						 'r_0387__kms_s_1257r_0387',
						 'r_0393__Keq_r_0393',
						 'r_0393__Vmax_r_0393',
						 'r_0393__kmp_s_0615r_0393',
						 'r_0393__kmp_s_0706r_0393',
						 'r_0393__kms_s_0616r_0393',
						 'r_0393__kms_s_0710r_0393',
						 'r_0394__Keq_r_0394',
						 'r_0394__Vmax_r_0394',
						 'r_0394__kmp_s_0616r_0394',
						 'r_0394__kmp_s_0763_br_0394',
						 'r_0394__kmp_s_1011r_0394',
						 'r_0394__kms_s_0615r_0394',
						 'r_0398__Keq_r_0398',
						 'r_0398__Vmax_r_0398',
						 'r_0398__kmp_s_1243r_0398',
						 'r_0398__kmp_s_1434_br_0398',
						 'r_0398__kms_s_0193r_0398',
						 'r_0417__Keq_r_0417',
						 'r_0417__Vmax_r_0417',
						 'r_0417__kmp_s_0470r_0417',
						 'r_0417__kmp_s_0514r_0417',
						 'r_0417__kmp_s_0574r_0417',
						 'r_0417__kmp_s_1091r_0417',
						 'r_0417__kmp_s_1434_br_0417',
						 'r_0417__kms_s_0763_br_0417',
						 'r_0417__kms_s_1005r_0417',
						 'r_0417__kms_s_1096r_0417',
						 'r_0417__kms_s_1132r_0417',
						 'r_0418__Keq_r_0418',
						 'r_0418__Vmax_r_0418',
						 'r_0418__kmp_s_0470r_0418',
						 'r_0418__kmp_s_0514r_0418',
						 'r_0418__kmp_s_0968r_0418',
						 'r_0418__kmp_s_1091r_0418',
						 'r_0418__kmp_s_1434_br_0418',
						 'r_0418__kms_s_0574r_0418',
						 'r_0418__kms_s_0763_br_0418',
						 'r_0418__kms_s_1005r_0418',
						 'r_0418__kms_s_1096r_0418',
						 'r_0419__Keq_r_0419',
						 'r_0419__Vmax_r_0419',
						 'r_0419__kmp_s_0470r_0419',
						 'r_0419__kmp_s_0514r_0419',
						 'r_0419__kmp_s_1028r_0419',
						 'r_0419__kmp_s_1091r_0419',
						 'r_0419__kmp_s_1434_br_0419',
						 'r_0419__kms_s_0763_br_0419',
						 'r_0419__kms_s_0968r_0419',
						 'r_0419__kms_s_1005r_0419',
						 'r_0419__kms_s_1096r_0419',
						 'r_0421__Keq_r_0421',
						 'r_0421__Vmax_r_0421',
						 'r_0421__kmp_s_0470r_0421',
						 'r_0421__kmp_s_0514r_0421',
						 'r_0421__kmp_s_1091r_0421',
						 'r_0421__kmp_s_1170r_0421',
						 'r_0421__kmp_s_1434_br_0421',
						 'r_0421__kms_s_0763_br_0421',
						 'r_0421__kms_s_1005r_0421',
						 'r_0421__kms_s_1028r_0421',
						 'r_0421__kms_s_1096r_0421',
						 'r_0423__Keq_r_0423',
						 'r_0423__Vmax_r_0423',
						 'r_0423__kmp_s_0470r_0423',
						 'r_0423__kmp_s_0514r_0423',
						 'r_0423__kmp_s_1091r_0423',
						 'r_0423__kmp_s_1329r_0423',
						 'r_0423__kmp_s_1434_br_0423',
						 'r_0423__kms_s_0763_br_0423',
						 'r_0423__kms_s_1005r_0423',
						 'r_0423__kms_s_1096r_0423',
						 'r_0423__kms_s_1170r_0423',
						 'r_0425__Keq_r_0425',
						 'r_0425__Vmax_r_0425',
						 'r_0425__kmp_s_0470r_0425',
						 'r_0425__kmp_s_0514r_0425',
						 'r_0425__kmp_s_0987r_0425',
						 'r_0425__kmp_s_1091r_0425',
						 'r_0425__kmp_s_1434_br_0425',
						 'r_0425__kms_s_0763_br_0425',
						 'r_0425__kms_s_1005r_0425',
						 'r_0425__kms_s_1096r_0425',
						 'r_0425__kms_s_1329r_0425',
						 'r_0429__Keq_r_0429',
						 'r_0429__Vmax_r_0429',
						 'r_0429__kmp_s_0470r_0429',
						 'r_0429__kmp_s_0514r_0429',
						 'r_0429__kmp_s_0582r_0429',
						 'r_0429__kmp_s_1091r_0429',
						 'r_0429__kmp_s_1434_br_0429',
						 'r_0429__kms_s_0763_br_0429',
						 'r_0429__kms_s_1005r_0429',
						 'r_0429__kms_s_1096r_0429',
						 'r_0429__kms_s_1140r_0429',
						 'r_0430__Keq_r_0430',
						 'r_0430__Vmax_r_0430',
						 'r_0430__kmp_s_0470r_0430',
						 'r_0430__kmp_s_0514r_0430',
						 'r_0430__kmp_s_1091r_0430',
						 'r_0430__kmp_s_1140r_0430',
						 'r_0430__kmp_s_1434_br_0430',
						 'r_0430__kms_s_0380r_0430',
						 'r_0430__kms_s_0763_br_0430',
						 'r_0430__kms_s_1005r_0430',
						 'r_0430__kms_s_1096r_0430',
						 'r_0437__Keq_r_0437',
						 'r_0437__Vmax_r_0437',
						 'r_0437__kmp_s_0434r_0437',
						 'r_0437__kmp_s_0605r_0437',
						 'r_0437__kmp_s_1355r_0437',
						 'r_0437__kms_s_0446r_0437',
						 'r_0437__kms_s_0514r_0437',
						 'r_0437__kms_s_0987r_0437',
						 'r_0439__Keq_r_0439',
						 'r_0439__Vmax_r_0439',
						 'r_0439__kmp_s_0446r_0439',
						 'r_0439__kmp_s_0514r_0439',
						 'r_0439__kmp_s_1329r_0439',
						 'r_0439__kms_s_0434r_0439',
						 'r_0439__kms_s_0605r_0439',
						 'r_0439__kms_s_1334r_0439',
						 'r_0442__Keq_r_0442',
						 'r_0442__Vmax_r_0442',
						 'r_0442__kmp_s_0446r_0442',
						 'r_0442__kmp_s_0514r_0442',
						 'r_0442__kmp_s_1132r_0442',
						 'r_0442__kms_s_0434r_0442',
						 'r_0442__kms_s_0605r_0442',
						 'r_0442__kms_s_1140r_0442',
						 'r_0464__Keq_r_0464',
						 'r_0464__Vmax_r_0464',
						 'r_0464__kmp_s_0470r_0464',
						 'r_0464__kmp_s_0514r_0464',
						 'r_0464__kmp_s_0977r_0464',
						 'r_0464__kmp_s_1091r_0464',
						 'r_0464__kmp_s_1434_br_0464',
						 'r_0464__kms_s_0582r_0464',
						 'r_0464__kms_s_0763_br_0464',
						 'r_0464__kms_s_1005r_0464',
						 'r_0464__kms_s_1096r_0464',
						 'r_0465__Keq_r_0465',
						 'r_0465__Vmax_r_0465',
						 'r_0465__kmp_s_0470r_0465',
						 'r_0465__kmp_s_0514r_0465',
						 'r_0465__kmp_s_1044r_0465',
						 'r_0465__kmp_s_1091r_0465',
						 'r_0465__kmp_s_1434_br_0465',
						 'r_0465__kms_s_0763_br_0465',
						 'r_0465__kms_s_0977r_0465',
						 'r_0465__kms_s_1005r_0465',
						 'r_0465__kms_s_1096r_0465',
						 'r_0466__Keq_r_0466',
						 'r_0466__Vmax_r_0466',
						 'r_0466__kmp_s_0470r_0466',
						 'r_0466__kmp_s_0514r_0466',
						 'r_0466__kmp_s_1091r_0466',
						 'r_0466__kmp_s_1187r_0466',
						 'r_0466__kmp_s_1434_br_0466',
						 'r_0466__kms_s_0763_br_0466',
						 'r_0466__kms_s_1005r_0466',
						 'r_0466__kms_s_1044r_0466',
						 'r_0466__kms_s_1096r_0466',
						 'r_0467__Keq_r_0467',
						 'r_0467__Vmax_r_0467',
						 'r_0467__kmp_s_0470r_0467',
						 'r_0467__kmp_s_0514r_0467',
						 'r_0467__kmp_s_1091r_0467',
						 'r_0467__kmp_s_1334r_0467',
						 'r_0467__kmp_s_1434_br_0467',
						 'r_0467__kms_s_0763_br_0467',
						 'r_0467__kms_s_1005r_0467',
						 'r_0467__kms_s_1096r_0467',
						 'r_0467__kms_s_1187r_0467',
						 'r_0479__Keq_r_0479',
						 'r_0479__Vmax_r_0479',
						 'r_0479__kmp_s_0122r_0479',
						 'r_0479__kmp_s_0400r_0479',
						 'r_0479__kmp_s_1207r_0479',
						 'r_0479__kms_s_0309r_0479',
						 'r_0479__kms_s_0446r_0479',
						 'r_0479__kms_s_0689r_0479',
						 'r_0484__Keq_r_0484',
						 'r_0484__Vmax_r_0484',
						 'r_0484__kmp_s_0731r_0484',
						 'r_0484__kmp_s_0735r_0484',
						 'r_0484__kms_s_0537r_0484',
						 'r_0485__Keq_r_0485',
						 'r_0485__Vmax_r_0485',
						 'r_0485__kmp_s_0692r_0485',
						 'r_0485__kmp_s_1434_br_0485',
						 'r_0485__kms_s_0069r_0485',
						 'r_0488__Keq_r_0488',
						 'r_0488__Vmax_r_0488',
						 'r_0488__kmp_s_0657r_0488',
						 'r_0488__kmp_s_1338r_0488',
						 'r_0488__kms_s_0659r_0488',
						 'r_0488__kms_s_0692r_0488',
						 'r_0496__Keq_r_0496',
						 'r_0496__Vmax_r_0496',
						 'r_0496__kmp_s_0195r_0496',
						 'r_0496__kmp_s_0605r_0496',
						 'r_0496__kms_s_0712r_0496',
						 'r_0496__kms_s_0850r_0496',
						 'r_0499__Keq_r_0499',
						 'r_0499__Vmax_r_0499',
						 'r_0499__kmp_s_0400r_0499',
						 'r_0499__kmp_s_0455r_0499',
						 'r_0499__kmp_s_0763_br_0499',
						 'r_0499__kms_s_0446r_0499',
						 'r_0499__kms_s_0545r_0499',
						 'r_0504__Keq_r_0504',
						 'r_0504__Vmax_r_0504',
						 'r_0504__kmp_s_0539r_0504',
						 'r_0504__kms_s_0455r_0504',
						 'r_0505__Keq_r_0505',
						 'r_0505__Vmax_r_0505',
						 'r_0505__kmp_s_0539r_0505',
						 'r_0505__kms_s_0410r_0505',
						 'r_0506__Keq_r_0506',
						 'r_0506__Vmax_r_0506',
						 'r_0506__kmp_s_0400r_0506',
						 'r_0506__kmp_s_0894r_0506',
						 'r_0506__kms_s_0446r_0506',
						 'r_0506__kms_s_0899r_0506',
						 'r_0509__Keq_r_0509',
						 'r_0509__Vmax_r_0509',
						 'r_0509__kmp_s_0899r_0509',
						 'r_0509__kmp_s_1091r_0509',
						 'r_0509__kmp_s_1434_br_0509',
						 'r_0509__kms_s_0185r_0509',
						 'r_0509__kms_s_0430r_0509',
						 'r_0509__kms_s_0763_br_0509',
						 'r_0509__kms_s_1096r_0509',
						 'r_0510__Keq_r_0510',
						 'r_0510__Vmax_r_0510',
						 'r_0510__kmp_s_0899r_0510',
						 'r_0510__kmp_s_1082r_0510',
						 'r_0510__kms_s_0185r_0510',
						 'r_0510__kms_s_0763_br_0510',
						 'r_0510__kms_s_0907r_0510',
						 'r_0510__kms_s_1087r_0510',
						 'r_0512__Keq_r_0512',
						 'r_0512__Vmax_r_0512',
						 'r_0512__kmp_s_0905r_0512',
						 'r_0512__kmp_s_1082r_0512',
						 'r_0512__kmp_s_1207r_0512',
						 'r_0512__kms_s_0763_br_0512',
						 'r_0512__kms_s_0894r_0512',
						 'r_0512__kms_s_1087r_0512',
						 'r_0514__Keq_r_0514',
						 'r_0514__Vmax_r_0514',
						 'r_0514__kmp_s_0333r_0514',
						 'r_0514__kmp_s_0605r_0514',
						 'r_0514__kmp_s_0899r_0514',
						 'r_0514__kms_s_0331r_0514',
						 'r_0514__kms_s_0907r_0514',
						 'r_0514__kms_s_1434_br_0514',
						 'r_0515__Keq_r_0515',
						 'r_0515__Vmax_r_0515',
						 'r_0515__kmp_s_0400r_0515',
						 'r_0515__kmp_s_0763_br_0515',
						 'r_0515__kmp_s_0907r_0515',
						 'r_0515__kmp_s_1207r_0515',
						 'r_0515__kms_s_0430r_0515',
						 'r_0515__kms_s_0446r_0515',
						 'r_0515__kms_s_0899r_0515',
						 'r_0525__Keq_r_0525',
						 'r_0525__Vmax_r_0525',
						 'r_0525__kmp_s_0265r_0525',
						 'r_0525__kmp_s_0763_br_0525',
						 'r_0525__kmp_s_1087r_0525',
						 'r_0525__kms_s_0731r_0525',
						 'r_0525__kms_s_1082r_0525',
						 'r_0525__kms_s_1207r_0525',
						 'r_0526__Keq_r_0526',
						 'r_0526__Vmax_r_0526',
						 'r_0526__kmp_s_0734r_0526',
						 'r_0526__kmp_s_0763_br_0526',
						 'r_0526__kmp_s_1096r_0526',
						 'r_0526__kms_s_0732r_0526',
						 'r_0526__kms_s_1091r_0526',
						 'r_0528__Keq_r_0528',
						 'r_0528__Vmax_r_0528',
						 'r_0528__kmp_s_0732r_0528',
						 'r_0528__kmp_s_1207r_0528',
						 'r_0528__kms_s_1315r_0528',
						 'r_0528__kms_s_1434_br_0528',
						 'r_0529__Keq_r_0529',
						 'r_0529__Vmax_r_0529',
						 'r_0529__kmp_s_0659r_0529',
						 'r_0529__kmp_s_0735r_0529',
						 'r_0529__kms_s_0657r_0529',
						 'r_0529__kms_s_1315r_0529',
						 'r_0530__Keq_r_0530',
						 'r_0530__Vmax_r_0530',
						 'r_0530__kmp_s_1082r_0530',
						 'r_0530__kmp_s_1315r_0530',
						 'r_0530__kms_s_0735r_0530',
						 'r_0530__kms_s_0763_br_0530',
						 'r_0530__kms_s_1087r_0530',
						 'r_0534__Keq_r_0534',
						 'r_0534__Vmax_r_0534',
						 'r_0534__kmp_s_0083r_0534',
						 'r_0534__kmp_s_0514r_0534',
						 'r_0534__kmp_s_0763_br_0534',
						 'r_0534__kms_s_0386r_0534',
						 'r_0534__kms_s_1315r_0534',
						 'r_0538__Keq_r_0538',
						 'r_0538__Vmax_r_0538',
						 'r_0538__kmp_s_0307r_0538',
						 'r_0538__kmp_s_0430r_0538',
						 'r_0538__kmp_s_0470r_0538',
						 'r_0538__kmp_s_1087r_0538',
						 'r_0538__kms_s_0309r_0538',
						 'r_0538__kms_s_0740r_0538',
						 'r_0538__kms_s_1082r_0538',
						 'r_0539__Keq_r_0539',
						 'r_0539__Vmax_r_0539',
						 'r_0539__kmp_s_0309r_0539',
						 'r_0539__kmp_s_0943r_0539',
						 'r_0539__kms_s_0307r_0539',
						 'r_0539__kms_s_0740r_0539',
						 'r_0539__kms_s_1434_br_0539',
						 'r_0547__Keq_r_0547',
						 'r_0547__Vmax_r_0547',
						 'r_0547__kmp_s_0438r_0547',
						 'r_0547__kmp_s_0763_br_0547',
						 'r_0547__kmp_s_1411r_0547',
						 'r_0547__kms_s_1415r_0547',
						 'r_0547__kms_s_1434_br_0547',
						 'r_0551__Keq_r_0551',
						 'r_0551__Vmax_r_0551',
						 'r_0551__kmp_s_0434r_0551',
						 'r_0551__kmp_s_0605r_0551',
						 'r_0551__kmp_s_0752r_0551',
						 'r_0551__kmp_s_0763_br_0551',
						 'r_0551__kmp_s_0899r_0551',
						 'r_0551__kms_s_0306r_0551',
						 'r_0551__kms_s_0446r_0551',
						 'r_0551__kms_s_0907r_0551',
						 'r_0551__kms_s_1434_br_0551',
						 'r_0562__Keq_r_0562',
						 'r_0562__Vmax_r_0562',
						 'r_0562__kmp_s_0145r_0562',
						 'r_0562__kmp_s_0605r_0562',
						 'r_0562__kmp_s_0689r_0562',
						 'r_0562__kmp_s_0763_br_0562',
						 'r_0562__kms_s_0755r_0562',
						 'r_0562__kms_s_1434_br_0562',
						 'r_0567__Keq_r_0567',
						 'r_0567__Vmax_r_0567',
						 'r_0567__kmp_s_0400r_0567',
						 'r_0567__kmp_s_0706r_0567',
						 'r_0567__kms_s_0446r_0567',
						 'r_0567__kms_s_0752r_0567',
						 'r_0568__Keq_r_0568',
						 'r_0568__Vmax_r_0568',
						 'r_0568__kmp_s_0562r_0568',
						 'r_0568__kmp_s_0706r_0568',
						 'r_0568__kms_s_0566r_0568',
						 'r_0568__kms_s_0752r_0568',
						 'r_0573__Keq_r_0573',
						 'r_0573__Vmax_r_0573',
						 'r_0573__kmp_s_0400r_0573',
						 'r_0573__kmp_s_0410r_0573',
						 'r_0573__kmp_s_0763_br_0573',
						 'r_0573__kms_s_0446r_0573',
						 'r_0573__kms_s_0545r_0573',
						 'r_0575__Keq_r_0575',
						 'r_0575__Vmax_r_0575',
						 'r_0575__kmp_s_0763_br_0575',
						 'r_0575__kmp_s_0911r_0575',
						 'r_0575__kmp_s_1087r_0575',
						 'r_0575__kms_s_0915r_0575',
						 'r_0575__kms_s_1082r_0575',
						 'r_0575__kms_s_1434_br_0575',
						 'r_0576__Keq_r_0576',
						 'r_0576__Vmax_r_0576',
						 'r_0576__kmp_s_0915r_0576',
						 'r_0576__kmp_s_1207r_0576',
						 'r_0576__kms_s_0916r_0576',
						 'r_0576__kms_s_1434_br_0576',
						 'r_0577__Keq_r_0577',
						 'r_0577__Vmax_r_0577',
						 'r_0577__kmp_s_0185r_0577',
						 'r_0577__kmp_s_0916r_0577',
						 'r_0577__kms_s_0212r_0577',
						 'r_0577__kms_s_0899r_0577',
						 'r_0581__Keq_r_0581',
						 'r_0581__Vmax_r_0581',
						 'r_0581__kmp_s_0800r_0581',
						 'r_0581__kms_s_0468r_0581',
						 'r_0581__kms_s_1434_br_0581',
						 'r_0582__Keq_r_0582',
						 'r_0582__Vmax_r_0582',
						 'r_0582__kmp_s_0514r_0582',
						 'r_0582__kmp_s_0763_br_0582',
						 'r_0582__kmp_s_0798r_0582',
						 'r_0582__kms_s_0185r_0582',
						 'r_0582__kms_s_0380r_0582',
						 'r_0582__kms_s_1434_br_0582',
						 'r_0585__Keq_r_0585',
						 'r_0585__Vmax_r_0585',
						 'r_0585__kmp_s_0180r_0585',
						 'r_0585__kmp_s_0763_br_0585',
						 'r_0585__kmp_s_1087r_0585',
						 'r_0585__kms_s_0800r_0585',
						 'r_0585__kms_s_1082r_0585',
						 'r_0586__Keq_r_0586',
						 'r_0586__Vmax_r_0586',
						 'r_0586__kmp_s_0919r_0586',
						 'r_0586__kmp_s_1082r_0586',
						 'r_0586__kms_s_0763_br_0586',
						 'r_0586__kms_s_0886r_0586',
						 'r_0586__kms_s_1087r_0586',
						 'r_0588__Keq_r_0588',
						 'r_0588__Vmax_r_0588',
						 'r_0588__kmp_s_0400r_0588',
						 'r_0588__kmp_s_0763_br_0588',
						 'r_0588__kmp_s_1122r_0588',
						 'r_0588__kms_s_0446r_0588',
						 'r_0588__kms_s_0919r_0588',
						 'r_0589__Keq_r_0589',
						 'r_0589__Vmax_r_0589',
						 'r_0589__kmp_s_0514r_0589',
						 'r_0589__kmp_s_1117r_0589',
						 'r_0589__kms_s_0380r_0589',
						 'r_0589__kms_s_0919r_0589',
						 'r_0598__Keq_r_0598',
						 'r_0598__Vmax_r_0598',
						 'r_0598__kmp_s_0031r_0598',
						 'r_0598__kmp_s_0514r_0598',
						 'r_0598__kmp_s_1091r_0598',
						 'r_0598__kms_s_0225r_0598',
						 'r_0598__kms_s_0763_br_0598',
						 'r_0598__kms_s_1096r_0598',
						 'r_0599__Keq_r_0599',
						 'r_0599__Vmax_r_0599',
						 'r_0599__kmp_s_0225r_0599',
						 'r_0599__kmp_s_0514r_0599',
						 'r_0599__kmp_s_0763_br_0599',
						 'r_0599__kms_s_0374r_0599',
						 'r_0599__kms_s_0380r_0599',
						 'r_0599__kms_s_1434_br_0599',
						 'r_0604__Keq_r_0604',
						 'r_0604__Vmax_r_0604',
						 'r_0604__kmp_s_0317r_0604',
						 'r_0604__kmp_s_0532r_0604',
						 'r_0604__kmp_s_0763_br_0604',
						 'r_0604__kmp_s_0899r_0604',
						 'r_0604__kms_s_0315r_0604',
						 'r_0604__kms_s_0907r_0604',
						 'r_0605__Keq_r_0605',
						 'r_0605__Vmax_r_0605',
						 'r_0605__kmp_s_0212r_0605',
						 'r_0605__kmp_s_1434_br_0605',
						 'r_0605__kms_s_0532r_0605',
						 'r_0606__Keq_r_0606',
						 'r_0606__Vmax_r_0606',
						 'r_0606__kmp_s_0816r_0606',
						 'r_0606__kmp_s_1434_br_0606',
						 'r_0606__kms_s_0325r_0606',
						 'r_0607__Keq_r_0607',
						 'r_0607__Vmax_r_0607',
						 'r_0607__kmp_s_0306r_0607',
						 'r_0607__kmp_s_0763_br_0607',
						 'r_0607__kmp_s_1087r_0607',
						 'r_0607__kms_s_0816r_0607',
						 'r_0607__kms_s_1082r_0607',
						 'r_0607__kms_s_1434_br_0607',
						 'r_0608__Keq_r_0608',
						 'r_0608__Vmax_r_0608',
						 'r_0608__kmp_s_0088r_0608',
						 'r_0608__kmp_s_0470r_0608',
						 'r_0608__kmp_s_1434_br_0608',
						 'r_0608__kms_s_0078r_0608',
						 'r_0608__kms_s_0763_br_0608',
						 'r_0610__Keq_r_0610',
						 'r_0610__Vmax_r_0610',
						 'r_0610__kmp_s_0763_br_0610',
						 'r_0610__kmp_s_1207r_0610',
						 'r_0610__kms_s_0605r_0610',
						 'r_0610__kms_s_1434_br_0610',
						 'r_0618__Keq_r_0618',
						 'r_0618__Vmax_r_0618',
						 'r_0618__kmp_s_0824r_0618',
						 'r_0618__kms_s_0128r_0618',
						 'r_0618__kms_s_1013r_0618',
						 'r_0621__Keq_r_0621',
						 'r_0621__Vmax_r_0621',
						 'r_0621__kmp_s_0828r_0621',
						 'r_0621__kms_s_0128r_0621',
						 'r_0621__kms_s_1060r_0621',
						 'r_0630__Keq_r_0630',
						 'r_0630__Vmax_r_0630',
						 'r_0630__kmp_s_0185r_0630',
						 'r_0630__kmp_s_0470r_0630',
						 'r_0630__kmp_s_1096r_0630',
						 'r_0630__kms_s_0847r_0630',
						 'r_0630__kms_s_1091r_0630',
						 'r_0633__Keq_r_0633',
						 'r_0633__Vmax_r_0633',
						 'r_0633__kmp_s_0749r_0633',
						 'r_0633__kmp_s_1338r_0633',
						 'r_0633__kms_s_0847r_0633',
						 'r_0634__Keq_r_0634',
						 'r_0634__Vmax_r_0634',
						 'r_0634__kmp_s_0185r_0634',
						 'r_0634__kmp_s_0920r_0634',
						 'r_0634__kms_s_0058r_0634',
						 'r_0634__kms_s_0899r_0634',
						 'r_0638__Keq_r_0638',
						 'r_0638__Vmax_r_0638',
						 'r_0638__kmp_s_1257r_0638',
						 'r_0638__kms_s_0850r_0638',
						 'r_0640__Keq_r_0640',
						 'r_0640__Vmax_r_0640',
						 'r_0640__kmp_s_0007r_0640',
						 'r_0640__kmp_s_1091r_0640',
						 'r_0640__kms_s_0042r_0640',
						 'r_0640__kms_s_0763_br_0640',
						 'r_0640__kms_s_1096r_0640',
						 'r_0647__Keq_r_0647',
						 'r_0647__Vmax_r_0647',
						 'r_0647__kmp_s_0185r_0647',
						 'r_0647__kmp_s_0863r_0647',
						 'r_0647__kms_s_0899r_0647',
						 'r_0647__kms_s_1277r_0647',
						 'r_0650__Keq_r_0650',
						 'r_0650__Vmax_r_0650',
						 'r_0650__kmp_s_0434r_0650',
						 'r_0650__kmp_s_0605r_0650',
						 'r_0650__kmp_s_0867r_0650',
						 'r_0650__kmp_s_1082r_0650',
						 'r_0650__kms_s_0446r_0650',
						 'r_0650__kms_s_0763_br_0650',
						 'r_0650__kms_s_0861r_0650',
						 'r_0650__kms_s_1087r_0650',
						 'r_0657__Keq_r_0657',
						 'r_0657__Vmax_r_0657',
						 'r_0657__kmp_s_0120r_0657',
						 'r_0657__kmp_s_0763_br_0657',
						 'r_0657__kmp_s_1434_br_0657',
						 'r_0657__kms_s_0905r_0657',
						 'r_0660__Keq_r_0660',
						 'r_0660__Vmax_r_0660',
						 'r_0660__kmp_s_0118r_0660',
						 'r_0660__kmp_s_0763_br_0660',
						 'r_0660__kmp_s_1096r_0660',
						 'r_0660__kms_s_1091r_0660',
						 'r_0660__kms_s_1379r_0660',
						 'r_0661__Keq_r_0661',
						 'r_0661__Vmax_r_0661',
						 'r_0661__kmp_s_1082r_0661',
						 'r_0661__kmp_s_1379r_0661',
						 'r_0661__kms_s_0118r_0661',
						 'r_0661__kms_s_0763_br_0661',
						 'r_0661__kms_s_1087r_0661',
						 'r_0667__Keq_r_0667',
						 'r_0667__Vmax_r_0667',
						 'r_0667__kmp_s_0183r_0667',
						 'r_0667__kmp_s_0430r_0667',
						 'r_0667__kms_s_0949r_0667',
						 'r_0673__Keq_r_0673',
						 'r_0673__Vmax_r_0673',
						 'r_0673__kmp_s_0963r_0673',
						 'r_0673__kms_s_0040r_0673',
						 'r_0674__Keq_r_0674',
						 'r_0674__Vmax_r_0674',
						 'r_0674__kmp_s_0185r_0674',
						 'r_0674__kmp_s_0925r_0674',
						 'r_0674__kms_s_0297r_0674',
						 'r_0674__kms_s_0899r_0674',
						 'r_0688__Keq_r_0688',
						 'r_0688__Vmax_r_0688',
						 'r_0688__kmp_s_0069r_0688',
						 'r_0688__kmp_s_1082r_0688',
						 'r_0688__kms_s_0763_br_0688',
						 'r_0688__kms_s_1087r_0688',
						 'r_0688__kms_s_1156r_0688',
						 'r_0697__Keq_r_0697',
						 'r_0697__Vmax_r_0697',
						 'r_0697__kmp_s_0605r_0697',
						 'r_0697__kmp_s_0710r_0697',
						 'r_0697__kms_s_0553r_0697',
						 'r_0697__kms_s_0755r_0697',
						 'r_0697__kms_s_0763_br_0697',
						 'r_0698__Keq_r_0698',
						 'r_0698__Vmax_r_0698',
						 'r_0698__kmp_s_0554r_0698',
						 'r_0698__kms_s_0539r_0698',
						 'r_0699__Keq_r_0699',
						 'r_0699__Vmax_r_0699',
						 'r_0699__kmp_s_0122r_0699',
						 'r_0699__kmp_s_0763_br_0699',
						 'r_0699__kms_s_0015r_0699',
						 'r_0699__kms_s_1434_br_0699',
						 'r_0701__Keq_r_0701',
						 'r_0701__Vmax_r_0701',
						 'r_0701__kmp_s_0605r_0701',
						 'r_0701__kmp_s_1207r_0701',
						 'r_0701__kmp_s_1293r_0701',
						 'r_0701__kms_s_0446r_0701',
						 'r_0701__kms_s_0933r_0701',
						 'r_0701__kms_s_1434_br_0701',
						 'r_0702__Keq_r_0702',
						 'r_0702__Vmax_r_0702',
						 'r_0702__kmp_s_0309r_0702',
						 'r_0702__kmp_s_0763_br_0702',
						 'r_0702__kmp_s_0933r_0702',
						 'r_0702__kms_s_0328r_0702',
						 'r_0702__kms_s_0917r_0702',
						 'r_0707__Keq_r_0707',
						 'r_0707__Vmax_r_0707',
						 'r_0707__kmp_s_0015r_0707',
						 'r_0707__kmp_s_1096r_0707',
						 'r_0707__kms_s_0307r_0707',
						 'r_0707__kms_s_1091r_0707',
						 'r_0712__Keq_r_0712',
						 'r_0712__Vmax_r_0712',
						 'r_0712__kmp_s_0022r_0712',
						 'r_0712__kmp_s_0481r_0712',
						 'r_0712__kmp_s_0763_br_0712',
						 'r_0712__kms_s_0031r_0712',
						 'r_0712__kms_s_0521r_0712',
						 'r_0715__Keq_r_0715',
						 'r_0715__Vmax_r_0715',
						 'r_0715__kmp_s_0400r_0715',
						 'r_0715__kmp_s_0470r_0715',
						 'r_0715__kmp_s_0850r_0715',
						 'r_0715__kmp_s_1207r_0715',
						 'r_0715__kms_s_0021r_0715',
						 'r_0715__kms_s_0446r_0715',
						 'r_0719__Keq_r_0719',
						 'r_0719__Vmax_r_0719',
						 'r_0719__kmp_s_0247r_0719',
						 'r_0719__kmp_s_0763_br_0719',
						 'r_0719__kmp_s_1096r_0719',
						 'r_0719__kms_s_0046r_0719',
						 'r_0719__kms_s_1091r_0719',
						 'r_0720__Keq_r_0720',
						 'r_0720__Vmax_r_0720',
						 'r_0720__kmp_s_0257r_0720',
						 'r_0720__kmp_s_0763_br_0720',
						 'r_0720__kmp_s_1096r_0720',
						 'r_0720__kms_s_0052r_0720',
						 'r_0720__kms_s_1091r_0720',
						 'r_0721__Keq_r_0721',
						 'r_0721__Vmax_r_0721',
						 'r_0721__kmp_s_0254r_0721',
						 'r_0721__kmp_s_0763_br_0721',
						 'r_0721__kmp_s_1096r_0721',
						 'r_0721__kms_s_0234r_0721',
						 'r_0721__kms_s_1091r_0721',
						 'r_0722__Keq_r_0722',
						 'r_0722__Vmax_r_0722',
						 'r_0722__kmp_s_0261r_0722',
						 'r_0722__kmp_s_0763_br_0722',
						 'r_0722__kmp_s_1096r_0722',
						 'r_0722__kms_s_0055r_0722',
						 'r_0722__kms_s_1091r_0722',
						 'r_0723__Keq_r_0723',
						 'r_0723__Vmax_r_0723',
						 'r_0723__kmp_s_1013r_0723',
						 'r_0723__kms_s_0710r_0723',
						 'r_0723__kms_s_0828r_0723',
						 'r_0725__Keq_r_0725',
						 'r_0725__Vmax_r_0725',
						 'r_0725__kmp_s_1020r_0725',
						 'r_0725__kmp_s_1207r_0725',
						 'r_0725__kms_s_0128r_0725',
						 'r_0725__kms_s_1434_br_0725',
						 'r_0726__Keq_r_0726',
						 'r_0726__Vmax_r_0726',
						 'r_0726__kmp_s_0128r_0726',
						 'r_0726__kms_s_0410r_0726',
						 'r_0728__Keq_r_0728',
						 'r_0728__Vmax_r_0728',
						 'r_0728__kmp_s_0149r_0728',
						 'r_0728__kmp_s_1091r_0728',
						 'r_0728__kmp_s_1207r_0728',
						 'r_0728__kms_s_0763_br_0728',
						 'r_0728__kms_s_1070r_0728',
						 'r_0728__kms_s_1096r_0728',
						 'r_0765__Keq_r_0765',
						 'r_0765__Vmax_r_0765',
						 'r_0765__kmp_s_0181r_0765',
						 'r_0765__kmp_s_0470r_0765',
						 'r_0765__kms_s_0180r_0765',
						 'r_0765__kms_s_0763_br_0765',
						 'r_0771__Keq_r_0771',
						 'r_0771__Vmax_r_0771',
						 'r_0771__kmp_s_0446r_0771',
						 'r_0771__kmp_s_0481r_0771',
						 'r_0771__kms_s_0400r_0771',
						 'r_0771__kms_s_0521r_0771',
						 'r_0779__Keq_r_0779',
						 'r_0779__Vmax_r_0779',
						 'r_0779__kmp_s_0400r_0779',
						 'r_0779__kmp_s_1430r_0779',
						 'r_0779__kms_s_0446r_0779',
						 'r_0779__kms_s_1411r_0779',
						 'r_0783__Keq_r_0783',
						 'r_0783__Vmax_r_0783',
						 'r_0783__kmp_s_0369r_0783',
						 'r_0783__kmp_s_0763_br_0783',
						 'r_0783__kmp_s_0917r_0783',
						 'r_0783__kms_s_0805r_0783',
						 'r_0783__kms_s_1117r_0783',
						 'r_0789__Keq_r_0789',
						 'r_0789__Vmax_r_0789',
						 'r_0789__kmp_s_0763_br_0789',
						 'r_0789__kmp_s_0887r_0789',
						 'r_0789__kmp_s_1207r_0789',
						 'r_0789__kms_s_0469r_0789',
						 'r_0789__kms_s_1151r_0789',
						 'r_0791__Keq_r_0791',
						 'r_0791__Vmax_r_0791',
						 'r_0791__kmp_s_1071r_0791',
						 'r_0791__kmp_s_1151r_0791',
						 'r_0791__kms_s_0899r_0791',
						 'r_0791__kms_s_1051r_0791',
						 'r_0793__Keq_r_0793',
						 'r_0793__Vmax_r_0793',
						 'r_0793__kmp_s_0605r_0793',
						 'r_0793__kmp_s_1155r_0793',
						 'r_0793__kms_s_0331r_0793',
						 'r_0793__kms_s_1154r_0793',
						 'r_0794__Keq_r_0794',
						 'r_0794__Vmax_r_0794',
						 'r_0794__kmp_s_0470r_0794',
						 'r_0794__kmp_s_1417r_0794',
						 'r_0794__kms_s_0763_br_0794',
						 'r_0794__kms_s_1155r_0794',
						 'r_0825__Keq_r_0825',
						 'r_0825__Vmax_r_0825',
						 'r_0825__kmp_s_0185r_0825',
						 'r_0825__kmp_s_0936r_0825',
						 'r_0825__kms_s_0859r_0825',
						 'r_0825__kms_s_0899r_0825',
						 'r_0831__Keq_r_0831',
						 'r_0831__Vmax_r_0831',
						 'r_0831__kmp_s_0763_br_0831',
						 'r_0831__kmp_s_1226r_0831',
						 'r_0831__kmp_s_1290r_0831',
						 'r_0831__kms_s_1233r_0831',
						 'r_0831__kms_s_1293r_0831',
						 'r_0847__Keq_r_0847',
						 'r_0847__Vmax_r_0847',
						 'r_0847__kmp_s_0090r_0847',
						 'r_0847__kmp_s_0511r_0847',
						 'r_0847__kmp_s_0763_br_0847',
						 'r_0847__kms_s_0485r_0847',
						 'r_0847__kms_s_1020r_0847',
						 'r_0850__Keq_r_0850',
						 'r_0850__Vmax_r_0850',
						 'r_0850__kmp_s_0470r_0850',
						 'r_0850__kmp_s_1233r_0850',
						 'r_0850__kms_s_1219r_0850',
						 'r_0853__Keq_r_0853',
						 'r_0853__Vmax_r_0853',
						 'r_0853__kmp_s_0511r_0853',
						 'r_0853__kmp_s_0763_br_0853',
						 'r_0853__kmp_s_1219r_0853',
						 'r_0853__kms_s_0485r_0853',
						 'r_0853__kms_s_0943r_0853',
						 'r_0856__Keq_r_0856',
						 'r_0856__Vmax_r_0856',
						 'r_0856__kmp_s_0397r_0856',
						 'r_0856__kmp_s_0763_br_0856',
						 'r_0856__kmp_s_1349r_0856',
						 'r_0856__kmp_s_1517r_0856',
						 'r_0856__kms_s_0206r_0856',
						 'r_0856__kms_s_1521r_0856',
						 'r_0859__Keq_r_0859',
						 'r_0859__Vmax_r_0859',
						 'r_0859__kmp_s_0400r_0859',
						 'r_0859__kmp_s_0537r_0859',
						 'r_0859__kmp_s_0763_br_0859',
						 'r_0859__kms_s_0446r_0859',
						 'r_0859__kms_s_0539r_0859',
						 'r_0861__Keq_r_0861',
						 'r_0861__Vmax_r_0861',
						 'r_0861__kmp_s_0549r_0861',
						 'r_0861__kms_s_0410r_0861',
						 'r_0865__Keq_r_0865',
						 'r_0865__Vmax_r_0865',
						 'r_0865__kmp_s_0264r_0865',
						 'r_0865__kmp_s_0446r_0865',
						 'r_0865__kms_s_0265r_0865',
						 'r_0865__kms_s_0400r_0865',
						 'r_0866__Keq_r_0866',
						 'r_0866__Vmax_r_0866',
						 'r_0866__kmp_s_0193r_0866',
						 'r_0866__kms_s_0264r_0866',
						 'r_0873__Keq_r_0873',
						 'r_0873__Vmax_r_0873',
						 'r_0873__kmp_s_1228r_0873',
						 'r_0873__kmp_s_1290r_0873',
						 'r_0873__kms_s_1225r_0873',
						 'r_0873__kms_s_1293r_0873',
						 'r_0874__Keq_r_0874',
						 'r_0874__Vmax_r_0874',
						 'r_0874__kmp_s_0763_br_0874',
						 'r_0874__kmp_s_1225r_0874',
						 'r_0874__kmp_s_1290r_0874',
						 'r_0874__kms_s_1226r_0874',
						 'r_0874__kms_s_1293r_0874',
						 'r_0875__Keq_r_0875',
						 'r_0875__Vmax_r_0875',
						 'r_0875__kmp_s_0553r_0875',
						 'r_0875__kms_s_0554r_0875',
						 'r_0877__Keq_r_0877',
						 'r_0877__Vmax_r_0877',
						 'r_0877__kmp_s_0021r_0877',
						 'r_0877__kmp_s_0400r_0877',
						 'r_0877__kms_s_0022r_0877',
						 'r_0877__kms_s_0446r_0877',
						 'r_0881__Keq_r_0881',
						 'r_0881__Vmax_r_0881',
						 'r_0881__kmp_s_0079r_0881',
						 'r_0881__kms_s_0080r_0881',
						 'r_0881__kms_s_1434_br_0881',
						 'r_0882__Keq_r_0882',
						 'r_0882__Vmax_r_0882',
						 'r_0882__kmp_s_0080r_0882',
						 'r_0882__kmp_s_0605r_0882',
						 'r_0882__kmp_s_0763_br_0882',
						 'r_0882__kms_s_0334r_0882',
						 'r_0882__kms_s_1434_br_0882',
						 'r_0883__Keq_r_0883',
						 'r_0883__Vmax_r_0883',
						 'r_0883__kmp_s_0318r_0883',
						 'r_0883__kmp_s_0763_br_0883',
						 'r_0883__kms_s_0316r_0883',
						 'r_0883__kms_s_0470r_0883',
						 'r_0884__Keq_r_0884',
						 'r_0884__Vmax_r_0884',
						 'r_0884__kmp_s_0316r_0884',
						 'r_0884__kmp_s_0400r_0884',
						 'r_0884__kmp_s_0763_br_0884',
						 'r_0884__kmp_s_1207r_0884',
						 'r_0884__kms_s_0158r_0884',
						 'r_0884__kms_s_0446r_0884',
						 'r_0885__Keq_r_0885',
						 'r_0885__Vmax_r_0885',
						 'r_0885__kmp_s_0309r_0885',
						 'r_0885__kmp_s_0325r_0885',
						 'r_0885__kms_s_0122r_0885',
						 'r_0885__kms_s_0317r_0885',
						 'r_0886__Keq_r_0886',
						 'r_0886__Vmax_r_0886',
						 'r_0886__kmp_s_0009r_0886',
						 'r_0886__kmp_s_0400r_0886',
						 'r_0886__kmp_s_0763_br_0886',
						 'r_0886__kmp_s_1207r_0886',
						 'r_0886__kms_s_0318r_0886',
						 'r_0886__kms_s_0446r_0886',
						 'r_0886__kms_s_0881r_0886',
						 'r_0887__Keq_r_0887',
						 'r_0887__Vmax_r_0887',
						 'r_0887__kmp_s_0078r_0887',
						 'r_0887__kms_s_1066r_0887',
						 'r_0888__Keq_r_0888',
						 'r_0888__Vmax_r_0888',
						 'r_0888__kmp_s_0158r_0888',
						 'r_0888__kmp_s_0400r_0888',
						 'r_0888__kmp_s_0763_br_0888',
						 'r_0888__kmp_s_0899r_0888',
						 'r_0888__kmp_s_1207r_0888',
						 'r_0888__kms_s_0446r_0888',
						 'r_0888__kms_s_0907r_0888',
						 'r_0888__kms_s_1052r_0888',
						 'r_0888__kms_s_1434_br_0888',
						 'r_0889__Keq_r_0889',
						 'r_0889__Vmax_r_0889',
						 'r_0889__kmp_s_0309r_0889',
						 'r_0889__kmp_s_0763_br_0889',
						 'r_0889__kmp_s_1052r_0889',
						 'r_0889__kms_s_0122r_0889',
						 'r_0889__kms_s_1048r_0889',
						 'r_0890__Keq_r_0890',
						 'r_0890__Vmax_r_0890',
						 'r_0890__kmp_s_0400r_0890',
						 'r_0890__kmp_s_0763_br_0890',
						 'r_0890__kmp_s_1048r_0890',
						 'r_0890__kmp_s_1207r_0890',
						 'r_0890__kms_s_0333r_0890',
						 'r_0890__kms_s_0446r_0890',
						 'r_0890__kms_s_0740r_0890',
						 'r_0891__Keq_r_0891',
						 'r_0891__Vmax_r_0891',
						 'r_0891__kmp_s_0331r_0891',
						 'r_0891__kmp_s_0434r_0891',
						 'r_0891__kmp_s_0763_br_0891',
						 'r_0891__kms_s_0427r_0891',
						 'r_0891__kms_s_0446r_0891',
						 'r_0911__Keq_r_0911',
						 'r_0911__Vmax_r_0911',
						 'r_0911__kmp_s_0470r_0911',
						 'r_0911__kmp_s_0859r_0911',
						 'r_0911__kmp_s_1434_br_0911',
						 'r_0911__kms_s_0763_br_0911',
						 'r_0911__kms_s_1258r_0911',
						 'r_0913__Keq_r_0913',
						 'r_0913__Vmax_r_0913',
						 'r_0913__kmp_s_0209r_0913',
						 'r_0913__kmp_s_0470r_0913',
						 'r_0913__kmp_s_1096r_0913',
						 'r_0913__kms_s_1091r_0913',
						 'r_0913__kms_s_1258r_0913',
						 'r_0934__Keq_r_0934',
						 'r_0934__Vmax_r_0934',
						 'r_0934__kmp_s_0320r_0934',
						 'r_0934__kmp_s_1207r_0934',
						 'r_0934__kms_s_0319r_0934',
						 'r_0934__kms_s_1434_br_0934',
						 'r_0936__Keq_r_0936',
						 'r_0936__Vmax_r_0936',
						 'r_0936__kmp_s_0939r_0936',
						 'r_0936__kmp_s_1091r_0936',
						 'r_0936__kms_s_0120r_0936',
						 'r_0936__kms_s_0763_br_0936',
						 'r_0936__kms_s_1096r_0936',
						 'r_0937__Keq_r_0937',
						 'r_0937__Vmax_r_0937',
						 'r_0937__kmp_s_0400r_0937',
						 'r_0937__kmp_s_0763_br_0937',
						 'r_0937__kmp_s_1156r_0937',
						 'r_0937__kmp_s_1207r_0937',
						 'r_0937__kms_s_0446r_0937',
						 'r_0937__kms_s_0458r_0937',
						 'r_0937__kms_s_1277r_0937',
						 'r_0938__Keq_r_0938',
						 'r_0938__Vmax_r_0938',
						 'r_0938__kmp_s_0366r_0938',
						 'r_0938__kmp_s_0470r_0938',
						 'r_0938__kms_s_0763_br_0938',
						 'r_0938__kms_s_1277r_0938',
						 'r_0940__Keq_r_0940',
						 'r_0940__Vmax_r_0940',
						 'r_0940__kmp_s_0380r_0940',
						 'r_0940__kmp_s_0470r_0940',
						 'r_0940__kmp_s_1087r_0940',
						 'r_0940__kms_s_0514r_0940',
						 'r_0940__kms_s_1082r_0940',
						 'r_0940__kms_s_1277r_0940',
						 'r_0941__Keq_r_0941',
						 'r_0941__Vmax_r_0941',
						 'r_0941__kmp_s_0446r_0941',
						 'r_0941__kmp_s_1277r_0941',
						 'r_0941__kms_s_0400r_0941',
						 'r_0941__kms_s_0763_br_0941',
						 'r_0941__kms_s_1243r_0941',
						 'r_0948__Keq_r_0948',
						 'r_0948__Vmax_r_0948',
						 'r_0948__kmp_s_0335r_0948',
						 'r_0948__kmp_s_1207r_0948',
						 'r_0948__kmp_s_1434_br_0948',
						 'r_0948__kms_s_0163r_0948',
						 'r_0948__kms_s_0320r_0948',
						 'r_0949__Keq_r_0949',
						 'r_0949__Vmax_r_0949',
						 'r_0949__kmp_s_0320r_0949',
						 'r_0949__kmp_s_1283r_0949',
						 'r_0949__kms_s_0335r_0949',
						 'r_0951__Keq_r_0951',
						 'r_0951__Vmax_r_0951',
						 'r_0951__kmp_s_0562r_0951',
						 'r_0951__kmp_s_1434_br_0951',
						 'r_0951__kmp_s_1517r_0951',
						 'r_0951__kms_s_0400r_0951',
						 'r_0951__kms_s_1521r_0951',
						 'r_0955__Keq_r_0955',
						 'r_0955__Vmax_r_0955',
						 'r_0955__kmp_s_0591r_0955',
						 'r_0955__kmp_s_1434_br_0955',
						 'r_0955__kmp_s_1517r_0955',
						 'r_0955__kms_s_0706r_0955',
						 'r_0955__kms_s_1521r_0955',
						 'r_0957__Keq_r_0957',
						 'r_0957__Vmax_r_0957',
						 'r_0957__kmp_s_0622r_0957',
						 'r_0957__kmp_s_1434_br_0957',
						 'r_0957__kmp_s_1517r_0957',
						 'r_0957__kms_s_1411r_0957',
						 'r_0957__kms_s_1521r_0957',
						 'r_0959__Keq_r_0959',
						 'r_0959__Vmax_r_0959',
						 'r_0959__kmp_s_0566r_0959',
						 'r_0959__kmp_s_1434_br_0959',
						 'r_0959__kmp_s_1517r_0959',
						 'r_0959__kms_s_0446r_0959',
						 'r_0959__kms_s_1521r_0959',
						 'r_0963__Keq_r_0963',
						 'r_0963__Vmax_r_0963',
						 'r_0963__kmp_s_0427r_0963',
						 'r_0963__kms_s_0557r_0963',
						 'r_0965__Keq_r_0965',
						 'r_0965__Vmax_r_0965',
						 'r_0965__kmp_s_0557r_0965',
						 'r_0965__kms_s_0561r_0965',
						 'r_0967__Keq_r_0967',
						 'r_0967__Vmax_r_0967',
						 'r_0967__kmp_s_0669r_0967',
						 'r_0967__kmp_s_0763_br_0967',
						 'r_0967__kmp_s_1290r_0967',
						 'r_0967__kms_s_1293r_0967',
						 'r_0967__kms_s_1447r_0967',
						 'r_0969__Keq_r_0969',
						 'r_0969__Vmax_r_0969',
						 'r_0969__kmp_s_0185r_0969',
						 'r_0969__kmp_s_0763_br_0969',
						 'r_0969__kmp_s_0929r_0969',
						 'r_0969__kmp_s_1087r_0969',
						 'r_0969__kms_s_0942r_0969',
						 'r_0969__kms_s_1082r_0969',
						 'r_0969__kms_s_1434_br_0969',
						 'r_0970__Keq_r_0970',
						 'r_0970__Vmax_r_0970',
						 'r_0970__kmp_s_0942r_0970',
						 'r_0970__kmp_s_1091r_0970',
						 'r_0970__kmp_s_1434_br_0970',
						 'r_0970__kms_s_0763_br_0970',
						 'r_0970__kms_s_0867r_0970',
						 'r_0970__kms_s_0899r_0970',
						 'r_0970__kms_s_1096r_0970',
						 'r_0972__Keq_r_0972',
						 'r_0972__Vmax_r_0972',
						 'r_0972__kmp_s_0218r_0972',
						 'r_0972__kmp_s_0470r_0972',
						 'r_0972__kmp_s_0514r_0972',
						 'r_0972__kms_s_0943r_0972',
						 'r_0972__kms_s_1187r_0972',
						 'r_0976__Keq_r_0976',
						 'r_0976__Vmax_r_0976',
						 'r_0976__kmp_s_1091r_0976',
						 'r_0976__kmp_s_1306r_0976',
						 'r_0976__kms_s_0217r_0976',
						 'r_0976__kms_s_0763_br_0976',
						 'r_0976__kms_s_1096r_0976',
						 'r_0977__Keq_r_0977',
						 'r_0977__Vmax_r_0977',
						 'r_0977__kmp_s_0267r_0977',
						 'r_0977__kmp_s_0400r_0977',
						 'r_0977__kmp_s_0763_br_0977',
						 'r_0977__kms_s_0446r_0977',
						 'r_0977__kms_s_1306r_0977',
						 'r_0991__Keq_r_0991',
						 'r_0991__Vmax_r_0991',
						 'r_0991__kmp_s_0040r_0991',
						 'r_0991__kmp_s_1082r_0991',
						 'r_0991__kmp_s_1434_br_0991',
						 'r_0991__kms_s_0763_br_0991',
						 'r_0991__kms_s_1087r_0991',
						 'r_0991__kms_s_1160r_0991',
						 'r_0991__kms_s_1327r_0991',
						 'r_0993__Keq_r_0993',
						 'r_0993__Vmax_r_0993',
						 'r_0993__kmp_s_0605r_0993',
						 'r_0993__kmp_s_1091r_0993',
						 'r_0993__kmp_s_1327r_0993',
						 'r_0993__kms_s_0195r_0993',
						 'r_0993__kms_s_0763_br_0993',
						 'r_0993__kms_s_1096r_0993',
						 'r_0995__Keq_r_0995',
						 'r_0995__Vmax_r_0995',
						 'r_0995__kmp_s_0641r_0995',
						 'r_0995__kmp_s_1434_br_0995',
						 'r_0995__kms_s_0635r_0995',
						 'r_0995__kms_s_0663r_0995',
						 'r_1003__Keq_r_1003',
						 'r_1003__Vmax_r_1003',
						 'r_1003__kmp_s_0400r_1003',
						 'r_1003__kmp_s_1207r_1003',
						 'r_1003__kmp_s_1342r_1003',
						 'r_1003__kms_s_0446r_1003',
						 'r_1003__kms_s_0514r_1003',
						 'r_1003__kms_s_1338r_1003',
						 'r_1007__Keq_r_1007',
						 'r_1007__Vmax_r_1007',
						 'r_1007__kmp_s_0304r_1007',
						 'r_1007__kmp_s_1207r_1007',
						 'r_1007__kms_s_0400r_1007',
						 'r_1007__kms_s_0763_br_1007',
						 'r_1007__kms_s_1347r_1007',
						 'r_1008__Keq_r_1008',
						 'r_1008__Vmax_r_1008',
						 'r_1008__kmp_s_0805r_1008',
						 'r_1008__kmp_s_1091r_1008',
						 'r_1008__kmp_s_1434_br_1008',
						 'r_1008__kms_s_0763_br_1008',
						 'r_1008__kms_s_1096r_1008',
						 'r_1008__kms_s_1349r_1008',
						 'r_1024__Keq_r_1024',
						 'r_1024__Vmax_r_1024',
						 'r_1024__kmp_s_1091r_1024',
						 'r_1024__kmp_s_1521r_1024',
						 'r_1024__kms_s_0763_br_1024',
						 'r_1024__kms_s_1096r_1024',
						 'r_1024__kms_s_1517r_1024',
						 'r_1026__Keq_r_1026',
						 'r_1026__Vmax_r_1026',
						 'r_1026__kmp_s_0366r_1026',
						 'r_1026__kmp_s_0740r_1026',
						 'r_1026__kms_s_0949r_1026',
						 'r_1027__Keq_r_1027',
						 'r_1027__Vmax_r_1027',
						 'r_1027__kmp_s_0949r_1027',
						 'r_1027__kmp_s_1207r_1027',
						 'r_1027__kms_s_1122r_1027',
						 'r_1027__kms_s_1434_br_1027',
						 'r_1032__Keq_r_1032',
						 'r_1032__Vmax_r_1032',
						 'r_1032__kmp_s_0601r_1032',
						 'r_1032__kmp_s_0619r_1032',
						 'r_1032__kms_s_0307r_1032',
						 'r_1032__kms_s_0624r_1032',
						 'r_1035__Keq_r_1035',
						 'r_1035__Vmax_r_1035',
						 'r_1035__kmp_s_0731r_1035',
						 'r_1035__kmp_s_1304r_1035',
						 'r_1035__kms_s_0533r_1035',
						 'r_1035__kms_s_0539r_1035',
						 'r_1036__Keq_r_1036',
						 'r_1036__Vmax_r_1036',
						 'r_1036__kmp_s_0427r_1036',
						 'r_1036__kmp_s_0561r_1036',
						 'r_1036__kms_s_0731r_1036',
						 'r_1036__kms_s_1304r_1036',
						 'r_1037__Keq_r_1037',
						 'r_1037__Vmax_r_1037',
						 'r_1037__kmp_s_0533r_1037',
						 'r_1037__kmp_s_0561r_1037',
						 'r_1037__kms_s_0539r_1037',
						 'r_1037__kms_s_0731r_1037',
						 'r_1038__Keq_r_1038',
						 'r_1038__Vmax_r_1038',
						 'r_1038__kmp_s_0416r_1038',
						 'r_1038__kmp_s_1207r_1038',
						 'r_1038__kms_s_0419r_1038',
						 'r_1038__kms_s_1434_br_1038',
						 'r_1040__Keq_r_1040',
						 'r_1040__Vmax_r_1040',
						 'r_1040__kmp_s_0596r_1040',
						 'r_1040__kmp_s_0663r_1040',
						 'r_1040__kms_s_1399r_1040',
						 'r_1040__kms_s_1434_br_1040',
						 'r_1041__Keq_r_1041',
						 'r_1041__Vmax_r_1041',
						 'r_1041__kmp_s_0731r_1041',
						 'r_1041__kms_s_0735r_1041',
						 'r_1042__Keq_r_1042',
						 'r_1042__Vmax_r_1042',
						 'r_1042__kmp_s_0731r_1042',
						 'r_1042__kmp_s_0952r_1042',
						 'r_1042__kmp_s_1434_br_1042',
						 'r_1042__kms_s_0088r_1042',
						 'r_1042__kms_s_0943r_1042',
						 'r_1050__Keq_r_1050',
						 'r_1050__Vmax_r_1050',
						 'r_1050__kmp_s_0185r_1050',
						 'r_1050__kmp_s_0955r_1050',
						 'r_1050__kms_s_0209r_1050',
						 'r_1050__kms_s_0899r_1050',
						 'r_1059__Keq_r_1059',
						 'r_1059__Vmax_r_1059',
						 'r_1059__kmp_s_0400r_1059',
						 'r_1059__kmp_s_1411r_1059',
						 'r_1059__kms_s_0446r_1059',
						 'r_1059__kms_s_1417r_1059',
						 'r_1066__Keq_r_1066',
						 'r_1066__Vmax_r_1066',
						 'r_1066__kmp_s_0446r_1066',
						 'r_1066__kmp_s_0624r_1066',
						 'r_1066__kms_s_0400r_1066',
						 'r_1066__kms_s_0622r_1066',
						 'r_1072__Keq_r_1072',
						 'r_1072__Vmax_r_1072',
						 'r_1072__kmp_s_0605r_1072',
						 'r_1072__kmp_s_1415r_1072',
						 'r_1072__kms_s_0549r_1072',
						 'r_1072__kms_s_0763_br_1072',
						 'r_1072__kms_s_1430r_1072',
						 'r_1073__Keq_r_1073',
						 'r_1073__Vmax_r_1073',
						 'r_1073__kmp_s_0185r_1073',
						 'r_1073__kmp_s_0960r_1073',
						 'r_1073__kms_s_0238r_1073',
						 'r_1073__kms_s_0899r_1073',
						 'r_1157__Keq_r_1157',
						 'r_1157__Vmax_r_1157',
						 'r_1157__kmp_s_0430r_1157',
						 'r_1157__kms_s_0431_br_1157',
						 'r_1194__Keq_r_1194',
						 'r_1194__Vmax_r_1194',
						 'r_1194__kmp_s_0472_br_1194',
						 'r_1194__kms_s_0470r_1194',
						 'r_1247__Keq_r_1247',
						 'r_1247__Vmax_r_1247',
						 'r_1247__kmp_s_0651_br_1247',
						 'r_1247__kms_s_0650r_1247',
						 'r_1293__Keq_r_1293',
						 'r_1293__Vmax_r_1293',
						 'r_1293__kmp_s_0545r_1293',
						 'r_1293__kms_s_0547_br_1293',
						 'r_1435__Keq_r_1435',
						 'r_1435__Vmax_r_1435',
						 'r_1435__kmp_s_1160r_1435',
						 'r_1435__kms_s_1162_br_1435',
						 'r_1461__Keq_r_1461',
						 'r_1461__Vmax_r_1461',
						 'r_1461__kmp_s_0763_br_1461',
						 'r_1461__kmp_s_1207r_1461',
						 'r_1461__kms_s_0766_br_1461',
						 'r_1461__kms_s_1209_br_1461',
						 'r_1503__Keq_r_1503',
						 'r_1503__Vmax_r_1503',
						 'r_1503__kmp_s_0766_br_1503',
						 'r_1503__kmp_s_1339_br_1503',
						 'r_1503__kms_s_0763_br_1503',
						 'r_1503__kms_s_1338r_1503',
						 'r_1507__Keq_r_1507',
						 'r_1507__Vmax_r_1507',
						 'r_1507__kmp_s_1347r_1507',
						 'r_1507__kms_s_1348_br_1507',
						 'r_1672__Keq_r_1672',
						 'r_1672__Vmax_r_1672',
						 'r_1672__kmp_s_0386r_1672',
						 'r_1672__kms_s_1342r_1672',
						 'r_1812__V_o',
						 'r_1812__a_s_0001r_1812',
						 'r_1812__s_0001_or_1812',
						 'r_1812__a_s_0416r_1812',
						 'r_1812__s_0416_or_1812',
						 'r_1812__a_s_0434r_1812',
						 'r_1812__s_0434_or_1812',
						 'r_1812__a_s_0446r_1812',
						 'r_1812__s_0446_or_1812',
						 'r_1812__a_s_0511r_1812',
						 'r_1812__s_0511_or_1812',
						 'r_1812__a_s_0564r_1812',
						 'r_1812__s_0564_or_1812',
						 'r_1812__a_s_0569r_1812',
						 'r_1812__s_0569_or_1812',
						 'r_1812__a_s_0593r_1812',
						 'r_1812__s_0593_or_1812',
						 'r_1812__a_s_0619r_1812',
						 'r_1812__s_0619_or_1812',
						 'r_1812__a_s_0740r_1812',
						 'r_1812__s_0740_or_1812',
						 'r_1812__a_s_0743r_1812',
						 'r_1812__s_0743_or_1812',
						 'r_1812__a_s_0752r_1812',
						 'r_1812__s_0752_or_1812',
						 'r_1812__a_s_0863r_1812',
						 'r_1812__s_0863_or_1812',
						 'r_1812__a_s_0873r_1812',
						 'r_1812__s_0873_or_1812',
						 'r_1812__a_s_0877r_1812',
						 'r_1812__s_0877_or_1812',
						 'r_1812__a_s_0881r_1812',
						 'r_1812__s_0881_or_1812',
						 'r_1812__a_s_0889r_1812',
						 'r_1812__s_0889_or_1812',
						 'r_1812__a_s_0899r_1812',
						 'r_1812__s_0899_or_1812',
						 'r_1812__a_s_0907r_1812',
						 'r_1812__s_0907_or_1812',
						 'r_1812__a_s_0911r_1812',
						 'r_1812__s_0911_or_1812',
						 'r_1812__a_s_0920r_1812',
						 'r_1812__s_0920_or_1812',
						 'r_1812__a_s_0925r_1812',
						 'r_1812__s_0925_or_1812',
						 'r_1812__a_s_0929r_1812',
						 'r_1812__s_0929_or_1812',
						 'r_1812__a_s_0933r_1812',
						 'r_1812__s_0933_or_1812',
						 'r_1812__a_s_0936r_1812',
						 'r_1812__s_0936_or_1812',
						 'r_1812__a_s_0939r_1812',
						 'r_1812__s_0939_or_1812',
						 'r_1812__a_s_0943r_1812',
						 'r_1812__s_0943_or_1812',
						 'r_1812__a_s_0949r_1812',
						 'r_1812__s_0949_or_1812',
						 'r_1812__a_s_0952r_1812',
						 'r_1812__s_0952_or_1812',
						 'r_1812__a_s_0955r_1812',
						 'r_1812__s_0955_or_1812',
						 'r_1812__a_s_0960r_1812',
						 'r_1812__s_0960_or_1812',
						 'r_1812__a_s_1000r_1812',
						 'r_1812__s_1000_or_1812',
						 'r_1812__a_s_1011r_1812',
						 'r_1812__s_1011_or_1812',
						 'r_1812__a_s_1347r_1812',
						 'r_1812__s_1347_or_1812',
						 'r_1812__a_s_1417r_1812',
						 'r_1812__s_1417_or_1812',
						 'r_1812__a_s_1283r_1812',
						 'r_1812__s_1283_or_1812',
						 'r_1814__V_o',
						 'r_1814__a_s_0463r_1814',
						 'r_1814__s_0463_or_1814',
						 'r_1816__V_o',
						 'r_1816__a_s_0090r_1816',
						 'r_1816__s_0090_or_1816',
						 'r_1816__a_s_0124r_1816',
						 'r_1816__s_0124_or_1816',
						 'r_1816__a_s_0627r_1816',
						 'r_1816__s_0627_or_1816',
						 'r_1816__a_s_0632r_1816',
						 'r_1816__s_0632_or_1816',
						 'r_1816__a_s_0635r_1816',
						 'r_1816__s_0635_or_1816',
						 'r_1816__a_s_0641r_1816',
						 'r_1816__s_0641_or_1816',
						 'r_1816__a_s_0663r_1816',
						 'r_1816__s_0663_or_1816',
						 'r_1816__a_s_0669r_1816',
						 'r_1816__s_0669_or_1816',
						 'r_1816__a_s_0824r_1816',
						 'r_1816__s_0824_or_1816',
						 'r_1816__a_s_0963r_1816',
						 'r_1816__s_0963_or_1816',
						 'r_1816__a_s_1219r_1816',
						 'r_1816__s_1219_or_1816',
						 'r_1816__a_s_1228r_1816',
						 'r_1816__s_1228_or_1816',
						 'r_1816__a_s_1233r_1816',
						 'r_1816__s_1233_or_1816',
						 'r_1816__a_s_1399r_1816',
						 'r_1816__s_1399_or_1816',
						 'r_1816__a_s_1447r_1816',
						 'r_1816__s_1447_or_1816',
						 'intracellular',
						 'extracellular']
	module_dict['initvars'] = {'s_1005': 0.548999999216,
						 's_0430': 0.548999999216,
						 's_0899': 0.548999996435,
						 's_0554': 0.548999999216,
						 's_1000': 0.54900000371,
						 's_1122': 0.548999999216,
						 's_0124': 0.548999999216,
						 's_1160': 0.548999996463,
						 's_0669': 0.548999999216,
						 's_0320': 0.548999999216,
						 's_1277': 0.0605904998459,
						 's_0325': 0.549000001219,
						 's_0521': 0.54900000196,
						 's_1226': 0.548999999216,
						 's_0328': 0.548999999216,
						 's_0464_b': 24.499999887,
						 's_1080': 0.549000001971,
						 's_0481': 0.54899999608,
						 's_0529': 0.549000000915,
						 's_0069': 0.549000001219,
						 's_0079': 0.548999999216,
						 's_0078': 0.548999996529,
						 's_0083': 0.548999995995,
						 's_0400': 1.71906998614,
						 's_1087': 0.0867352997424,
						 's_0247': 0.549000000915,
						 's_1325': 0.548999999216,
						 's_1082': 1.50325999658,
						 's_0749': 0.548999995944,
						 's_1379': 0.548999996262,
						 's_0873': 0.548999999216,
						 's_0911': 0.548999999216,
						 's_1209_b': 24.49999974,
						 's_0877': 0.548999999216,
						 's_0801': 0.549000001219,
						 's_0641': 0.548999999216,
						 's_1447': 0.548999999216,
						 's_0917': 0.548999999216,
						 's_1073': 0.548999999216,
						 's_1070': 0.548999999216,
						 's_1071': 0.548999996383,
						 's_0763_b': 0.548999999216,
						 's_0755': 0.548999999216,
						 's_0627': 0.548999999216,
						 's_0553': 0.54900000196,
						 's_0046': 0.548999999216,
						 's_0410': 0.548999996395,
						 's_0040': 0.548999999216,
						 's_0319': 0.548999999216,
						 's_0042': 0.548999999216,
						 's_0315': 0.548999999216,
						 's_0316': 0.548999996168,
						 's_0317': 0.548999999216,
						 's_0798': 0.549000001219,
						 's_0397': 0.548999996619,
						 's_0416': 0.548999999216,
						 's_0393': 0.548999996273999,
						 's_0167': 0.549000001219,
						 's_0254': 0.549000000915,
						 's_0257': 0.549000000915,
						 's_0163': 0.549000001186,
						 's_1456': 0.548999999216,
						 's_0659': 0.548999996435,
						 's_0712': 0.548999999216,
						 's_1434_b': 0.548999999216,
						 's_0963': 0.548999999685,
						 's_1342': 0.548999999216,
						 's_0960': 0.99999999807,
						 's_0650': 49.9999997395,
						 's_0847': 0.548999999216,
						 's_1349': 0.548999999216,
						 's_0419': 0.548999996395,
						 's_0657': 0.548999999216,
						 's_0968': 0.54899999668,
						 's_0193': 0.05150660046,
						 's_0828': 0.548999999216,
						 's_0195': 0.548999999216,
						 's_0824': 0.548999999216,
						 's_1293': 0.548999996273,
						 's_1290': 0.548999996435,
						 's_0052': 0.548999999216,
						 's_0309': 0.548999999216,
						 's_1215': 0.548999999216,
						 's_0545': 0.09875869957,
						 's_1455': 0.548999999216,
						 's_0055': 0.548999999216,
						 's_0485': 0.548999999216,
						 's_0303': 0.54899999551,
						 's_0302': 0.548999999216,
						 's_0301': 0.548999999216,
						 's_0058': 0.548999999216,
						 's_0307': 0.549000001826,
						 's_0306': 0.549000002154,
						 's_0987': 0.548999997213,
						 's_0304': 0.548999996343,
						 's_0268': 0.54900000196,
						 's_0615': 0.548999999216,
						 's_0118': 0.548999996262,
						 's_0380': 0.548999996435,
						 's_0386': 0.548999995995,
						 's_0663': 0.548999996435,
						 's_0261': 0.549000000915,
						 's_0894': 0.548999999216,
						 's_0264': 0.363387999607,
						 's_0265': 0.000108759000085,
						 's_0267': 0.548999997773,
						 's_0859': 0.548999996435,
						 's_0692': 0.548999999216,
						 's_0916': 0.548999996435,
						 's_0463': 0.548999999216,
						 's_1334': 0.548999996435,
						 's_0915': 0.549000003759,
						 's_0706': 0.548999996111,
						 's_0850': 0.548999996435,
						 's_0468': 0.548999999216,
						 's_0469': 0.548999996395,
						 's_0181': 0.548999996435,
						 's_0170': 0.548999999216,
						 's_0183': 0.549000000846,
						 's_0185': 0.548999999216,
						 's_1521': 0.548999996236,
						 's_0431_b': 37.9999998108,
						 's_0591': 0.54899999608,
						 's_1051': 0.548999999216,
						 's_1052': 0.548999996413,
						 's_1053': 0.548999999216,
						 's_1339_b': 0.9999999981,
						 's_1207': 0.548999999216,
						 's_1283': 0.548999999216,
						 's_0574': 0.54899999668,
						 's_0369': 0.54900000196,
						 's_1117': 0.548999996395,
						 's_0889': 0.548999999216,
						 's_0455': 0.496413999333,
						 's_0863': 0.548999995944,
						 's_0022': 0.548999996395,
						 's_1228': 0.548999999216,
						 's_0021': 0.548999996063,
						 's_0374': 0.548999999216,
						 's_0632': 0.54900000196,
						 's_0238': 0.549000001999,
						 's_0905': 0.54899999748,
						 's_0470': 0.99999999807,
						 's_0907': 0.548999995879,
						 's_1348_b': 42.19999979,
						 's_1162_b': 24.49999989,
						 's_1048': 0.548999996395,
						 's_1327': 0.548999996687,
						 's_1060': 0.548999996463,
						 's_0800': 0.548999999216,
						 's_0710': 0.548999996435,
						 's_1329': 0.548999999216,
						 's_1347': 0.548999996474,
						 's_0805': 0.548999996395,
						 's_1458': 0.548999999216,
						 's_1044': 0.54899999668,
						 's_0881': 0.548999996273,
						 's_0569': 0.548999996395,
						 's_1233': 0.548999996395,
						 's_0206': 0.548999996343,
						 's_0886': 0.548999996435,
						 's_0887': 0.548999996406,
						 's_0888': 0.548999999216,
						 's_0562': 0.54899999608,
						 's_0561': 0.548999999216,
						 's_0209': 0.548999996529,
						 's_0566': 0.548999996435,
						 's_0564': 0.548999999216,
						 's_0031': 0.548999996568,
						 's_0689': 0.548999999216,
						 's_1187': 0.548999999216,
						 's_0366': 0.120104000134,
						 's_0605': 0.548999996218,
						 's_0939': 0.548999999216,
						 's_0446': 1.09207999161,
						 's_0601': 0.54900000196,
						 's_1355': 0.548999996395,
						 's_0936': 0.548999999216,
						 's_0933': 0.548999996434,
						 's_0919': 0.548999999216,
						 's_1091': 0.548999999216,
						 's_1338': 0.548999999216,
						 's_0955': 0.548999999216,
						 's_0952': 0.99999999807,
						 's_0088': 0.548999996529,
						 's_0122': 0.548999996383,
						 's_0120': 0.549000001186,
						 's_0215': 0.54899999551,
						 's_0472_b': 1.00000027208e-05,
						 's_0217': 0.548999999216,
						 's_0216': 0.549000001219,
						 's_0080': 0.5489999965,
						 's_0218': 0.549000001826,
						 's_1225': 0.548999996435,
						 's_0128': 0.5489999965,
						 's_0001': 0.549000001186,
						 's_0752': 0.548999996279,
						 's_0007': 0.549000001219,
						 's_0008': 0.548999999216,
						 's_0009': 0.549000001219,
						 's_0514': 0.548999995995,
						 's_0766_b': 0.1,
						 's_0356': 0.548999999216,
						 's_0511': 0.548999999216,
						 's_0596': 0.548999995995,
						 's_0929': 0.548999999216,
						 's_0616': 0.548999996435,
						 's_0651_b': 24.49999989,
						 's_0593': 0.548999999216,
						 's_0458': 0.548999996101,
						 's_0180': 0.548999995536,
						 's_0920': 0.548999999216,
						 's_0619': 0.548999999216,
						 's_0297': 0.548999999216,
						 's_1415': 0.549000001186,
						 's_1140': 0.54899999668,
						 's_1417': 0.548999999216,
						 's_0949': 1.00000000123,
						 's_1411': 0.548999999216,
						 's_0090': 0.548999996262,
						 's_1304': 0.548999999216,
						 's_1306': 0.548999999216,
						 's_1457': 0.548999996369,
						 's_0943': 0.548999996435,
						 's_0942': 0.549000002886,
						 's_0861': 0.548999999216,
						 's_0549': 0.548999999216,
						 's_1258': 0.548999999216,
						 's_1028': 0.54899999668,
						 's_0225': 0.549000001866,
						 's_1020': 0.548999999216,
						 's_1132': 0.54899999668,
						 's_0743': 0.548999999216,
						 's_0740': 0.548999999216,
						 's_0150': 0.54900000196,
						 's_0018': 0.548999999216,
						 's_0017': 0.549000001219,
						 's_0015': 0.548999996435,
						 's_1399': 0.548999999216,
						 's_0501': 0.5489999965,
						 's_0500': 0.548999995879,
						 's_0158': 0.54899999593,
						 's_0010': 0.548999996568,
						 's_0816': 0.548999996273,
						 's_0622': 0.548999996395,
						 's_0735': 0.601872999094,
						 's_0624': 0.548999996395,
						 's_1517': 0.548999999216,
						 's_0582': 0.54899999668,
						 's_1219': 0.549000001352,
						 's_1066': 0.548999999216,
						 's_0427': 0.548999996273999,
						 's_0507': 0.548999996435,
						 's_1151': 0.548999996395,
						 's_1170': 0.548999999216,
						 's_1155': 0.548999999216,
						 's_1154': 0.548999999216,
						 's_0925': 0.548999999216,
						 's_1156': 0.548999996435,
						 's_1315': 12.8510998429,
						 's_0977': 0.54899999668,
						 's_1430': 0.548999995967,
						 's_0333': 0.548999996435,
						 's_0330': 0.548999999216,
						 's_0331': 0.548999996435,
						 's_0334': 0.548999999216,
						 's_0335': 0.548999996262,
						 's_1011': 0.548999999216,
						 's_1243': 0.0271092999605,
						 's_1013': 0.548999999216,
						 's_0234': 0.548999999216,
						 's_0145': 0.54900000196,
						 's_0539': 0.104554999996,
						 's_0146': 0.54900000196,
						 's_1096': 0.548999996474,
						 's_0547_b': 11.1,
						 's_0530': 0.548999999216,
						 's_0532': 0.548999996369,
						 's_0533': 0.549000000621,
						 's_0149': 0.548999996435,
						 's_0064': 0.548999996435,
						 's_0537': 1.34278000007,
						 's_0439': 0.548999996435,
						 's_0438': 0.549000001219,
						 's_0734': 0.54899999611,
						 's_0212': 0.548999996435,
						 's_0732': 0.149999999336,
						 's_0867': 0.548999999216,
						 's_0731': 0.0436363000303,
						 's_1257': 0.548999996435,
						 's_0318': 0.548999999216,
						 's_0635': 0.548999999216,
						 's_0434': 1.25955999733,
						 's_0557': 0.549000001186}
	module_dict['initpars'] = {'r_0419__kms_s_0968r_0419': 0.549,
						 'r_0418__Vmax_r_0418': 0.00599719,
						 'r_0581__Vmax_r_0581': 0.731504,
						 'r_0423__kmp_s_0470r_0423': 1.0,
						 'r_0890__kmp_s_1207r_0890': 0.549,
						 'r_1816__s_0669_or_1816': 0.549,
						 'r_0284__Keq_r_0284': 2.00364,
						 'r_0911__kmp_s_0470r_0911': 1.0,
						 'r_0993__kms_s_1096r_0993': 0.549,
						 'r_0384__kmp_s_0238r_0384': 0.549,
						 'r_0064__kms_s_1082r_0064': 1.50326,
						 'r_0969__kms_s_1434_br_0969': 0.549,
						 'r_0965__kmp_s_0557r_0965': 0.549,
						 'r_0539__Keq_r_0539': 2.00364,
						 'r_0488__kmp_s_1338r_0488': 0.549,
						 'r_0657__kmp_s_1434_br_0657': 0.549,
						 'r_0510__Keq_r_0510': 34.7263,
						 'r_0937__kms_s_0446r_0937': 1.09208,
						 'r_0165__kmp_s_0755r_0165': 0.549,
						 'r_0360__Keq_r_0360': 0.698801,
						 'r_0387__kms_s_0850r_0387': 0.549,
						 'r_0883__Vmax_r_0883': 0.46739,
						 'r_0959__kmp_s_1434_br_0959': 0.549,
						 'r_1050__kms_s_0209r_1050': 0.549,
						 'r_0464__kmp_s_1434_br_0464': 0.549,
						 'r_0163__kms_s_0400r_0163': 1.71907,
						 'r_0538__kms_s_1082r_0538': 1.50326,
						 'r_0226__Vmax_r_0226': 1.90762,
						 'r_0657__Keq_r_0657': 0.331541,
						 'r_0169__Keq_r_0169': 0.6039,
						 'r_0607__kms_s_0816r_0607': 0.549,
						 'r_0025__Keq_r_0025': 0.6039,
						 'r_0466__kms_s_1044r_0466': 0.549,
						 'r_0719__kms_s_1091r_0719': 0.549,
						 'r_0339__kmp_s_0889r_0339': 0.549,
						 'r_0650__kmp_s_0434r_0650': 1.25956,
						 'r_0765__Vmax_r_0765': 1.0241,
						 'r_0059__kmp_s_1082r_0059': 1.50326,
						 'r_0712__Keq_r_0712': 0.6039,
						 'r_1026__kms_s_0949r_1026': 1.0,
						 'r_0959__Keq_r_0959': 0.303587,
						 'r_0573__kmp_s_0400r_0573': 1.71907,
						 'r_0567__kmp_s_0706r_0567': 0.549,
						 'r_1812__a_s_0877r_1812': 0.17152,
						 'r_0779__Vmax_r_0779': 7.3843,
						 'r_0588__Vmax_r_0588': 8.76037,
						 'r_0951__kmp_s_1517r_0951': 0.549,
						 'r_0891__kmp_s_0434r_0891': 1.25956,
						 'r_0573__Keq_r_0573': 2000.0,
						 'r_0969__kmp_s_0929r_0969': 0.549,
						 'r_0702__kmp_s_0309r_0702': 0.549,
						 'r_0951__kms_s_0400r_0951': 1.71907,
						 'r_0485__kms_s_0069r_0485': 0.549,
						 'r_0287__kms_s_0763_br_0287': 0.549,
						 'r_0712__kmp_s_0763_br_0712': 0.549,
						 'r_1435__kms_s_1162_br_1435': 24.5,
						 'r_0268__kmp_s_1091r_0268': 0.549,
						 'r_0551__Keq_r_0551': 0.382386,
						 'r_0638__Vmax_r_0638': 0.025113,
						 'r_0266__kms_s_1160r_0266': 0.549,
						 'r_0306__Keq_r_0306': 0.6039,
						 'r_0093__kmp_s_1091r_0093': 0.549,
						 'r_0585__Vmax_r_0585': 1.60929,
						 'r_0025__kms_s_0167r_0025': 0.549,
						 'r_1507__kmp_s_1347r_1507': 0.549,
						 'r_0599__Keq_r_0599': 1.1,
						 'r_0374__kmp_s_1154r_0374': 0.549,
						 'r_0582__kmp_s_0798r_0582': 0.549,
						 'r_0955__kms_s_1521r_0955': 0.549,
						 'r_0783__Vmax_r_0783': 0.624358,
						 'r_0874__kms_s_1226r_0874': 0.549,
						 'r_0529__Keq_r_0529': 0.0515178,
						 'r_0722__kmp_s_1096r_0722': 0.549,
						 'r_0016__Vmax_r_0016': 1.15193,
						 'r_0442__Keq_r_0442': 0.953736,
						 'r_0504__kmp_s_0539r_0504': 0.104555,
						 'r_0599__kms_s_0374r_0599': 0.549,
						 'r_0386__kms_s_0446r_0386': 1.09208,
						 'r_0437__kmp_s_1355r_0437': 0.549,
						 'r_0940__kmp_s_0470r_0940': 1.0,
						 'r_1026__kmp_s_0740r_1026': 0.549,
						 'r_0582__Keq_r_0582': 1.1,
						 'r_0362__kms_s_0400r_0362': 1.71907,
						 'r_1503__Keq_r_1503': 1.0,
						 'r_0512__kmp_s_0905r_0512': 0.549,
						 'r_0246__kmp_s_1434_br_0246': 0.549,
						 'r_0728__Vmax_r_0728': 1.2441,
						 'r_0112__Vmax_r_0112': 2.1714,
						 'r_0261__Keq_r_0261': 0.6039,
						 'r_0970__Keq_r_0970': 2.00364,
						 'r_0421__kmp_s_1091r_0421': 0.549,
						 'r_0394__kms_s_0615r_0394': 0.549,
						 'r_0125__kms_s_0514r_0125': 0.549,
						 'r_0650__kms_s_0763_br_0650': 0.549,
						 'r_0530__kmp_s_1082r_0530': 1.50326,
						 'r_1072__kms_s_0763_br_1072': 0.549,
						 'r_0362__Vmax_r_0362': 0.010395,
						 'r_0021__kms_s_0533r_0021': 0.549,
						 'r_0362__kmp_s_0593r_0362': 0.549,
						 'r_0043__kms_s_0356r_0043': 0.549,
						 'r_0233__kms_s_0446r_0233': 1.09208,
						 'r_0825__kmp_s_0936r_0825': 0.549,
						 'r_0330__kms_s_0507r_0330': 0.549,
						 'r_0014__kms_s_0146r_0014': 0.549,
						 'r_0352__kmp_s_0763_br_0352': 0.549,
						 'r_0484__kmp_s_0731r_0484': 0.0436363,
						 'r_0940__kms_s_0514r_0940': 0.549,
						 'r_0263__kms_s_0215r_0263': 0.549,
						 'r_1008__kms_s_1349r_1008': 0.549,
						 'r_0728__kmp_s_1207r_0728': 0.549,
						 'r_1035__Vmax_r_1035': 0.14014,
						 'r_1816__a_s_1228r_1816': 0.002884,
						 'r_0157__Keq_r_0157': 2.18098,
						 'r_0006__Vmax_r_0006': 1.58399,
						 'r_0567__kms_s_0446r_0567': 1.09208,
						 'r_1812__a_s_0960r_1812': 0.25728,
						 'r_0034__kmp_s_0434r_0034': 1.25956,
						 'r_0789__Keq_r_0789': 0.6039,
						 'r_1247__Keq_r_1247': 1.0,
						 'r_0701__kmp_s_1207r_0701': 0.549,
						 'r_0661__Vmax_r_0661': 3.30332,
						 'r_0169__kmp_s_0692r_0169': 0.549,
						 'r_0575__Vmax_r_0575': 0.688047,
						 'r_1042__kms_s_0943r_1042': 0.549,
						 'r_0183__Vmax_r_0183': 99.1,
						 'r_0225__kmp_s_0692r_0225': 0.549,
						 'r_0338__kmp_s_1434_br_0338': 0.549,
						 'r_0719__Keq_r_0719': 0.6039,
						 'r_0889__kmp_s_1052r_0889': 0.549,
						 'r_0936__Keq_r_0936': 3.64962,
						 'r_0159__kmp_s_0917r_0159': 0.549,
						 'r_0779__Keq_r_0779': 1.73154,
						 'r_0419__Keq_r_0419': 3.64962,
						 'r_0499__Vmax_r_0499': 72.4789,
						 'r_0698__kms_s_0539r_0698': 0.104555,
						 'r_0831__kms_s_1293r_0831': 0.549,
						 'r_0125__kmp_s_1434_br_0125': 0.549,
						 'r_0418__kmp_s_0514r_0418': 0.549,
						 'r_0031__kmp_s_0470r_0031': 1.0,
						 'r_0506__Vmax_r_0506': 0.54978,
						 'r_0965__Vmax_r_0965': 0.5577,
						 'r_0421__kms_s_1028r_0421': 0.549,
						 'r_0791__kms_s_0899r_0791': 0.549,
						 'r_0172__kmp_s_0763_br_0172': 0.549,
						 'r_0226__kms_s_0881r_0226': 0.549,
						 'r_0130__Vmax_r_0130': 0.58058,
						 'r_1461__Keq_r_1461': 1.0,
						 'r_0890__kms_s_0446r_0890': 1.09208,
						 'r_0488__kmp_s_0657r_0488': 0.549,
						 'r_0123__kms_s_0446r_0123': 1.09208,
						 'r_0674__kms_s_0297r_0674': 0.549,
						 'r_0386__kms_s_0734r_0386': 0.549,
						 'r_0725__kms_s_0128r_0725': 0.549,
						 'r_1816__s_1219_or_1816': 0.549,
						 'r_0970__Vmax_r_0970': 3.3649,
						 'r_0608__kms_s_0763_br_0608': 0.549,
						 'r_0340__Keq_r_0340': 0.6039,
						 'r_0040__kms_s_0557r_0040': 0.549,
						 'r_0783__kms_s_1117r_0783': 0.549,
						 'r_0425__kmp_s_1434_br_0425': 0.549,
						 'r_0783__kmp_s_0917r_0783': 0.549,
						 'r_0229__Keq_r_0229': 0.696513,
						 'r_0530__kms_s_0735r_0530': 0.601873,
						 'r_0886__kms_s_0881r_0886': 0.549,
						 'r_0284__kmp_s_0605r_0284': 0.549,
						 'r_0934__kmp_s_1207r_0934': 0.549,
						 'r_0911__kms_s_0763_br_0911': 0.549,
						 'r_0948__kmp_s_0335r_0948': 0.549,
						 'r_0226__kmp_s_0605r_0226': 0.549,
						 'r_1059__kmp_s_1411r_1059': 0.549,
						 'r_0699__Vmax_r_0699': 1.2166,
						 'r_0029__Keq_r_0029': 0.6039,
						 'r_0888__kms_s_0907r_0888': 0.549,
						 'r_0213__kms_s_0410r_0213': 0.549,
						 'r_0618__kmp_s_0824r_0618': 0.549,
						 'r_0512__Keq_r_0512': 19.0647,
						 'r_0886__kmp_s_1207r_0886': 0.549,
						 'r_0913__Vmax_r_0913': 0.648558,
						 'r_0859__kmp_s_0763_br_0859': 0.549,
						 'r_1032__Keq_r_1032': 1.1,
						 'r_0093__kmp_s_0328r_0093': 0.549,
						 'r_1812__a_s_0873r_1812': 0.13579,
						 'r_0225__kmp_s_0873r_0225': 0.549,
						 'r_1816__s_0635_or_1816': 0.549,
						 'r_0381__kms_s_1073r_0381': 0.549,
						 'r_0510__Vmax_r_0510': 31.5593,
						 'r_0418__kms_s_0763_br_0418': 0.549,
						 'r_0610__kms_s_1434_br_0610': 0.549,
						 'r_0029__kmp_s_0468r_0029': 0.549,
						 'r_0347__kms_s_0763_br_0347': 0.549,
						 'r_0949__kmp_s_1283r_0949': 0.549,
						 'r_0265__kmp_s_1434_br_0265': 0.549,
						 'r_0937__kmp_s_0763_br_0937': 0.549,
						 'r_0029__kms_s_0798r_0029': 0.549,
						 'r_0885__kms_s_0122r_0885': 0.549,
						 'r_0794__Vmax_r_0794': 0.52591,
						 'r_0515__kmp_s_0907r_0515': 0.549,
						 'r_0360__kmp_s_0446r_0360': 1.09208,
						 'r_0479__Vmax_r_0479': 0.087285,
						 'r_0585__kmp_s_0180r_0585': 0.549,
						 'r_0021__kms_s_1243r_0021': 0.0271093,
						 'r_0298__kms_s_1160r_0298': 0.549,
						 'r_0127__kmp_s_0369r_0127': 0.549,
						 'r_0875__kms_s_0554r_0875': 0.549,
						 'r_0016__kmp_s_0470r_0016': 1.0,
						 'r_0484__Vmax_r_0484': 5.50982,
						 'r_0429__kmp_s_0514r_0429': 0.549,
						 'r_0940__Keq_r_0940': 1.04749,
						 'r_0298__kmp_s_1290r_0298': 0.549,
						 'r_0026__kmp_s_0763_br_0026': 0.549,
						 'r_0357__kmp_s_0569r_0357': 0.549,
						 'r_0008__kmp_s_0315r_0008': 0.549,
						 'r_0057__kmp_s_1082r_0057': 1.50326,
						 'r_0765__Keq_r_0765': 2.00364,
						 'r_1194__kms_s_0470r_1194': 1.0,
						 'r_0506__kms_s_0446r_0506': 1.09208,
						 'r_0385__Keq_r_0385': 0.6039,
						 'r_0271__kmp_s_0635r_0271': 0.549,
						 'r_0306__Vmax_r_0306': 0.731496,
						 'r_0238__Vmax_r_0238': 13.3815,
						 'r_0394__Vmax_r_0394': 4.51436,
						 'r_0437__kms_s_0987r_0437': 0.549,
						 'r_0551__kms_s_1434_br_0551': 0.549,
						 'r_0525__kmp_s_1087r_0525': 0.0867353,
						 'r_1024__Keq_r_1024': 2.00364,
						 'r_0913__kmp_s_1096r_0913': 0.549,
						 'r_1027__kms_s_1434_br_1027': 0.549,
						 'r_0306__kms_s_0330r_0306': 0.549,
						 'r_1812__a_s_0619r_1812': 0.003587,
						 'r_0336__kmp_s_0400r_0336': 1.71907,
						 'r_0336__Keq_r_0336': 0.521887,
						 'r_0423__kmp_s_1329r_0423': 0.549,
						 'r_0630__kms_s_1091r_0630': 0.549,
						 'r_1157__Keq_r_1157': 1.0,
						 'r_1007__Vmax_r_1007': 0.624362,
						 'r_0111__Vmax_r_0111': 3.41221,
						 'r_0970__kms_s_0763_br_0970': 0.549,
						 'r_0059__Keq_r_0059': 34.7263,
						 'r_0538__Keq_r_0538': 0.063468,
						 'r_1812__a_s_0416r_1812': 0.023371,
						 'r_1007__Keq_r_1007': 0.639881,
						 'r_0715__kmp_s_0400r_0715': 1.71907,
						 'r_0014__Keq_r_0014': 2.00364,
						 'r_0765__kmp_s_0181r_0765': 0.549,
						 'r_0418__kmp_s_1434_br_0418': 0.549,
						 'r_1027__kmp_s_1207r_1027': 0.549,
						 'r_0510__kms_s_1087r_0510': 0.0867353,
						 'r_0949__Vmax_r_0949': 0.00274998,
						 'r_0429__kmp_s_0582r_0429': 0.549,
						 'r_0339__kms_s_0888r_0339': 0.549,
						 'r_0937__kmp_s_1156r_0937': 0.549,
						 'r_0026__Keq_r_0026': 1.1,
						 'r_0793__kmp_s_1155r_0793': 0.549,
						 'r_0026__Vmax_r_0026': 2.2935,
						 'r_0853__kmp_s_0763_br_0853': 0.549,
						 'r_1812__a_s_0939r_1812': 0.12864,
						 'r_0573__Vmax_r_0573': 1.99579,
						 'r_0972__kms_s_1187r_0972': 0.549,
						 'r_0429__kms_s_1140r_0429': 0.549,
						 'r_1293__Keq_r_1293': 1.0,
						 'r_0171__Keq_r_0171': 1.38552,
						 'r_0995__kmp_s_0641r_0995': 0.549,
						 'r_0859__Keq_r_0859': 12.2086,
						 'r_0865__Vmax_r_0865': 94.7102,
						 'r_1066__kmp_s_0446r_1066': 1.09208,
						 'r_0485__Vmax_r_0485': 2.08449,
						 'r_0068__Keq_r_0068': 22.2765,
						 'r_0031__kms_s_0763_br_0031': 0.549,
						 'r_0831__kmp_s_1290r_0831': 0.549,
						 'r_0265__Keq_r_0265': 2.00364,
						 'r_0660__kmp_s_1096r_0660': 0.549,
						 'r_0882__Vmax_r_0882': 0.504568,
						 'r_1072__kmp_s_1415r_1072': 0.549,
						 'r_0375__Vmax_r_0375': 0.0240791,
						 'r_0720__Keq_r_0720': 0.6039,
						 'r_0660__Keq_r_0660': 0.331541,
						 'r_0969__kmp_s_0185r_0969': 0.549,
						 'r_0702__kms_s_0917r_0702': 0.549,
						 'r_0031__kmp_s_0297r_0031': 0.549,
						 'r_0042__kms_s_0216r_0042': 0.549,
						 'r_0340__kmp_s_0888r_0340': 0.549,
						 'r_0568__Keq_r_0568': 1.1,
						 'r_0604__kmp_s_0899r_0604': 0.549,
						 'r_1812__a_s_0593r_1812': 0.002432,
						 'r_0417__kmp_s_0514r_0417': 0.549,
						 'r_0515__kmp_s_0400r_0515': 1.71907,
						 'r_0722__Keq_r_0722': 0.6039,
						 'r_0568__Vmax_r_0568': 0.0076692,
						 'r_0464__kms_s_0582r_0464': 0.549,
						 'r_0421__kmp_s_1434_br_0421': 0.549,
						 'r_0530__kmp_s_1315r_0530': 12.8511,
						 'r_1812__s_0899_or_1812': 0.549,
						 'r_1507__Keq_r_1507': 1.0,
						 'r_1816__a_s_0627r_1816': 9.6e-05,
						 'r_0604__kms_s_0907r_0604': 0.549,
						 'r_0976__kms_s_0763_br_0976': 0.549,
						 'r_0630__kmp_s_0470r_0630': 1.0,
						 'r_0779__kms_s_0446r_0779': 1.09208,
						 'r_0268__kmp_s_1434_br_0268': 0.549,
						 'r_0258__Keq_r_0258': 2.00364,
						 'r_0466__kmp_s_1434_br_0466': 0.549,
						 'r_0442__kmp_s_1132r_0442': 0.549,
						 'r_0586__Keq_r_0586': 34.7263,
						 'r_1293__Vmax_r_1293': 2.36101,
						 'r_0238__kmp_s_0886r_0238': 0.549,
						 'r_0889__kms_s_1048r_0889': 0.549,
						 'r_0157__kmp_s_0434r_0157': 1.25956,
						 'r_0264__kmp_s_1447r_0264': 0.549,
						 'r_0728__kms_s_1070r_0728': 0.549,
						 'r_0607__Vmax_r_0607': 0.501598,
						 'r_0608__kmp_s_1434_br_0608': 0.549,
						 'r_1812__s_0960_or_1812': 1.0,
						 'r_0890__Keq_r_0890': 0.950614,
						 'r_0479__kmp_s_0122r_0479': 0.549,
						 'r_0610__kmp_s_0763_br_0610': 0.549,
						 'r_0031__kms_s_0010r_0031': 0.549,
						 'r_0647__kmp_s_0863r_0647': 0.549,
						 'r_0510__kms_s_0763_br_0510': 0.549,
						 'r_0779__kms_s_1411r_0779': 0.549,
						 'r_0938__kmp_s_0366r_0938': 0.120104,
						 'r_0165__kmp_s_0434r_0165': 1.25956,
						 'r_0258__kmp_s_0124r_0258': 0.549,
						 'r_1036__kms_s_0731r_1036': 0.0436363,
						 'r_0336__kmp_s_1207r_0336': 0.549,
						 'r_1812__a_s_0929r_1812': 0.23942,
						 'r_1040__kms_s_1434_br_1040': 0.549,
						 'r_0442__Vmax_r_0442': 0.001914,
						 'r_0698__kmp_s_0554r_0698': 0.549,
						 'r_0598__kmp_s_0031r_0598': 0.549,
						 'r_0712__kmp_s_0481r_0712': 0.549,
						 'r_0701__kms_s_1434_br_0701': 0.549,
						 'r_0728__kms_s_1096r_0728': 0.549,
						 'r_0042__Vmax_r_0042': 0.731496,
						 'r_0588__kmp_s_0400r_0588': 1.71907,
						 'r_0701__Keq_r_0701': 0.552982,
						 'r_0650__kmp_s_0605r_0650': 0.549,
						 'r_0018__kmp_s_0861r_0018': 0.549,
						 'r_0585__Keq_r_0585': 0.0348439,
						 'r_0697__kms_s_0763_br_0697': 0.549,
						 'r_0856__kmp_s_0397r_0856': 0.549,
						 'r_0722__kms_s_1091r_0722': 0.549,
						 'r_0977__kmp_s_0763_br_0977': 0.549,
						 'r_0339__kmp_s_0430r_0339': 0.549,
						 'r_0465__kmp_s_1044r_0465': 0.549,
						 'r_0499__kms_s_0545r_0499': 0.0987587,
						 'r_0861__Keq_r_0861': 1.1,
						 'r_0765__kms_s_0763_br_0765': 0.549,
						 'r_0667__Vmax_r_0667': 0.196349,
						 'r_1812__a_s_0889r_1812': 0.04288,
						 'r_0496__kmp_s_0605r_0496': 0.549,
						 'r_0163__kmp_s_0434r_0163': 1.25956,
						 'r_0794__kms_s_0763_br_0794': 0.549,
						 'r_0479__Keq_r_0479': 1.73154,
						 'r_0467__kmp_s_0470r_0467': 1.0,
						 'r_0425__kms_s_1005r_0425': 0.549,
						 'r_1050__kms_s_0899r_1050': 0.549,
						 'r_0873__kms_s_1293r_0873': 0.549,
						 'r_0883__kmp_s_0318r_0883': 0.549,
						 'r_0270__Vmax_r_0270': 0.00017589,
						 'r_0014__Vmax_r_0014': 0.00605002,
						 'r_0938__Vmax_r_0938': 62.986,
						 'r_0467__Vmax_r_0467': 0.00599719,
						 'r_0618__kms_s_1013r_0618': 0.549,
						 'r_0618__Keq_r_0618': 2.00364,
						 'r_0888__kmp_s_0763_br_0888': 0.549,
						 'r_0660__kmp_s_0763_br_0660': 0.549,
						 'r_0859__kms_s_0539r_0859': 0.104555,
						 'r_0059__kms_s_0254r_0059': 0.549,
						 'r_0667__kmp_s_0430r_0667': 0.549,
						 'r_1812__a_s_0434r_1812': 0.051,
						 'r_0969__kmp_s_0763_br_0969': 0.549,
						 'r_0512__kms_s_1087r_0512': 0.0867353,
						 'r_0249__kms_s_0446r_0249': 1.09208,
						 'r_0068__kmp_s_1207r_0068': 0.549,
						 'r_0577__Keq_r_0577': 1.1,
						 'r_0936__kms_s_0120r_0936': 0.549,
						 'r_0246__kms_s_0400r_0246': 1.71907,
						 'r_0976__kms_s_0217r_0976': 0.549,
						 'r_0058__kms_s_0257r_0058': 0.549,
						 'r_0174__Keq_r_0174': 0.121402,
						 'r_0421__kmp_s_0514r_0421': 0.549,
						 'r_0284__kms_s_0763_br_0284': 0.549,
						 'r_0674__kms_s_0899r_0674': 0.549,
						 'r_0661__kmp_s_1082r_0661': 1.50326,
						 'r_0970__kmp_s_1091r_0970': 0.549,
						 'r_0993__kmp_s_1091r_0993': 0.549,
						 'r_0791__kms_s_1051r_0791': 0.549,
						 'r_0284__kms_s_0521r_0284': 0.549,
						 'r_1812__a_s_0955r_1812': 0.096481,
						 'r_0133__kms_s_0149r_0133': 0.549,
						 'r_0417__kms_s_1132r_0417': 0.549,
						 'r_0525__kms_s_1207r_0525': 0.549,
						 'r_1024__kms_s_1517r_1024': 0.549,
						 'r_0853__kmp_s_1219r_0853': 0.549,
						 'r_0882__Keq_r_0882': 0.6039,
						 'r_0965__kms_s_0561r_0965': 0.549,
						 'r_0261__kmp_s_0470r_0261': 1.0,
						 'r_0060__Keq_r_0060': 34.7263,
						 'r_0336__Vmax_r_0336': 0.703339,
						 'r_0026__kmp_s_0514r_0026': 0.549,
						 'r_0647__kmp_s_0185r_0647': 0.549,
						 'r_0791__Keq_r_0791': 1.1,
						 'r_0512__kms_s_0763_br_0512': 0.549,
						 'r_0586__kmp_s_1082r_0586': 1.50326,
						 'r_0057__kms_s_1087r_0057': 0.0867353,
						 'r_0387__kmp_s_0712r_0387': 0.549,
						 'r_0287__kmp_s_1060r_0287': 0.549,
						 'r_0963__Vmax_r_0963': 0.5544,
						 'r_0464__kmp_s_1091r_0464': 0.549,
						 'r_0467__kms_s_1187r_0467': 0.549,
						 'r_0957__kms_s_1521r_0957': 0.549,
						 'r_0889__kmp_s_0763_br_0889': 0.549,
						 'r_0534__kmp_s_0083r_0534': 0.549,
						 'r_0874__kmp_s_1290r_0874': 0.549,
						 'r_1812__s_0593_or_1812': 0.549,
						 'r_0847__Keq_r_0847': 0.331541,
						 'r_0040__Keq_r_0040': 0.331541,
						 'r_0064__kmp_s_0010r_0064': 0.549,
						 'r_0771__kmp_s_0481r_0771': 0.549,
						 'r_0025__kmp_s_1434_br_0025': 0.549,
						 'r_0582__kmp_s_0763_br_0582': 0.549,
						 'r_0496__Vmax_r_0496': 0.058597,
						 'r_0505__Keq_r_0505': 0.29,
						 'r_0886__kmp_s_0400r_0886': 1.71907,
						 'r_0235__Vmax_r_0235': 9.856,
						 'r_1816__s_0090_or_1816': 0.549,
						 'r_0268__Keq_r_0268': 3.64962,
						 'r_0873__kmp_s_1290r_0873': 0.549,
						 'r_0771__Vmax_r_0771': 0.014553,
						 'r_0604__kmp_s_0532r_0604': 0.549,
						 'r_0304__Vmax_r_0304': 0.3861,
						 'r_1040__kmp_s_0596r_1040': 0.549,
						 'r_0875__Keq_r_0875': 1.1,
						 'r_0235__kmp_s_0881r_0235': 0.549,
						 'r_0026__kms_s_0380r_0026': 0.549,
						 'r_1032__kms_s_0307r_1032': 0.549,
						 'r_0226__kmp_s_0763_br_0226': 0.549,
						 'r_1816__a_s_0641r_1816': 0.000812,
						 'r_0650__kmp_s_1082r_0650': 1.50326,
						 'r_0183__Keq_r_0183': 14456.7,
						 'r_0170__Vmax_r_0170': 1.8216,
						 'r_0267__kms_s_1456r_0267': 0.549,
						 'r_0528__kms_s_1434_br_0528': 0.549,
						 'r_0423__kmp_s_1091r_0423': 0.549,
						 'r_0437__kms_s_0514r_0437': 0.549,
						 'r_0015__kmp_s_0146r_0015': 0.549,
						 'r_1059__kmp_s_0400r_1059': 1.71907,
						 'r_0701__kms_s_0933r_0701': 0.549,
						 'r_0042__kmp_s_0217r_0042': 0.549,
						 'r_1816__V_o': 0.0555,
						 'r_1812__a_s_0952r_1812': 0.028,
						 'r_0429__Vmax_r_0429': 0.0179399,
						 'r_1037__kmp_s_0561r_1037': 0.549,
						 'r_0381__kmp_s_0064r_0381': 0.549,
						 'r_0771__kms_s_0400r_0771': 1.71907,
						 'r_0430__kms_s_1005r_0430': 0.549,
						 'r_0539__kms_s_0307r_0539': 0.549,
						 'r_0360__kms_s_0400r_0360': 1.71907,
						 'r_0464__Vmax_r_0464': 0.0179399,
						 'r_0387__Vmax_r_0387': 0.058597,
						 'r_1036__kmp_s_0427r_1036': 0.549,
						 'r_0464__kmp_s_0977r_0464': 0.549,
						 'r_0882__kmp_s_0763_br_0882': 0.549,
						 'r_0825__Keq_r_0825': 1.1,
						 'r_0357__Vmax_r_0357': 0.0163349,
						 'r_0351__kms_s_0763_br_0351': 0.549,
						 'r_0940__kmp_s_1087r_0940': 0.0867353,
						 'r_0043__Vmax_r_0043': 0.731496,
						 'r_0913__Keq_r_0913': 1.1,
						 'r_0707__kmp_s_1096r_0707': 0.549,
						 'r_0528__kms_s_1315r_0528': 12.8511,
						 'r_0370__kms_s_0596r_0370': 0.549,
						 'r_0509__kms_s_1096r_0509': 0.549,
						 'r_0509__kmp_s_0899r_0509': 0.549,
						 'r_0232__kms_s_0469r_0232': 0.549,
						 'r_0387__Keq_r_0387': 1.1,
						 'r_0515__kmp_s_1207r_0515': 0.549,
						 'r_0701__Vmax_r_0701': 0.141075,
						 'r_0267__Keq_r_0267': 2.00364,
						 'r_0886__kms_s_0318r_0886': 0.549,
						 'r_0967__kmp_s_0763_br_0967': 0.549,
						 'r_0419__kms_s_1096r_0419': 0.549,
						 'r_0282__kmp_s_1160r_0282': 0.549,
						 'r_0633__Keq_r_0633': 0.6039,
						 'r_0063__kmp_s_0008r_0063': 0.549,
						 'r_1040__kms_s_1399r_1040': 0.549,
						 'r_0499__kmp_s_0455r_0499': 0.496414,
						 'r_0064__kmp_s_0763_br_0064': 0.549,
						 'r_0437__kms_s_0446r_0437': 1.09208,
						 'r_0715__kmp_s_1207r_0715': 0.549,
						 'r_0977__Vmax_r_0977': 1.60929,
						 'r_0661__Keq_r_0661': 63.2537,
						 'r_0504__kms_s_0455r_0504': 0.496414,
						 'r_0251__kmp_s_0763_br_0251': 0.549,
						 'r_0370__kmp_s_0514r_0370': 0.549,
						 'r_0060__kms_s_1087r_0060': 0.0867353,
						 'r_0723__Vmax_r_0723': 0.00127051,
						 'r_0585__kmp_s_0763_br_0585': 0.549,
						 'r_0430__kms_s_0380r_0430': 0.549,
						 'r_1037__Keq_r_1037': 72.6682,
						 'r_1816__s_1399_or_1816': 0.549,
						 'r_1812__a_s_0925r_1812': 0.25014,
						 'r_0976__kmp_s_1306r_0976': 0.549,
						 'r_0232__kmp_s_0763_br_0232': 0.549,
						 'r_0419__kmp_s_0514r_0419': 0.549,
						 'r_0884__kmp_s_1207r_0884': 0.549,
						 'r_1812__s_1283_or_1812': 0.549,
						 'r_1037__kmp_s_0533r_1037': 0.549,
						 'r_0026__kms_s_0238r_0026': 0.549,
						 'r_0598__Keq_r_0598': 2.00364,
						 'r_0936__kmp_s_1091r_0936': 0.549,
						 'r_0699__kmp_s_0763_br_0699': 0.549,
						 'r_0965__Keq_r_0965': 1.1,
						 'r_1037__kms_s_0731r_1037': 0.0436363,
						 'r_1507__Vmax_r_1507': 0.0190579,
						 'r_0547__kms_s_1434_br_0547': 0.549,
						 'r_0262__kmp_s_1087r_0262': 0.0867353,
						 'r_0419__Vmax_r_0419': 0.00599719,
						 'r_0063__Keq_r_0063': 2.00364,
						 'r_0267__kmp_s_1434_br_0267': 0.549,
						 'r_0865__kms_s_0400r_0865': 1.71907,
						 'r_0831__kmp_s_0763_br_0831': 0.549,
						 'r_0568__kmp_s_0562r_0568': 0.549,
						 'r_0429__kmp_s_0470r_0429': 1.0,
						 'r_0174__kms_s_0863r_0174': 0.549,
						 'r_0573__kms_s_0545r_0573': 0.0987587,
						 'r_0235__kmp_s_0185r_0235': 0.549,
						 'r_0959__Vmax_r_0959': 0.0120516,
						 'r_0506__kms_s_0899r_0506': 0.549,
						 'r_0789__kmp_s_1207r_0789': 0.549,
						 'r_0251__kms_s_0470r_0251': 1.0,
						 'r_0287__Keq_r_0287': 2.00364,
						 'r_0031__Vmax_r_0031': 1.0703,
						 'r_1059__Vmax_r_1059': 0.23947,
						 'r_0385__kmp_s_0058r_0385': 0.549,
						 'r_0991__kms_s_0763_br_0991': 0.549,
						 'r_0831__Vmax_r_0831': 0.0193599,
						 'r_0504__Vmax_r_0504': 6.56505,
						 'r_0245__kms_s_0446r_0245': 1.09208,
						 'r_0370__kmp_s_1399r_0370': 0.549,
						 'r_0417__kmp_s_1434_br_0417': 0.549,
						 'r_0284__kmp_s_0485r_0284': 0.549,
						 'r_0598__kms_s_1096r_0598': 0.549,
						 'r_1812__s_0955_or_1812': 0.549,
						 'r_0886__Keq_r_0886': 0.950614,
						 'r_0576__Vmax_r_0576': 0.32109,
						 'r_0598__kms_s_0225r_0598': 0.549,
						 'r_0264__Vmax_r_0264': 0.0454962,
						 'r_0127__kmp_s_0514r_0127': 0.549,
						 'r_0886__kmp_s_0009r_0886': 0.549,
						 'r_0466__Keq_r_0466': 3.64962,
						 'r_1816__a_s_0963r_1816': 3.2e-05,
						 'r_0261__kmp_s_0763_br_0261': 0.549,
						 'r_0940__kms_s_1082r_0940': 1.50326,
						 'r_0118__Keq_r_0118': 1.1,
						 'r_0009__kms_s_0083r_0009': 0.549,
						 'r_0042__Keq_r_0042': 0.6039,
						 'r_0425__kms_s_0763_br_0425': 0.549,
						 'r_0393__Keq_r_0393': 1.1,
						 'r_1812__a_s_1011r_1812': 0.82099,
						 'r_1008__kmp_s_1434_br_1008': 0.549,
						 'r_0261__kms_s_1091r_0261': 0.549,
						 'r_0330__kmp_s_1434_br_0330': 0.549,
						 'r_0856__kmp_s_1517r_0856': 0.549,
						 'r_0715__kmp_s_0470r_0715': 1.0,
						 'r_0220__kmp_s_0605r_0220': 0.549,
						 'r_0287__kmp_s_1434_br_0287': 0.549,
						 'r_0885__Vmax_r_0885': 0.7854,
						 'r_0621__kms_s_0128r_0621': 0.549,
						 'r_0949__Keq_r_0949': 1.1,
						 'r_0439__kms_s_0605r_0439': 0.549,
						 'r_0093__kms_s_0307r_0093': 0.549,
						 'r_0577__kmp_s_0185r_0577': 0.549,
						 'r_0976__kms_s_1096r_0976': 0.549,
						 'r_1032__Vmax_r_1032': 0.015323,
						 'r_0941__kms_s_1243r_0941': 0.0271093,
						 'r_0630__kmp_s_1096r_0630': 0.549,
						 'r_0418__Keq_r_0418': 3.64962,
						 'r_0959__kmp_s_1517r_0959': 0.549,
						 'r_1007__kms_s_0763_br_1007': 0.549,
						 'r_1812__s_0936_or_1812': 0.549,
						 'r_0336__kms_s_1430r_0336': 0.549,
						 'r_1024__kmp_s_1091r_1024': 0.549,
						 'r_0060__kmp_s_1082r_0060': 1.50326,
						 'r_1816__s_0641_or_1816': 0.549,
						 'r_0831__Keq_r_0831': 0.6039,
						 'r_0889__kmp_s_0309r_0889': 0.549,
						 'r_0370__kmp_s_0763_br_0370': 0.549,
						 'r_0371__kms_s_1434_br_0371': 0.549,
						 'r_0970__kmp_s_0942r_0970': 0.549,
						 'r_0465__kms_s_0763_br_0465': 0.549,
						 'r_0514__kmp_s_0333r_0514': 0.549,
						 'r_0118__kmp_s_0514r_0118': 0.549,
						 'r_1024__Vmax_r_1024': 0.705433,
						 'r_0865__kms_s_0265r_0865': 0.000108759,
						 'r_0093__kms_s_0763_br_0093': 0.549,
						 'r_0466__kms_s_1096r_0466': 0.549,
						 'r_0233__kmp_s_0301r_0233': 0.549,
						 'r_0029__kmp_s_1434_br_0029': 0.549,
						 'r_0267__Vmax_r_0267': 0.0951282,
						 'r_0385__kms_s_0007r_0385': 0.549,
						 'r_0258__Vmax_r_0258': 0.0458592,
						 'r_0385__Vmax_r_0385': 0.523597,
						 'r_0267__kms_s_1096r_0267': 0.549,
						 'r_0268__Vmax_r_0268': 0.0951282,
						 'r_0290__kms_s_1325r_0290': 0.549,
						 'r_1066__kms_s_0400r_1066': 1.71907,
						 'r_1812__s_0743_or_1812': 0.549,
						 'r_0262__kmp_s_0215r_0262': 0.549,
						 'r_0430__Keq_r_0430': 40.2,
						 'r_0330__Vmax_r_0330': 4.40547,
						 'r_0467__kms_s_1096r_0467': 0.549,
						 'r_0957__Vmax_r_0957': 0.0404138,
						 'r_0163__Keq_r_0163': 0.512011,
						 'r_0934__kms_s_1434_br_0934': 0.549,
						 'r_0015__kms_s_0145r_0015': 0.549,
						 'r_0221__kmp_s_0439r_0221': 0.549,
						 'r_0509__kms_s_0185r_0509': 0.549,
						 'r_0861__kms_s_0410r_0861': 0.549,
						 'r_0442__kmp_s_0446r_0442': 1.09208,
						 'r_0345__kms_s_0481r_0345': 0.549,
						 'r_0437__Keq_r_0437': 1.26869,
						 'r_0604__kmp_s_0763_br_0604': 0.549,
						 'r_0934__Keq_r_0934': 1.1,
						 'r_0352__kmp_s_1096r_0352': 0.549,
						 'r_0005__Vmax_r_0005': 6.24684,
						 'r_0577__kmp_s_0916r_0577': 0.549,
						 'r_0941__Vmax_r_0941': 146.411,
						 'r_0528__Keq_r_0528': 0.0128394,
						 'r_1194__Keq_r_1194': 1.0,
						 'r_0866__kms_s_0264r_0866': 0.363388,
						 'r_1812__s_0952_or_1812': 1.0,
						 'r_0112__kms_s_0763_br_0112': 0.549,
						 'r_0384__Keq_r_0384': 0.6039,
						 'r_0991__kms_s_1160r_0991': 0.549,
						 'r_0728__kmp_s_1091r_0728': 0.549,
						 'r_0330__kmp_s_0501r_0330': 0.549,
						 'r_0277__kms_s_1434_br_0277': 0.549,
						 'r_0068__kms_s_0267r_0068': 0.549,
						 'r_0568__kmp_s_0706r_0568': 0.549,
						 'r_0229__kmp_s_0899r_0229': 0.549,
						 'r_0351__Vmax_r_0351': 3.30331,
						 'r_0026__kmp_s_0167r_0026': 0.549,
						 'r_1157__kms_s_0431_br_1157': 38.0,
						 'r_0232__Vmax_r_0232': 0.826427,
						 'r_0607__kmp_s_1087r_0607': 0.0867353,
						 'r_0660__kms_s_1091r_0660': 0.549,
						 'r_0529__kmp_s_0659r_0529': 0.549,
						 'r_1247__Vmax_r_1247': 4.81765,
						 'r_0064__kms_s_0008r_0064': 0.549,
						 'r_0890__Vmax_r_0890': 1.53571,
						 'r_0588__kmp_s_1122r_0588': 0.549,
						 'r_0936__Vmax_r_0936': 0.863944,
						 'r_0538__kmp_s_1087r_0538': 0.0867353,
						 'r_0417__Keq_r_0417': 3.64962,
						 'r_0551__kms_s_0306r_0551': 0.549,
						 'r_0582__kms_s_0380r_0582': 0.549,
						 'r_0439__kmp_s_0446r_0439': 1.09208,
						 'r_1812__a_s_0936r_1812': 0.11435,
						 'r_0111__Keq_r_0111': 2.00364,
						 'r_1040__Vmax_r_1040': 0.0043505,
						 'r_0853__Vmax_r_0853': 0.0266199,
						 'r_0339__kms_s_1434_br_0339': 0.549,
						 'r_0386__Vmax_r_0386': 5.48128,
						 'r_0515__kmp_s_0763_br_0515': 0.549,
						 'r_0630__kms_s_0847r_0630': 0.549,
						 'r_0674__kmp_s_0185r_0674': 0.549,
						 'r_0948__kms_s_0320r_0948': 0.549,
						 'r_0719__kms_s_0046r_0719': 0.549,
						 'r_0258__kmp_s_1091r_0258': 0.549,
						 'r_0530__Vmax_r_0530': 12.5841,
						 'r_0328__kmp_s_0514r_0328': 0.549,
						 'r_0514__kmp_s_0899r_0514': 0.549,
						 'r_0650__Keq_r_0650': 21.9885,
						 'r_0064__Vmax_r_0064': 1.68189,
						 'r_0967__Keq_r_0967': 0.6039,
						 'r_0386__kmp_s_0735r_0386': 0.601873,
						 'r_0715__Keq_r_0715': 0.950614,
						 'r_0977__kms_s_1306r_0977': 0.549,
						 'r_1812__a_s_0740r_1812': 0.32518,
						 'r_0307__kmp_s_0847r_0307': 0.549,
						 'r_0277__kms_s_0458r_0277': 0.549,
						 'r_0793__Keq_r_0793': 1.1,
						 'r_0425__Keq_r_0425': 40.2,
						 'r_0937__kmp_s_1207r_0937': 0.549,
						 'r_0599__kmp_s_0225r_0599': 0.549,
						 'r_1812__s_0925_or_1812': 0.549,
						 'r_0650__kms_s_1087r_0650': 0.0867353,
						 'r_0885__kmp_s_0325r_0885': 0.549,
						 'r_0889__Keq_r_0889': 0.6039,
						 'r_1816__a_s_0824r_1816': 0.000417,
						 'r_0951__Keq_r_0951': 0.192861,
						 'r_0213__kmp_s_1411r_0213': 0.549,
						 'r_0634__kmp_s_0920r_0634': 0.549,
						 'r_1812__s_0740_or_1812': 0.549,
						 'r_0125__Vmax_r_0125': 26.9831,
						 'r_0877__kmp_s_0400r_0877': 1.71907,
						 'r_0270__kms_s_0669r_0270': 0.549,
						 'r_0873__Keq_r_0873': 1.1,
						 'r_0576__kmp_s_1207r_0576': 0.549,
						 'r_0009__kmp_s_1215r_0009': 0.549,
						 'r_0888__Vmax_r_0888': 3.13818,
						 'r_0345__Vmax_r_0345': 0.19019,
						 'r_0856__kmp_s_1349r_0856': 0.549,
						 'r_0606__Vmax_r_0606': 0.560996,
						 'r_0352__kms_s_1091r_0352': 0.549,
						 'r_0970__kms_s_0899r_0970': 0.549,
						 'r_0991__kms_s_1087r_0991': 0.0867353,
						 'r_1461__kms_s_1209_br_1461': 24.5,
						 'r_0031__Keq_r_0031': 2.00364,
						 'r_0417__kmp_s_1091r_0417': 0.549,
						 'r_0575__kms_s_0915r_0575': 0.549,
						 'r_0282__Keq_r_0282': 0.6039,
						 'r_0265__Vmax_r_0265': 0.0951282,
						 'r_0941__kmp_s_0446r_0941': 1.09208,
						 'r_0949__kms_s_0335r_0949': 0.549,
						 'r_0287__kmp_s_1091r_0287': 0.549,
						 'r_1812__a_s_1417r_1812': 0.067,
						 'r_0467__kmp_s_1334r_0467': 0.549,
						 'r_0712__kmp_s_0022r_0712': 0.549,
						 'r_0277__Keq_r_0277': 0.821515,
						 'r_0884__kms_s_0158r_0884': 0.549,
						 'r_1003__kmp_s_1342r_1003': 0.549,
						 'r_0514__Keq_r_0514': 1.1,
						 'r_0374__kms_s_0064r_0374': 0.549,
						 'r_0634__kms_s_0058r_0634': 0.549,
						 'r_0213__Vmax_r_0213': 0.157299,
						 'r_0226__kms_s_0887r_0226': 0.549,
						 'r_0016__Keq_r_0016': 33.0686,
						 'r_0417__kms_s_1005r_0417': 0.549,
						 'r_0488__Keq_r_0488': 1.1,
						 'r_0384__Vmax_r_0384': 1.55099,
						 'r_0068__kms_s_1243r_0068': 0.0271093,
						 'r_0371__kms_s_1215r_0371': 0.549,
						 'r_0728__kms_s_0763_br_0728': 0.549,
						 'r_0264__kms_s_0763_br_0264': 0.549,
						 'r_0647__kms_s_0899r_0647': 0.549,
						 'r_0510__kmp_s_0899r_0510': 0.549,
						 'r_0347__kmp_s_0689r_0347': 0.549,
						 'r_0191__kmp_s_1096r_0191': 0.549,
						 'r_0221__kms_s_0500r_0221': 0.549,
						 'r_0586__Vmax_r_0586': 9.81316,
						 'r_0488__kms_s_0659r_0488': 0.549,
						 'r_0398__Vmax_r_0398': 6.15027,
						 'r_0881__Keq_r_0881': 2.00364,
						 'r_0352__kms_s_0530r_0352': 0.549,
						 'r_0793__kms_s_1154r_0793': 0.549,
						 'r_0328__kms_s_0380r_0328': 0.549,
						 'r_0496__Keq_r_0496': 1.1,
						 'r_0421__kms_s_1005r_0421': 0.549,
						 'r_1059__Keq_r_1059': 1.73154,
						 'r_0225__Vmax_r_0225': 0.414697,
						 'r_1812__a_s_0943r_1812': 0.25371,
						 'r_0499__kms_s_0446r_0499': 1.09208,
						 'r_0111__kms_s_0763_br_0111': 0.549,
						 'r_0171__kmp_s_0692r_0171': 0.549,
						 'r_0877__Keq_r_0877': 1.73154,
						 'r_0284__kms_s_1215r_0284': 0.549,
						 'r_1812__s_1011_or_1812': 0.549,
						 'r_0133__kmp_s_1051r_0133': 0.549,
						 'r_0568__kms_s_0752r_0568': 0.549,
						 'r_1008__kms_s_0763_br_1008': 0.549,
						 'extracellular': 1.0,
						 'r_1461__kms_s_0766_br_1461': 0.1,
						 'r_0191__Keq_r_0191': 2.76045,
						 'r_0577__Vmax_r_0577': 0.32109,
						 'r_0699__Keq_r_0699': 1.1,
						 'r_1024__kms_s_0763_br_1024': 0.549,
						 'r_0499__kmp_s_0763_br_0499': 0.549,
						 'r_1816__a_s_1219r_1816': 0.000373,
						 'r_0423__kms_s_1096r_0423': 0.549,
						 'r_0991__kms_s_1327r_0991': 0.549,
						 'r_0246__kms_s_0763_br_0246': 0.549,
						 'r_0967__kmp_s_0669r_0967': 0.549,
						 'r_0467__kmp_s_0514r_0467': 0.549,
						 'r_0847__kms_s_0485r_0847': 0.549,
						 'r_0865__kmp_s_0264r_0865': 0.363388,
						 'r_0394__kmp_s_0616r_0394': 0.549,
						 'r_0890__kms_s_0740r_0890': 0.549,
						 'r_0877__kms_s_0022r_0877': 0.549,
						 'r_0307__Keq_r_0307': 2.00364,
						 'r_0430__kmp_s_0514r_0430': 0.549,
						 'r_0913__kmp_s_0470r_0913': 1.0,
						 'r_0562__kms_s_1434_br_0562': 0.549,
						 'r_0506__kmp_s_0400r_0506': 1.71907,
						 'r_0673__Vmax_r_0673': 0.01254,
						 'r_0423__kmp_s_0514r_0423': 0.549,
						 'r_1435__Keq_r_1435': 1.0,
						 'r_0667__kms_s_0949r_0667': 1.0,
						 'r_0699__kms_s_0015r_0699': 0.549,
						 'r_0265__kms_s_0763_br_0265': 0.549,
						 'r_0157__Vmax_r_0157': 0.103455,
						 'r_0509__kms_s_0763_br_0509': 0.549,
						 'r_0429__kms_s_1005r_0429': 0.549,
						 'r_0418__kmp_s_0470r_0418': 1.0,
						 'r_0123__kmp_s_0400r_0123': 1.71907,
						 'r_0261__Vmax_r_0261': 0.0785835,
						 'r_0605__Keq_r_0605': 0.6039,
						 'r_0133__Vmax_r_0133': 0.58058,
						 'r_1042__kmp_s_0952r_1042': 1.0,
						 'r_0698__Vmax_r_0698': 1.5048,
						 'r_0562__kmp_s_0689r_0562': 0.549,
						 'r_0226__kmp_s_0434r_0226': 1.25956,
						 'r_0328__kms_s_1434_br_0328': 0.549,
						 'r_0865__kmp_s_0446r_0865': 1.09208,
						 'r_0991__Keq_r_0991': 34.7263,
						 'r_0271__kms_s_0632r_0271': 0.549,
						 'r_0266__kms_s_1096r_0266': 0.549,
						 'r_0034__kms_s_0397r_0034': 0.549,
						 'r_0063__kms_s_1434_br_0063': 0.549,
						 'r_0723__kmp_s_1013r_0723': 0.549,
						 'r_1816__s_1233_or_1816': 0.549,
						 'r_0336__kms_s_0446r_0336': 1.09208,
						 'r_0610__Keq_r_0610': 0.6039,
						 'r_0263__kms_s_1096r_0263': 0.549,
						 'r_0287__kms_s_1160r_0287': 0.549,
						 'r_1812__a_s_0863r_1812': 0.35734,
						 'r_0793__kms_s_0331r_0793': 0.549,
						 'r_0765__kms_s_0180r_0765': 0.549,
						 'r_0064__Keq_r_0064': 0.0348439,
						 'r_0371__kmp_s_0596r_0371': 0.549,
						 'r_0262__kmp_s_0763_br_0262': 0.549,
						 'r_0633__kms_s_0847r_0633': 0.549,
						 'r_0044__kmp_s_1325r_0044': 0.549,
						 'r_0170__Keq_r_0170': 0.331541,
						 'r_1816__a_s_0669r_1816': 0.000114,
						 'r_0673__Keq_r_0673': 1.1,
						 'r_0957__kmp_s_1517r_0957': 0.549,
						 'r_0352__Keq_r_0352': 0.6039,
						 'r_1672__kms_s_1342r_1672': 0.549,
						 'r_1812__a_s_0752r_1812': 0.051,
						 'r_0721__Vmax_r_0721': 3.30329,
						 'r_0526__kms_s_1091r_0526': 0.549,
						 'r_0191__kmp_s_0763_br_0191': 0.549,
						 'r_0381__Keq_r_0381': 1.1,
						 'r_0885__kms_s_0317r_0885': 0.549,
						 'r_0063__Vmax_r_0063': 0.764505,
						 'r_0529__kms_s_0657r_0529': 0.549,
						 'r_0417__kms_s_0763_br_0417': 0.549,
						 'r_0351__kms_s_1087r_0351': 0.0867353,
						 'r_0688__kms_s_0763_br_0688': 0.549,
						 'r_0172__kms_s_0304r_0172': 0.549,
						 'r_0969__Keq_r_0969': 0.0348439,
						 'r_0479__kms_s_0446r_0479': 1.09208,
						 'r_0847__kmp_s_0090r_0847': 0.549,
						 'r_0509__Vmax_r_0509': 38.2031,
						 'r_1503__kmp_s_1339_br_1503': 1.0,
						 'r_1293__kms_s_0547_br_1293': 11.1,
						 'r_0529__kms_s_1315r_0529': 12.8511,
						 'r_0911__Vmax_r_0911': 0.768347,
						 'r_0111__kmp_s_1091r_0111': 0.549,
						 'r_0720__kms_s_0052r_0720': 0.549,
						 'r_0040__kmp_s_0689r_0040': 0.549,
						 'r_0277__kms_s_0907r_0277': 0.549,
						 'r_0722__Vmax_r_0722': 3.30329,
						 'r_0165__Vmax_r_0165': 4.0656,
						 'r_0608__Keq_r_0608': 1.1,
						 'r_0130__Keq_r_0130': 1.73154,
						 'r_0394__kmp_s_1011r_0394': 0.549,
						 'r_0006__kms_s_0438r_0006': 0.549,
						 'r_0044__kms_s_0763_br_0044': 0.549,
						 'r_0371__Vmax_r_0371': 0.00525138,
						 'r_0374__kms_s_1160r_0374': 0.549,
						 'r_0245__kmp_s_0605r_0245': 0.549,
						 'r_0789__kms_s_0469r_0789': 0.549,
						 'r_1816__s_0627_or_1816': 0.549,
						 'r_0890__kmp_s_1048r_0890': 0.549,
						 'r_0726__Keq_r_0726': 1.1,
						 'r_0528__kmp_s_0732r_0528': 0.15,
						 'r_0512__kmp_s_1207r_0512': 0.549,
						 'r_0423__kms_s_1005r_0423': 0.549,
						 'r_0417__Vmax_r_0417': 0.00599719,
						 'r_0873__kms_s_1225r_0873': 0.549,
						 'r_0130__kms_s_0446r_0130': 1.09208,
						 'r_0504__Keq_r_0504': 0.29,
						 'r_0505__kms_s_0410r_0505': 0.549,
						 'r_0040__kmp_s_0763_br_0040': 0.549,
						 'r_0362__kmp_s_0446r_0362': 1.09208,
						 'r_0948__Vmax_r_0948': 0.0120878,
						 'r_0581__kms_s_1434_br_0581': 0.549,
						 'r_0127__kms_s_0605r_0127': 0.549,
						 'r_0386__kmp_s_0400r_0386': 1.71907,
						 'r_0123__kmp_s_0763_br_0123': 0.549,
						 'r_0881__kmp_s_0079r_0881': 0.549,
						 'r_0328__Keq_r_0328': 1.1,
						 'r_0398__kmp_s_1434_br_0398': 0.549,
						 'r_0267__kmp_s_1457r_0267': 0.549,
						 'r_0015__kms_s_1096r_0015': 0.549,
						 'r_0226__Keq_r_0226': 0.696513,
						 'r_1812__a_s_0949r_1812': 0.19653,
						 'r_0328__kmp_s_0507r_0328': 0.549,
						 'r_0967__kms_s_1447r_0967': 0.549,
						 'r_0673__kmp_s_0963r_0673': 0.549,
						 'r_0347__kmp_s_1434_br_0347': 0.549,
						 'r_0582__kms_s_0185r_0582': 0.549,
						 'r_0174__kms_s_0749r_0174': 0.549,
						 'r_0229__Vmax_r_0229': 4.92183,
						 'r_0340__kms_s_0889r_0340': 0.549,
						 'r_0688__kms_s_1087r_0688': 0.0867353,
						 'r_0263__kmp_s_0302r_0263': 0.549,
						 'r_1072__kms_s_1430r_1072': 0.549,
						 'r_0723__kms_s_0828r_0723': 0.549,
						 'r_0233__Keq_r_0233': 1.73154,
						 'r_0621__kms_s_1060r_0621': 0.549,
						 'r_0525__Vmax_r_0525': 18.45,
						 'r_0688__Vmax_r_0688': 4.58593,
						 'r_0093__Keq_r_0093': 3.64962,
						 'r_0016__kms_s_0183r_0016': 0.549,
						 'r_0263__kms_s_0763_br_0263': 0.549,
						 'r_1003__kms_s_0514r_1003': 0.549,
						 'r_0008__Vmax_r_0008': 0.13761,
						 'r_0163__Vmax_r_0163': 2.28799,
						 'r_1435__kmp_s_1160r_1435': 0.549,
						 'r_0941__kms_s_0763_br_0941': 0.549,
						 'r_0093__Vmax_r_0093': 0.439232,
						 'r_1036__Keq_r_1036': 13.8394,
						 'r_0991__kmp_s_1434_br_0991': 0.549,
						 'r_0948__Keq_r_0948': 0.331541,
						 'r_0123__kmp_s_1207r_0123': 0.549,
						 'r_0697__kmp_s_0710r_0697': 0.549,
						 'r_0338__Keq_r_0338': 1.1,
						 'r_0525__kms_s_0731r_0525': 0.0436363,
						 'r_0044__kms_s_1096r_0044': 0.549,
						 'r_0183__kmp_s_0650r_0183': 50.0,
						 'r_0621__Keq_r_0621': 2.00364,
						 'r_0605__kmp_s_1434_br_0605': 0.549,
						 'r_1050__kmp_s_0185r_1050': 0.549,
						 'r_0783__Keq_r_0783': 0.6039,
						 'r_0789__kmp_s_0763_br_0789': 0.549,
						 'r_0630__Keq_r_0630': 1.1,
						 'r_1035__kmp_s_0731r_1035': 0.0436363,
						 'r_0963__kms_s_0557r_0963': 0.549,
						 'r_1024__kmp_s_1521r_1024': 0.549,
						 'r_1816__a_s_0632r_1816': 0.000125,
						 'r_0598__Vmax_r_0598': 0.3762,
						 'r_1816__a_s_0663r_1816': 0.000206,
						 'r_0484__kms_s_0537r_0484': 1.34278,
						 'r_0970__kms_s_0867r_0970': 0.549,
						 'r_0015__kms_s_0763_br_0015': 0.549,
						 'r_1812__s_0939_or_1812': 0.549,
						 'r_0229__kmp_s_0434r_0229': 1.25956,
						 'r_1003__Keq_r_1003': 1.73154,
						 'r_0442__kms_s_0434r_0442': 1.25956,
						 'r_0159__Vmax_r_0159': 0.065835,
						 'r_0640__Keq_r_0640': 2.00364,
						 'r_0850__kmp_s_1233r_0850': 0.549,
						 'r_1041__kms_s_0735r_1041': 0.601873,
						 'r_0271__kms_s_1096r_0271': 0.549,
						 'r_0589__kmp_s_1117r_0589': 0.549,
						 'r_0887__kmp_s_0078r_0887': 0.549,
						 'r_0887__Keq_r_0887': 1.1,
						 'r_0298__kmp_s_0632r_0298': 0.549,
						 'r_0465__kmp_s_0514r_0465': 0.549,
						 'r_0539__kms_s_1434_br_0539': 0.549,
						 'r_0268__kms_s_1096r_0268': 0.549,
						 'r_0698__Keq_r_0698': 5.77591,
						 'r_0794__kms_s_1155r_0794': 0.549,
						 'r_0266__kmp_s_1456r_0266': 0.549,
						 'r_0014__kmp_s_0430r_0014': 0.549,
						 'r_1037__kms_s_0539r_1037': 0.104555,
						 'r_1026__kmp_s_0366r_1026': 0.120104,
						 'r_0650__Vmax_r_0650': 4.53532,
						 'r_0551__kmp_s_0763_br_0551': 0.549,
						 'r_0249__kmp_s_0400r_0249': 1.71907,
						 'r_0018__Vmax_r_0018': 1.0241,
						 'r_0425__kms_s_1329r_0425': 0.549,
						 'r_0226__kmp_s_0017r_0226': 0.549,
						 'r_0575__kmp_s_0763_br_0575': 0.549,
						 'r_1035__kmp_s_1304r_1035': 0.549,
						 'r_0040__Vmax_r_0040': 0.00989001,
						 'r_0647__Keq_r_0647': 9.96691,
						 'r_0464__kms_s_1005r_0464': 0.549,
						 'r_0650__kms_s_0446r_0650': 1.09208,
						 'r_1503__kmp_s_0766_br_1503': 0.1,
						 'r_0165__kms_s_0400r_0165': 1.71907,
						 'r_0850__kms_s_1219r_0850': 0.549,
						 'r_0661__kms_s_1087r_0661': 0.0867353,
						 'r_1812__s_0889_or_1812': 0.549,
						 'r_0021__Keq_r_0021': 40.5765,
						 'r_0183__kmp_s_1082r_0183': 1.50326,
						 'r_0347__kms_s_1160r_0347': 0.549,
						 'r_0005__kmp_s_0763_br_0005': 0.549,
						 'r_1816__a_s_0124r_1816': 5.6e-05,
						 'r_0783__kms_s_0805r_0783': 0.549,
						 'r_0266__Keq_r_0266': 1.1,
						 'r_0993__kms_s_0195r_0993': 0.549,
						 'r_1008__Vmax_r_1008': 0.851402,
						 'r_0290__kmp_s_0763_br_0290': 0.549,
						 'r_1007__kms_s_0400r_1007': 1.71907,
						 'r_1812__s_0949_or_1812': 1.0,
						 'r_0938__Keq_r_0938': 3.97167,
						 'r_0886__kms_s_0446r_0886': 1.09208,
						 'r_0667__kmp_s_0183r_0667': 0.549,
						 'r_0265__kmp_s_1455r_0265': 0.549,
						 'r_0171__kms_s_1053r_0171': 0.549,
						 'r_0877__kms_s_0446r_0877': 1.09208,
						 'r_1461__kmp_s_1207r_1461': 0.549,
						 'r_0886__kmp_s_0763_br_0886': 0.549,
						 'r_0515__Keq_r_0515': 0.950614,
						 'r_0699__kmp_s_0122r_0699': 0.549,
						 'r_1050__Keq_r_1050': 1.1,
						 'r_0884__kmp_s_0763_br_0884': 0.549,
						 'r_0484__Keq_r_0484': 0.045,
						 'r_0510__kms_s_0185r_0510': 0.549,
						 'r_0647__kms_s_1277r_0647': 0.0605905,
						 'r_0271__Vmax_r_0271': 0.0430762,
						 'r_0225__Keq_r_0225': 0.6039,
						 'r_0606__kms_s_0325r_0606': 0.549,
						 'r_0551__kms_s_0446r_0551': 1.09208,
						 'r_0995__Keq_r_0995': 1.1,
						 'r_0547__kmp_s_0763_br_0547': 0.549,
						 'r_0791__Vmax_r_0791': 0.58058,
						 'r_0576__kms_s_1434_br_0576': 0.549,
						 'r_1812__s_1347_or_1812': 0.549,
						 'r_0874__kms_s_1293r_0874': 0.549,
						 'r_1008__kms_s_1096r_1008': 0.549,
						 'r_0955__kmp_s_0591r_0955': 0.549,
						 'r_0547__kmp_s_0438r_0547': 0.549,
						 'r_0969__kmp_s_1087r_0969': 0.0867353,
						 'r_0701__kmp_s_1293r_0701': 0.549,
						 'r_1812__s_0001_or_1812': 0.549,
						 'r_0847__Vmax_r_0847': 0.010285,
						 'r_0937__Keq_r_0937': 8.61335,
						 'r_0393__kmp_s_0615r_0393': 0.549,
						 'r_0306__kmp_s_0500r_0306': 0.549,
						 'r_0127__Vmax_r_0127': 25.905,
						 'r_0856__Keq_r_0856': 0.182016,
						 'r_0913__kms_s_1258r_0913': 0.549,
						 'r_1812__s_0873_or_1812': 0.549,
						 'r_1042__kmp_s_0731r_1042': 0.0436363,
						 'r_0421__kms_s_0763_br_0421': 0.549,
						 'r_0721__kms_s_1091r_0721': 0.549,
						 'r_0721__kmp_s_0254r_0721': 0.549,
						 'r_0647__Vmax_r_0647': 3.2494,
						 'r_0419__kms_s_1005r_0419': 0.549,
						 'r_0715__kms_s_0021r_0715': 0.549,
						 'r_0890__kms_s_0333r_0890': 0.549,
						 'r_0127__kms_s_0380r_0127': 0.549,
						 'r_0888__kmp_s_1207r_0888': 0.549,
						 'r_0347__kmp_s_0268r_0347': 0.549,
						 'r_0972__kmp_s_0218r_0972': 0.549,
						 'r_0581__kms_s_0468r_0581': 0.549,
						 'r_0157__kms_s_0393r_0157': 0.549,
						 'r_0371__Keq_r_0371': 0.331541,
						 'r_0589__kmp_s_0514r_0589': 0.549,
						 'r_0265__kms_s_1160r_0265': 0.549,
						 'r_0298__kmp_s_0763_br_0298': 0.549,
						 'r_1816__a_s_0635r_1816': 0.005603,
						 'r_0604__Keq_r_0604': 0.331541,
						 'r_0442__kmp_s_0514r_0442': 0.549,
						 'r_0969__Vmax_r_0969': 3.3649,
						 'r_0005__Keq_r_0005': 0.331541,
						 'r_0977__kms_s_0446r_0977': 1.09208,
						 'r_0021__Vmax_r_0021': 1.60931,
						 'r_0995__kms_s_0663r_0995': 0.549,
						 'r_0959__kms_s_1521r_0959': 0.549,
						 'r_0266__kms_s_0763_br_0266': 0.549,
						 'r_0021__kmp_s_0356r_0021': 0.549,
						 'r_0387__kms_s_1257r_0387': 0.549,
						 'r_0015__kmp_s_1091r_0015': 0.549,
						 'r_0723__Keq_r_0723': 2.00364,
						 'r_0421__kmp_s_0470r_0421': 1.0,
						 'r_0573__kmp_s_0410r_0573': 0.549,
						 'r_0667__Keq_r_0667': 0.331541,
						 'r_0604__Vmax_r_0604': 0.871524,
						 'r_0485__Keq_r_0485': 0.6039,
						 'r_0589__kms_s_0380r_0589': 0.549,
						 'r_0948__kmp_s_1207r_0948': 0.549,
						 'r_0258__kms_s_0268r_0258': 0.549,
						 'r_0339__kmp_s_0183r_0339': 0.549,
						 'r_0630__kmp_s_0185r_0630': 0.549,
						 'r_0865__Keq_r_0865': 2334.85,
						 'r_0484__kmp_s_0735r_0484': 0.601873,
						 'r_0715__kms_s_0446r_0715': 1.09208,
						 'r_0393__Vmax_r_0393': 3.5112,
						 'r_0064__kmp_s_1087r_0064': 0.0867353,
						 'r_1812__s_0434_or_1812': 1.25956,
						 'r_0235__kms_s_1156r_0235': 0.549,
						 'r_0538__kms_s_0309r_0538': 0.549,
						 'r_0608__kms_s_0078r_0608': 0.549,
						 'r_0370__Vmax_r_0370': 0.0120878,
						 'r_0599__kmp_s_0514r_0599': 0.549,
						 'r_0220__kmp_s_1066r_0220': 0.549,
						 'r_0512__kms_s_0894r_0512': 0.549,
						 'r_0955__Vmax_r_0955': 0.0163349,
						 'r_0847__kms_s_1020r_0847': 0.549,
						 'r_0374__Vmax_r_0374': 0.52591,
						 'r_0589__kms_s_0919r_0589': 0.549,
						 'r_0238__Keq_r_0238': 1.1,
						 'r_0957__kms_s_1411r_0957': 0.549,
						 'r_0883__Keq_r_0883': 0.6039,
						 'r_0884__Keq_r_0884': 0.286516,
						 'r_0883__kms_s_0316r_0883': 0.549,
						 'r_1027__Vmax_r_1027': 5.5748,
						 'r_0006__kmp_s_1434_br_0006': 0.549,
						 'r_0885__Keq_r_0885': 1.1,
						 'r_0466__kmp_s_1091r_0466': 0.549,
						 'r_1027__kmp_s_0949r_1027': 1.0,
						 'r_0506__kmp_s_0894r_0506': 0.549,
						 'r_0712__kms_s_0031r_0712': 0.549,
						 'r_0351__kmp_s_1082r_0351': 1.50326,
						 'r_0009__kms_s_0386r_0009': 0.549,
						 'r_0660__kmp_s_0118r_0660': 0.549,
						 'r_0972__Keq_r_0972': 1.1,
						 'r_0238__kmp_s_1207r_0238': 0.549,
						 'r_1672__Keq_r_1672': 1.1,
						 'r_0562__kmp_s_0605r_0562': 0.549,
						 'r_0287__kms_s_1080r_0287': 0.549,
						 'r_0421__kms_s_1096r_0421': 0.549,
						 'r_0043__kmp_s_0216r_0043': 0.549,
						 'r_0370__Keq_r_0370': 0.0999269,
						 'r_1816__a_s_1447r_1816': 1.5e-05,
						 'r_0163__kmp_s_0446r_0163': 1.09208,
						 'r_0159__kmp_s_0393r_0159': 0.549,
						 'r_0850__kmp_s_0470r_0850': 1.0,
						 'r_0235__Keq_r_0235': 1.1,
						 'r_0993__Keq_r_0993': 1.1,
						 'r_0328__kms_s_1156r_0328': 0.549,
						 'r_0351__Keq_r_0351': 34.7263,
						 'r_1157__Vmax_r_1157': 0.964941,
						 'r_0246__Vmax_r_0246': 76.0041,
						 'r_1503__kms_s_1338r_1503': 0.549,
						 'r_1027__kms_s_1122r_1027': 0.549,
						 'r_1812__a_s_1347r_1812': 0.02,
						 'r_1041__kmp_s_0731r_1041': 0.0436363,
						 'r_0725__kmp_s_1207r_0725': 0.549,
						 'r_0866__Vmax_r_0866': 3.76975,
						 'r_0791__kmp_s_1071r_0791': 0.549,
						 'r_0607__Keq_r_0607': 0.063468,
						 'r_0220__Vmax_r_0220': 0.11935,
						 'r_0728__kmp_s_0149r_0728': 0.549,
						 'r_0339__Vmax_r_0339': 0.719947,
						 'r_1812__s_0877_or_1812': 0.549,
						 'r_0172__Vmax_r_0172': 0.624358,
						 'r_0650__kms_s_0861r_0650': 0.549,
						 'r_0707__kms_s_0307r_0707': 0.549,
						 'r_0891__kms_s_0427r_0891': 0.549,
						 'r_0068__kmp_s_0330r_0068': 0.549,
						 'r_0514__kms_s_0907r_0514': 0.549,
						 'r_1812__a_s_0564r_1812': 0.003587,
						 'r_1814__V_o': 0.0555,
						 'r_0640__kms_s_0042r_0640': 0.549,
						 'r_1008__kmp_s_1091r_1008': 0.549,
						 'r_0661__kms_s_0118r_0661': 0.549,
						 'r_0891__Keq_r_0891': 0.696514,
						 'r_0417__kmp_s_0470r_0417': 1.0,
						 'r_0249__Keq_r_0249': 0.173154,
						 'r_0771__kmp_s_0446r_0771': 1.09208,
						 'r_0547__Vmax_r_0547': 3.48479,
						 'r_0575__kms_s_1434_br_0575': 0.549,
						 'r_0277__kmp_s_1207r_0277': 0.549,
						 'r_0264__kmp_s_1091r_0264': 0.549,
						 'r_0381__kms_s_0763_br_0381': 0.549,
						 'r_0618__kms_s_0128r_0618': 0.549,
						 'r_0060__kms_s_0763_br_0060': 0.549,
						 'r_0941__kms_s_0400r_0941': 1.71907,
						 'r_0437__kmp_s_0434r_0437': 1.25956,
						 'r_0970__kmp_s_1434_br_0970': 0.549,
						 'r_0779__kmp_s_1430r_0779': 0.549,
						 'r_0633__kmp_s_1338r_0633': 0.549,
						 'r_0707__kmp_s_0015r_0707': 0.549,
						 'r_0418__kms_s_1096r_0418': 0.549,
						 'r_0702__kms_s_0328r_0702': 0.549,
						 'r_0586__kms_s_0886r_0586': 0.549,
						 'r_1003__kmp_s_1207r_1003': 0.549,
						 'r_0174__Vmax_r_0174': 1.7171,
						 'r_0125__kms_s_0763_br_0125': 0.549,
						 'r_0262__kmp_s_0470r_0262': 1.0,
						 'r_0726__kms_s_0410r_0726': 0.549,
						 'r_0430__kmp_s_0470r_0430': 1.0,
						 'r_0157__kmp_s_0763_br_0157': 0.549,
						 'r_0995__Vmax_r_0995': 0.0034727,
						 'r_0251__Keq_r_0251': 0.6039,
						 'r_0264__kms_s_1096r_0264': 0.549,
						 'r_0357__kms_s_0430r_0357': 0.549,
						 'r_0589__Vmax_r_0589': 0.67221,
						 'r_1435__Vmax_r_1435': 0.0232306,
						 'r_0375__kms_s_0763_br_0375': 0.549,
						 'r_0722__kmp_s_0261r_0722': 0.549,
						 'r_0634__Vmax_r_0634': 0.73304,
						 'r_0884__kms_s_0446r_0884': 1.09208,
						 'r_1003__kms_s_0446r_1003': 1.09208,
						 'r_0529__Vmax_r_0529': 4.51989,
						 'r_0430__kms_s_1096r_0430': 0.549,
						 'r_0307__Vmax_r_0307': 4.40553,
						 'r_0585__kms_s_0800r_0585': 0.549,
						 'r_0467__kms_s_1005r_0467': 0.549,
						 'r_0969__kms_s_1082r_0969': 1.50326,
						 'r_0360__Vmax_r_0360': 0.015323,
						 'r_0938__kms_s_0763_br_0938': 0.549,
						 'r_1503__kms_s_0763_br_1503': 0.549,
						 'r_0034__Vmax_r_0034': 0.39732,
						 'r_0955__kms_s_0706r_0955': 0.549,
						 'r_0701__kmp_s_0605r_0701': 0.549,
						 'r_0638__Keq_r_0638': 1.1,
						 'r_0604__kms_s_0315r_0604': 0.549,
						 'r_0530__kms_s_0763_br_0530': 0.549,
						 'r_0183__kms_s_0366r_0183': 0.120104,
						 'r_0174__kmp_s_0740r_0174': 0.549,
						 'r_0940__kms_s_1277r_0940': 0.0605905,
						 'r_0673__kms_s_0040r_0673': 0.549,
						 'r_0568__kms_s_0566r_0568': 0.549,
						 'r_1812__s_0943_or_1812': 0.549,
						 'r_0585__kmp_s_1087r_0585': 0.0867353,
						 'r_0437__kmp_s_0605r_0437': 0.549,
						 'r_0789__kmp_s_0887r_0789': 0.549,
						 'r_0306__kmp_s_1207r_0306': 0.549,
						 'r_0599__kms_s_1434_br_0599': 0.549,
						 'r_0381__Vmax_r_0381': 0.52591,
						 'r_0634__kmp_s_0185r_0634': 0.549,
						 'r_0976__Keq_r_0976': 2.00364,
						 'r_0282__Vmax_r_0282': 0.187549,
						 'r_0220__kms_s_0439r_0220': 0.549,
						 'r_0551__Vmax_r_0551': 1.57168,
						 'r_0263__Keq_r_0263': 2.00364,
						 'r_0371__kmp_s_1207r_0371': 0.549,
						 'r_0417__kms_s_1096r_0417': 0.549,
						 'r_0577__kms_s_0899r_0577': 0.549,
						 'r_0610__kms_s_0605r_0610': 0.549,
						 'r_0262__kms_s_0303r_0262': 0.549,
						 'r_0534__kms_s_0386r_0534': 0.549,
						 'r_0722__kmp_s_0763_br_0722': 0.549,
						 'r_0347__Keq_r_0347': 5726.73,
						 'r_1059__kms_s_1417r_1059': 0.549,
						 'r_1194__kmp_s_0472_br_1194': 1e-05,
						 'r_0526__Vmax_r_0526': 5.48128,
						 'r_0794__kmp_s_1417r_0794': 0.549,
						 'r_0191__kms_s_1434_br_0191': 0.549,
						 'r_1072__Vmax_r_1072': 11.2651,
						 'r_0130__kmp_s_0400r_0130': 1.71907,
						 'r_0856__kms_s_0206r_0856': 0.549,
						 'r_0133__kmp_s_0185r_0133': 0.549,
						 'r_0883__kmp_s_0763_br_0883': 0.549,
						 'r_0430__kmp_s_1140r_0430': 0.549,
						 'r_0044__kmp_s_1091r_0044': 0.549,
						 'r_0419__kmp_s_1434_br_0419': 0.549,
						 'r_0720__kmp_s_1096r_0720': 0.549,
						 'r_0660__kms_s_1379r_0660': 0.549,
						 'r_0496__kms_s_0850r_0496': 0.549,
						 'r_0725__kms_s_1434_br_0725': 0.549,
						 'r_0697__kmp_s_0605r_0697': 0.549,
						 'r_0633__Vmax_r_0633': 1.22649,
						 'r_0466__kmp_s_0470r_0466': 1.0,
						 'r_0847__kmp_s_0763_br_0847': 0.549,
						 'r_0429__kmp_s_1434_br_0429': 0.549,
						 'r_0514__kms_s_0331r_0514': 0.549,
						 'r_0529__kmp_s_0735r_0529': 0.601873,
						 'r_0577__kms_s_0212r_0577': 0.549,
						 'r_0233__kmp_s_0400r_0233': 1.71907,
						 'r_0029__Vmax_r_0029': 0.731496,
						 'r_0271__kmp_s_1091r_0271': 0.549,
						 'r_0127__kms_s_0434r_0127': 1.25956,
						 'r_0937__Vmax_r_0937': 62.2377,
						 'r_0891__kmp_s_0331r_0891': 0.549,
						 'r_0825__kmp_s_0185r_0825': 0.549,
						 'r_0340__kmp_s_0763_br_0340': 0.549,
						 'r_0995__kms_s_0635r_0995': 0.549,
						 'r_0707__kms_s_1091r_0707': 0.549,
						 'r_0607__kmp_s_0763_br_0607': 0.549,
						 'r_0191__kms_s_1091r_0191': 0.549,
						 'r_0384__kmp_s_1434_br_0384': 0.549,
						 'r_0442__kms_s_0605r_0442': 0.549,
						 'r_1035__Keq_r_1035': 0.459088,
						 'r_0861__Vmax_r_0861': 3.0723,
						 'r_0887__Vmax_r_0887': 0.05115,
						 'r_0127__Keq_r_0127': 0.953736,
						 'r_0057__kms_s_0763_br_0057': 0.549,
						 'r_0567__Vmax_r_0567': 0.008393,
						 'r_0021__kmp_s_1207r_0021': 0.549,
						 'r_0005__kms_s_1415r_0005': 0.549,
						 'r_0018__Keq_r_0018': 1.1,
						 'r_0509__kmp_s_1091r_0509': 0.549,
						 'r_0221__Vmax_r_0221': 0.323947,
						 'r_1036__Vmax_r_1036': 0.14014,
						 'r_0955__kmp_s_1517r_0955': 0.549,
						 'r_0464__kms_s_0763_br_0464': 0.549,
						 'r_0018__kms_s_0181r_0018': 0.549,
						 'r_0562__Keq_r_0562': 0.6039,
						 'r_0170__kmp_s_0706r_0170': 0.549,
						 'r_0159__kms_s_1290r_0159': 0.549,
						 'r_0599__Vmax_r_0599': 0.3762,
						 'r_0889__Vmax_r_0889': 0.734467,
						 'r_0562__Vmax_r_0562': 0.0104499,
						 'r_0934__kms_s_0319r_0934': 0.549,
						 'r_0125__Keq_r_0125': 2.00364,
						 'r_0884__kmp_s_0316r_0884': 0.549,
						 'r_0221__Keq_r_0221': 0.0365906,
						 'r_0882__kmp_s_0605r_0882': 0.549,
						 'r_0347__kms_s_0963r_0347': 0.549,
						 'r_0859__Vmax_r_0859': 75.3828,
						 'r_0429__kms_s_1096r_0429': 0.549,
						 'r_0183__kms_s_0763_br_0183': 0.549,
						 'r_0525__kmp_s_0763_br_0525': 0.549,
						 'r_0423__kms_s_1170r_0423': 0.549,
						 'r_0265__kms_s_1096r_0265': 0.549,
						 'r_0419__kmp_s_1091r_0419': 0.549,
						 'r_0421__kmp_s_1170r_0421': 0.549,
						 'r_0221__kmp_s_0899r_0221': 0.549,
						 'r_0221__kmp_s_0763_br_0221': 0.549,
						 'r_0290__Vmax_r_0290': 0.00279509,
						 'r_0853__Keq_r_0853': 0.331541,
						 'r_0941__kmp_s_1277r_0941': 0.0605905,
						 'r_0976__Vmax_r_0976': 1.60931,
						 'r_1812__a_s_1283r_1812': 0.0009,
						 'r_0526__kmp_s_0734r_0526': 0.549,
						 'r_0277__kmp_s_0400r_0277': 1.71907,
						 'r_0245__kms_s_0331r_0245': 0.549,
						 'r_0430__kmp_s_1091r_0430': 0.549,
						 'r_1041__Keq_r_1041': 0.0797509,
						 'intracellular': 1.0,
						 'r_0266__Vmax_r_0266': 0.0951282,
						 'r_0245__Keq_r_0245': 0.552981,
						 'r_0429__kmp_s_1091r_0429': 0.549,
						 'r_0585__kms_s_1082r_0585': 1.50326,
						 'r_0888__kms_s_1434_br_0888': 0.549,
						 'r_0249__kmp_s_1207r_0249': 0.549,
						 'r_0429__Keq_r_0429': 3.64962,
						 'r_0398__kmp_s_1243r_0398': 0.0271093,
						 'r_0575__kmp_s_1087r_0575': 0.0867353,
						 'r_0607__kms_s_1434_br_0607': 0.549,
						 'r_0567__kmp_s_0400r_0567': 1.71907,
						 'r_0505__Vmax_r_0505': 0.753302,
						 'r_0991__Vmax_r_0991': 0.0961402,
						 'r_0712__kms_s_0521r_0712': 0.549,
						 'r_0172__kmp_s_0400r_0172': 1.71907,
						 'r_0725__kmp_s_1020r_0725': 0.549,
						 'r_0330__Keq_r_0330': 0.6039,
						 'r_1507__kms_s_1348_br_1507': 42.2,
						 'r_0370__kms_s_0386r_0370': 0.549,
						 'r_0640__kms_s_1096r_0640': 0.549,
						 'r_0606__kmp_s_0816r_0606': 0.549,
						 'r_0268__kmp_s_0303r_0268': 0.549,
						 'r_0264__Keq_r_0264': 2.00364,
						 'r_0060__kmp_s_0055r_0060': 0.549,
						 'r_0581__Keq_r_0581': 2.00364,
						 'r_0040__kmp_s_0163r_0040': 0.549,
						 'r_1812__s_0619_or_1812': 0.549,
						 'r_0608__Vmax_r_0608': 0.187549,
						 'r_1026__Vmax_r_1026': 3.18448,
						 'r_0018__kms_s_0899r_0018': 0.549,
						 'r_0277__Vmax_r_0277': 7.44478,
						 'r_1812__a_s_0907r_1812': 0.268,
						 'r_0937__kms_s_1277r_0937': 0.0605905,
						 'r_1032__kmp_s_0619r_1032': 0.549,
						 'r_0701__kms_s_0446r_0701': 1.09208,
						 'r_0238__kms_s_0301r_0238': 0.549,
						 'r_0384__kms_s_0018r_0384': 0.549,
						 'r_0888__kms_s_0446r_0888': 1.09208,
						 'r_1038__kmp_s_0416r_1038': 0.549,
						 'r_1816__s_0963_or_1816': 0.549,
						 'r_1072__Keq_r_1072': 2.00364,
						 'r_0539__Vmax_r_0539': 2.21431,
						 'r_0957__kmp_s_1434_br_0957': 0.549,
						 'r_0859__kmp_s_0537r_0859': 1.34278,
						 'r_1293__kmp_s_0545r_1293': 0.0987587,
						 'r_0430__Vmax_r_0430': 0.0237906,
						 'r_0465__kms_s_1096r_0465': 0.549,
						 'r_0576__Keq_r_0576': 1.1,
						 'r_0526__kmp_s_0763_br_0526': 0.549,
						 'r_0213__kmp_s_0763_br_0213': 0.549,
						 'r_0882__kms_s_0334r_0882': 0.549,
						 'r_0538__kmp_s_0430r_0538': 0.549,
						 'r_1812__s_0920_or_1812': 0.549,
						 'r_0172__Keq_r_0172': 0.950614,
						 'r_0607__kmp_s_0306r_0607': 0.549,
						 'r_1036__kmp_s_0561r_1036': 0.549,
						 'r_0057__kms_s_0247r_0057': 0.549,
						 'r_1038__kmp_s_1207r_1038': 0.549,
						 'r_0034__Keq_r_0034': 2.52371,
						 'r_0588__kmp_s_0763_br_0588': 0.549,
						 'r_0479__kms_s_0689r_0479': 0.549,
						 'r_0712__Vmax_r_0712': 0.275879,
						 'r_0506__Keq_r_0506': 1.73154,
						 'r_1008__kmp_s_0805r_1008': 0.549,
						 'r_0586__kmp_s_0919r_0586': 0.549,
						 'r_0661__kms_s_0763_br_0661': 0.549,
						 'r_0576__kmp_s_0915r_0576': 0.549,
						 'r_0386__Keq_r_0386': 1.04217,
						 'r_0437__Vmax_r_0437': 0.0038115,
						 'r_0336__kmp_s_0521r_0336': 0.549,
						 'r_0875__kmp_s_0553r_0875': 0.549,
						 'r_1194__Vmax_r_1194': 2.37902,
						 'r_0967__kms_s_1293r_0967': 0.549,
						 'r_1812__a_s_0569r_1812': 0.002432,
						 'r_0598__kmp_s_1091r_0598': 0.549,
						 'r_0430__kms_s_0763_br_0430': 0.549,
						 'r_0018__kmp_s_0185r_0018': 0.549,
						 'r_0157__kms_s_0446r_0157': 1.09208,
						 'r_0634__Keq_r_0634': 1.1,
						 'r_1073__kmp_s_0185r_1073': 0.549,
						 'r_0888__Keq_r_0888': 0.950614,
						 'r_0014__kmp_s_0319r_0014': 0.549,
						 'r_0575__Keq_r_0575': 0.00110373,
						 'r_0006__kmp_s_0743r_0006': 0.549,
						 'r_0466__kmp_s_0514r_0466': 0.549,
						 'r_0499__Keq_r_0499': 4.77829,
						 'r_0538__kmp_s_0307r_0538': 0.549,
						 'r_1812__a_s_0933r_1812': 0.050027,
						 'r_0232__Keq_r_0232': 0.6039,
						 'r_0485__kmp_s_0692r_0485': 0.549,
						 'r_0352__Vmax_r_0352': 3.30329,
						 'r_0605__kms_s_0532r_0605': 0.549,
						 'r_0723__kms_s_0710r_0723': 0.549,
						 'r_0170__kmp_s_1207r_0170': 0.549,
						 'r_0005__kmp_s_0001r_0005': 0.549,
						 'r_0398__Keq_r_0398': 6500.0,
						 'r_0125__kmp_s_0380r_0125': 0.549,
						 'r_1812__s_0752_or_1812': 0.549,
						 'r_0618__Vmax_r_0618': 0.00127051,
						 'r_0394__kmp_s_0763_br_0394': 0.549,
						 'r_0789__kms_s_1151r_0789': 0.549,
						 'r_0722__kms_s_0055r_0722': 0.549,
						 'r_0697__Keq_r_0697': 2.00364,
						 'r_1812__a_s_1000r_1812': 1.0,
						 'r_0936__kms_s_0763_br_0936': 0.549,
						 'r_0884__Vmax_r_0884': 1.26862,
						 'r_0993__kms_s_0763_br_0993': 0.549,
						 'r_0605__kmp_s_0212r_0605': 0.549,
						 'r_0174__kmp_s_1277r_0174': 0.0605905,
						 'r_0967__kmp_s_1290r_0967': 0.549,
						 'r_0044__kms_s_0218r_0044': 0.549,
						 'r_0238__kms_s_1096r_0238': 0.549,
						 'r_0702__kmp_s_0933r_0702': 0.549,
						 'r_0725__Vmax_r_0725': 0.006545,
						 'r_0263__Vmax_r_0263': 0.0454962,
						 'r_0465__kmp_s_0470r_0465': 1.0,
						 'r_0598__kmp_s_0514r_0598': 0.549,
						 'r_0866__kmp_s_0193r_0866': 0.0515066,
						 'r_0009__kmp_s_0763_br_0009': 0.549,
						 'r_0385__kmp_s_1434_br_0385': 0.549,
						 'r_0393__kms_s_0616r_0393': 0.549,
						 'r_0005__kmp_s_1411r_0005': 0.549,
						 'r_0058__kms_s_0763_br_0058': 0.549,
						 'r_0728__Keq_r_0728': 1.1,
						 'r_0159__kms_s_1434_br_0159': 0.549,
						 'r_0266__kmp_s_1434_br_0266': 0.549,
						 'r_0465__kmp_s_1091r_0465': 0.549,
						 'r_0657__Vmax_r_0657': 0.706853,
						 'r_0881__kms_s_0080r_0881': 0.549,
						 'r_0265__kms_s_0302r_0265': 0.549,
						 'r_0008__kms_s_0079r_0008': 0.549,
						 'r_0016__kmp_s_0042r_0016': 0.549,
						 'r_1027__Keq_r_1027': 2.00364,
						 'r_0229__kms_s_0881r_0229': 0.549,
						 'r_0937__kmp_s_0400r_0937': 1.71907,
						 'r_0715__Vmax_r_0715': 0.476517,
						 'r_0525__kms_s_1082r_0525': 1.50326,
						 'r_0888__kmp_s_0400r_0888': 1.71907,
						 'r_1066__kms_s_0622r_1066': 0.549,
						 'r_0873__kmp_s_1228r_0873': 0.549,
						 'r_0465__kms_s_1005r_0465': 0.549,
						 'r_0362__kms_s_0591r_0362': 0.549,
						 'r_0245__kmp_s_0334r_0245': 0.549,
						 'r_0191__Vmax_r_0191': 9.45451,
						 'r_1007__kms_s_1347r_1007': 0.549,
						 'r_0505__kmp_s_0539r_0505': 0.104555,
						 'r_0562__kms_s_0755r_0562': 0.549,
						 'r_0262__Keq_r_0262': 0.0348439,
						 'r_0340__Vmax_r_0340': 0.431968,
						 'r_0118__Vmax_r_0118': 0.125399,
						 'r_1041__Vmax_r_1041': 20.559,
						 'r_0057__kmp_s_0046r_0057': 0.549,
						 'r_0059__kmp_s_0234r_0059': 0.549,
						 'r_0220__kms_s_0331r_0220': 0.549,
						 'r_0783__kmp_s_0369r_0783': 0.549,
						 'r_0439__kmp_s_0514r_0439': 0.549,
						 'r_1812__s_0863_or_1812': 0.549,
						 'r_0534__kmp_s_0763_br_0534': 0.549,
						 'r_0509__Keq_r_0509': 2.00364,
						 'r_1036__kms_s_1304r_1036': 0.549,
						 'r_0298__kmp_s_1434_br_0298': 0.549,
						 'r_0969__kms_s_0942r_0969': 0.549,
						 'r_0599__kms_s_0380r_0599': 0.549,
						 'r_0972__kmp_s_0514r_0972': 0.549,
						 'r_0043__Keq_r_0043': 0.6039,
						 'r_0721__kms_s_0234r_0721': 0.549,
						 'r_0123__Vmax_r_0123': 0.105501,
						 'r_0515__kms_s_0899r_0515': 0.549,
						 'r_0328__Vmax_r_0328': 13.2165,
						 'r_0375__kmp_s_0309r_0375': 0.549,
						 'r_0340__kmp_s_0369r_0340': 0.549,
						 'r_0657__kmp_s_0763_br_0657': 0.549,
						 'r_0719__kmp_s_0247r_0719': 0.549,
						 'r_0418__kmp_s_0968r_0418': 0.549,
						 'r_0338__kms_s_0917r_0338': 0.549,
						 'r_0891__kmp_s_0763_br_0891': 0.549,
						 'r_0307__kms_s_0501r_0307': 0.549,
						 'r_0510__kmp_s_1082r_0510': 1.50326,
						 'r_0282__kmp_s_1434_br_0282': 0.549,
						 'r_0581__kmp_s_0800r_0581': 0.549,
						 'r_0697__kms_s_0553r_0697': 0.549,
						 'r_1042__kmp_s_1434_br_1042': 0.549,
						 'r_0351__kmp_s_0530r_0351': 0.549,
						 'r_0959__kms_s_0446r_0959': 1.09208,
						 'r_0650__kmp_s_0867r_0650': 0.549,
						 'r_0261__kmp_s_1458r_0261': 0.549,
						 'r_0111__kms_s_1096r_0111': 0.549,
						 'r_0512__kmp_s_1082r_0512': 1.50326,
						 'r_0357__kmp_s_1434_br_0357': 0.549,
						 'r_1073__Vmax_r_1073': 1.1011,
						 'r_1003__Vmax_r_1003': 0.13134,
						 'r_0362__Keq_r_0362': 0.698801,
						 'r_0345__kmp_s_0511r_0345': 0.549,
						 'r_0562__kmp_s_0145r_0562': 0.549,
						 'r_0465__kmp_s_1434_br_0465': 0.549,
						 'r_0352__kmp_s_0529r_0352': 0.549,
						 'r_0266__kmp_s_1091r_0266': 0.549,
						 'r_0025__kmp_s_0170r_0025': 0.549,
						 'r_0888__kms_s_1052r_0888': 0.549,
						 'r_0515__kms_s_0430r_0515': 0.549,
						 'r_0270__Keq_r_0270': 1.1,
						 'r_0586__kms_s_0763_br_0586': 0.549,
						 'r_0375__kms_s_0601r_0375': 0.549,
						 'r_0630__Vmax_r_0630': 6.98167,
						 'r_0884__kmp_s_0400r_0884': 1.71907,
						 'r_0290__kmp_s_0514r_0290': 0.549,
						 'r_0439__kms_s_1334r_0439': 0.549,
						 'r_0688__Keq_r_0688': 34.7263,
						 'r_0911__kms_s_1258r_0911': 0.549,
						 'r_0514__kmp_s_0605r_0514': 0.549,
						 'r_0375__kms_s_1096r_0375': 0.549,
						 'r_0130__kmp_s_1070r_0130': 0.549,
						 'r_0277__kmp_s_0763_br_0277': 0.549,
						 'r_0057__Keq_r_0057': 34.7263,
						 'r_0859__kmp_s_0400r_0859': 1.71907,
						 'r_0995__kmp_s_1434_br_0995': 0.549,
						 'r_0598__kms_s_0763_br_0598': 0.549,
						 'r_0488__Vmax_r_0488': 4.5199,
						 'r_0267__kms_s_0763_br_0267': 0.549,
						 'r_0125__kms_s_0369r_0125': 0.549,
						 'r_0042__kmp_s_1434_br_0042': 0.549,
						 'r_0123__kmp_s_1005r_0123': 0.549,
						 'r_0345__Keq_r_0345': 0.698801,
						 'r_0610__kmp_s_1207r_0610': 0.549,
						 'r_0058__kmp_s_0052r_0058': 0.549,
						 'r_1461__Vmax_r_1461': 0.0925906,
						 'r_0948__kmp_s_1434_br_0948': 0.549,
						 'r_0499__kmp_s_0400r_0499': 1.71907,
						 'r_0970__kms_s_1096r_0970': 0.549,
						 'r_0336__kmp_s_0763_br_0336': 0.549,
						 'r_0345__kmp_s_0446r_0345': 1.09208,
						 'r_0157__kmp_s_0400r_0157': 1.71907,
						 'r_0856__kmp_s_0763_br_0856': 0.549,
						 'r_0881__Vmax_r_0881': 0.229351,
						 'r_0133__kms_s_0899r_0133': 0.549,
						 'r_0118__kms_s_0380r_0118': 0.549,
						 'r_0719__Vmax_r_0719': 3.30329,
						 'r_0972__Vmax_r_0972': 0.00279509,
						 'r_0528__kmp_s_1207r_0528': 0.549,
						 'r_0229__kms_s_0907r_0229': 0.549,
						 'r_0357__kms_s_0624r_0357': 0.549,
						 'r_0940__Vmax_r_0940': 9.4545,
						 'r_0889__kms_s_0122r_0889': 0.549,
						 'r_0423__kmp_s_1434_br_0423': 0.549,
						 'r_0229__kmp_s_0763_br_0229': 0.549,
						 'r_0697__kms_s_0755r_0697': 0.549,
						 'r_0307__kms_s_1434_br_0307': 0.549,
						 'r_0183__kms_s_1087r_0183': 0.0867353,
						 'r_0977__Keq_r_0977': 0.950614,
						 'r_1050__kmp_s_0955r_1050': 0.549,
						 'r_0938__kmp_s_0470r_0938': 1.0,
						 'r_0165__kms_s_0706r_0165': 0.549,
						 'r_0351__kms_s_0529r_0351': 0.549,
						 'r_0951__kmp_s_0562r_0951': 0.549,
						 'r_0360__kmp_s_0564r_0360': 0.549,
						 'r_0512__Vmax_r_0512': 1.1781,
						 'r_1812__a_s_0511r_1812': 0.05,
						 'r_0304__kms_s_0500r_0304': 0.549,
						 'r_0948__kms_s_0163r_0948': 0.549,
						 'r_0640__kmp_s_1091r_0640': 0.549,
						 'r_0911__Keq_r_0911': 1.1,
						 'r_0165__Keq_r_0165': 0.805968,
						 'r_1073__kms_s_0899r_1073': 0.549,
						 'r_0891__kms_s_0446r_0891': 1.09208,
						 'r_0640__kmp_s_0007r_0640': 0.549,
						 'r_0789__Vmax_r_0789': 0.912336,
						 'r_0044__Vmax_r_0044': 0.00279511,
						 'r_0657__kms_s_0905r_0657': 0.549,
						 'r_0123__kms_s_0380r_0123': 0.549,
						 'r_0610__Vmax_r_0610': 3.2032,
						 'r_1072__kms_s_0549r_1072': 0.549,
						 'r_0794__Keq_r_0794': 2.00364,
						 'r_1812__a_s_0743r_1812': 0.51852,
						 'r_0464__kmp_s_0514r_0464': 0.549,
						 'r_1024__kms_s_1096r_1024': 0.549,
						 'r_0347__Vmax_r_0347': 0.12924,
						 'r_0539__kmp_s_0309r_0539': 0.549,
						 'r_1814__s_0463_or_1814': 0.549,
						 'r_1812__a_s_0881r_1812': 0.17152,
						 'r_0825__kms_s_0859r_0825': 0.549,
						 'r_1461__kmp_s_0763_br_1461': 0.549,
						 'r_0381__kmp_s_1434_br_0381': 0.549,
						 'r_0271__kms_s_0763_br_0271': 0.549,
						 'r_1812__a_s_0001r_1812': 1.1358,
						 'r_0702__kmp_s_0763_br_0702': 0.549,
						 'r_0246__kmp_s_0446r_0246': 1.09208,
						 'r_1816__s_0632_or_1816': 0.549,
						 'r_0720__Vmax_r_0720': 3.30329,
						 'r_0886__Vmax_r_0886': 1.53571,
						 'r_0213__Keq_r_0213': 0.6039,
						 'r_0418__kms_s_0574r_0418': 0.549,
						 'r_0060__kms_s_0261r_0060': 0.549,
						 'r_0044__Keq_r_0044': 3.64962,
						 'r_1247__kmp_s_0651_br_1247': 24.5,
						 'r_0261__kmp_s_1096r_0261': 0.549,
						 'r_0034__kmp_s_1207r_0034': 0.549,
						 'r_0573__kmp_s_0763_br_0573': 0.549,
						 'r_0911__kmp_s_1434_br_0911': 0.549,
						 'r_0937__kms_s_0458r_0937': 0.549,
						 'r_0170__kms_s_0881r_0170': 0.549,
						 'r_0229__kms_s_1434_br_0229': 0.549,
						 'r_0582__Vmax_r_0582': 2.1945,
						 'r_0604__kmp_s_0317r_0604': 0.549,
						 'r_0576__kms_s_0916r_0576': 0.549,
						 'r_0439__kms_s_0434r_0439': 1.25956,
						 'r_1812__s_0911_or_1812': 0.549,
						 'r_0588__Keq_r_0588': 0.950614,
						 'r_0465__kms_s_0977r_0465': 0.549,
						 'r_0229__kmp_s_0605r_0229': 0.549,
						 'r_0688__kms_s_1156r_0688': 0.549,
						 'r_0465__Keq_r_0465': 3.64962,
						 'r_0009__Vmax_r_0009': 0.0421078,
						 'r_0467__Keq_r_0467': 3.64962,
						 'r_1814__a_s_0463r_1814': 1.0,
						 'r_0464__Keq_r_0464': 3.64962,
						 'r_0112__kmp_s_0470r_0112': 1.0,
						 'r_1003__kmp_s_0400r_1003': 1.71907,
						 'r_0955__kmp_s_1434_br_0955': 0.549,
						 'r_0058__Vmax_r_0058': 3.30332,
						 'r_0251__kmp_s_0458r_0251': 0.549,
						 'r_0514__kms_s_1434_br_0514': 0.549,
						 'r_0298__kms_s_1293r_0298': 0.549,
						 'r_0191__kmp_s_0369r_0191': 0.549,
						 'r_0525__kmp_s_0265r_0525': 0.000108759,
						 'r_0885__kmp_s_0309r_0885': 0.549,
						 'r_0328__kmp_s_0763_br_0328': 0.549,
						 'r_0911__kmp_s_0859r_0911': 0.549,
						 'r_0719__kmp_s_0763_br_0719': 0.549,
						 'r_0856__kms_s_1521r_0856': 0.549,
						 'r_0287__kms_s_1096r_0287': 0.549,
						 'r_0514__Vmax_r_0514': 1.00155,
						 'r_0891__Vmax_r_0891': 2.25059,
						 'r_0934__Vmax_r_0934': 0.00385,
						 'r_0638__kmp_s_1257r_0638': 0.549,
						 'r_0913__kms_s_1091r_0913': 0.549,
						 'r_0238__kmp_s_1091r_0238': 0.549,
						 'r_0439__Keq_r_0439': 0.953736,
						 'r_0284__Vmax_r_0284': 0.0367841,
						 'r_0765__kmp_s_0470r_0765': 1.0,
						 'r_0791__kmp_s_1151r_0791': 0.549,
						 'r_0951__kmp_s_1434_br_0951': 0.549,
						 'r_1040__Keq_r_1040': 1.1,
						 'r_0874__Vmax_r_0874': 0.0193599,
						 'r_0059__Vmax_r_0059': 3.30332,
						 'r_0599__kmp_s_0763_br_0599': 0.549,
						 'r_0660__Vmax_r_0660': 3.30329,
						 'r_0034__kms_s_1434_br_0034': 0.549,
						 'r_0251__Vmax_r_0251': 20.097,
						 'r_0547__kms_s_1415r_0547': 0.549,
						 'r_0371__kmp_s_0763_br_0371': 0.549,
						 'r_0936__kms_s_1096r_0936': 0.549,
						 'r_0058__Keq_r_0058': 34.7263,
						 'r_0466__kms_s_0763_br_0466': 0.549,
						 'r_0825__Vmax_r_0825': 0.48895,
						 'r_0993__kmp_s_0605r_0993': 0.549,
						 'r_0111__kmp_s_0018r_0111': 0.549,
						 'r_0251__kms_s_1434_br_0251': 0.549,
						 'r_0169__kms_s_0009r_0169': 0.549,
						 'r_0726__kmp_s_0128r_0726': 0.549,
						 'r_0123__kms_s_0458r_0123': 0.549,
						 'r_0258__kms_s_1096r_0258': 0.549,
						 'r_0043__kmp_s_1207r_0043': 0.549,
						 'r_0551__kms_s_0907r_0551': 0.549,
						 'r_0277__kmp_s_0469r_0277': 0.549,
						 'r_0977__kmp_s_0267r_0977': 0.549,
						 'r_0661__kmp_s_1379r_0661': 0.549,
						 'r_1157__kmp_s_0430r_1157': 0.549,
						 'r_0347__kmp_s_1082r_0347': 1.50326,
						 'r_1812__s_0569_or_1812': 0.549,
						 'r_0697__Vmax_r_0697': 5.51762,
						 'r_1812__s_0511_or_1812': 0.549,
						 'r_0963__kmp_s_0427r_0963': 0.549,
						 'r_1035__kms_s_0539r_1035': 0.104555,
						 'r_1812__s_0929_or_1812': 0.549,
						 'r_0172__kmp_s_0206r_0172': 0.549,
						 'r_0159__Keq_r_0159': 1.1,
						 'r_0877__Vmax_r_0877': 0.17556,
						 'r_1032__kmp_s_0601r_1032': 0.549,
						 'r_0881__kms_s_1434_br_0881': 0.549,
						 'r_0068__Vmax_r_0068': 1.0241,
						 'r_0534__Vmax_r_0534': 0.0421077,
						 'r_0877__kmp_s_0021r_0877': 0.549,
						 'r_0169__Vmax_r_0169': 0.333848,
						 'r_1032__kms_s_0624r_1032': 0.549,
						 'r_0608__kmp_s_0088r_0608': 0.549,
						 'r_1050__Vmax_r_1050': 0.41272,
						 'r_0425__Vmax_r_0425': 0.0118696,
						 'r_0861__kmp_s_0549r_0861': 0.549,
						 'r_0298__kms_s_1447r_0298': 0.549,
						 'r_0882__kms_s_1434_br_0882': 0.549,
						 'r_0282__kms_s_0801r_0282': 0.549,
						 'r_0430__kmp_s_1434_br_0430': 0.549,
						 'r_0551__kmp_s_0434r_0551': 1.25956,
						 'r_0793__kmp_s_0605r_0793': 0.549,
						 'r_0496__kms_s_0712r_0496': 0.549,
						 'r_1038__Vmax_r_1038': 0.1001,
						 'r_0009__Keq_r_0009': 0.0999269,
						 'r_0526__kms_s_0732r_0526': 0.15,
						 'r_1026__Keq_r_1026': 0.0725309,
						 'r_0213__kmp_s_0419r_0213': 0.549,
						 'r_0263__kmp_s_1091r_0263': 0.549,
						 'r_0270__kmp_s_0627r_0270': 0.549,
						 'r_0831__kms_s_1233r_0831': 0.549,
						 'r_0605__Vmax_r_0605': 0.229349,
						 'r_0890__kmp_s_0400r_0890': 1.71907,
						 'r_0418__kms_s_1005r_0418': 0.549,
						 'r_0913__kmp_s_0209r_0913': 0.549,
						 'r_0963__Keq_r_0963': 1.1,
						 'r_0016__kms_s_1277r_0016': 0.0605905,
						 'r_0419__kmp_s_0470r_0419': 1.0,
						 'r_0229__kms_s_0446r_0229': 1.09208,
						 'r_0421__Keq_r_0421': 3.64962,
						 'r_0172__kms_s_0446r_0172': 1.09208,
						 'r_1035__kms_s_0533r_1035': 0.549,
						 'r_0720__kms_s_1091r_0720': 0.549,
						 'r_1072__kmp_s_0605r_1072': 0.549,
						 'r_0133__Keq_r_0133': 1.1,
						 'r_0949__kmp_s_0320r_0949': 0.549,
						 'r_0479__kmp_s_0400r_0479': 1.71907,
						 'r_0008__Keq_r_0008': 1.1,
						 'r_0057__Vmax_r_0057': 3.30332,
						 'r_0220__Keq_r_0220': 1.1,
						 'r_0959__kmp_s_0566r_0959': 0.549,
						 'r_1812__s_1417_or_1812': 0.549,
						 'r_0588__kms_s_0446r_0588': 1.09208,
						 'r_0530__Keq_r_0530': 741.47,
						 'r_1038__kms_s_1434_br_1038': 0.549,
						 'r_0249__kms_s_1434_br_0249': 0.549,
						 'r_0509__kms_s_0430r_0509': 0.549,
						 'r_0874__Keq_r_0874': 0.6039,
						 'r_0466__kmp_s_1187r_0466': 0.549,
						 'r_1816__s_1447_or_1816': 0.549,
						 'r_0509__kmp_s_1434_br_0509': 0.549,
						 'r_0657__kmp_s_0120r_0657': 0.549,
						 'r_0874__kmp_s_0763_br_0874': 0.549,
						 'r_0060__Vmax_r_0060': 3.30332,
						 'r_0831__kmp_s_1226r_0831': 0.549,
						 'r_0466__Vmax_r_0466': 0.0179399,
						 'r_0955__Keq_r_0955': 0.6039,
						 'r_1037__Vmax_r_1037': 1.1627,
						 'r_0290__Keq_r_0290': 0.6039,
						 'r_0972__kmp_s_0470r_0972': 1.0,
						 'r_0875__Vmax_r_0875': 1.5048,
						 'r_0009__kmp_s_0514r_0009': 0.549,
						 'r_0418__kmp_s_1091r_0418': 0.549,
						 'r_0856__Vmax_r_0856': 1.07843,
						 'r_0479__kms_s_0309r_0479': 0.549,
						 'r_0233__kms_s_0881r_0233': 0.549,
						 'r_0375__Keq_r_0375': 2.00364,
						 'r_1812__s_0907_or_1812': 0.549,
						 'r_0847__kmp_s_0511r_0847': 0.549,
						 'r_0573__kms_s_0446r_0573': 1.09208,
						 'r_0258__kms_s_0763_br_0258': 0.549,
						 'r_0287__Vmax_r_0287': 0.00584431,
						 'r_1812__s_1000_or_1812': 0.549,
						 'r_0850__Keq_r_0850': 1.1,
						 'r_0026__kms_s_1434_br_0026': 0.549,
						 'r_0419__kmp_s_1028r_0419': 0.549,
						 'r_0130__kms_s_1071r_0130': 0.549,
						 'r_0266__kms_s_1455r_0266': 0.549,
						 'r_0058__kms_s_1087r_0058': 0.0867353,
						 'r_0171__kmp_s_0434r_0171': 1.25956,
						 'r_0171__Vmax_r_0171': 0.395998,
						 'r_0265__kmp_s_1091r_0265': 0.549,
						 'r_1040__kmp_s_0663r_1040': 0.549,
						 'r_0938__kms_s_1277r_0938': 0.0605905,
						 'r_0419__kms_s_0763_br_0419': 0.549,
						 'r_0464__kms_s_1096r_0464': 0.549,
						 'r_0957__Keq_r_0957': 0.6039,
						 'r_1503__Vmax_r_1503': 0.840147,
						 'r_0014__kms_s_0763_br_0014': 0.549,
						 'r_0528__Vmax_r_0528': 3.48809,
						 'r_0290__kmp_s_1080r_0290': 0.549,
						 'r_0534__kms_s_1315r_0534': 12.8511,
						 'r_0059__kms_s_1087r_0059': 0.0867353,
						 'r_0951__Vmax_r_0951': 0.0120515,
						 'r_0246__kms_s_1207r_0246': 0.549,
						 'r_0016__kms_s_0763_br_0016': 0.549,
						 'r_0702__Keq_r_0702': 0.6039,
						 'r_1816__a_s_1233r_1816': 0.000697,
						 'r_0006__Keq_r_0006': 0.6039,
						 'r_0688__kmp_s_0069r_0688': 0.549,
						 'r_0357__Keq_r_0357': 0.6039,
						 'r_1008__Keq_r_1008': 3.64962,
						 'r_0271__Keq_r_0271': 2.00364,
						 'r_0606__Keq_r_0606': 0.6039,
						 'r_0721__kmp_s_0763_br_0721': 0.549,
						 'r_0726__Vmax_r_0726': 0.004323,
						 'r_0479__kmp_s_1207r_0479': 0.549,
						 'r_0112__Keq_r_0112': 299.629,
						 'r_0439__Vmax_r_0439': 0.001914,
						 'r_0304__kmp_s_1258r_0304': 0.549,
						 'r_0246__Keq_r_0246': 3.47564,
						 'r_0374__kmp_s_0801r_0374': 0.549,
						 'r_0170__kmp_s_0763_br_0170': 0.549,
						 'r_0267__kms_s_1160r_0267': 0.549,
						 'r_0417__kmp_s_0574r_0417': 0.549,
						 'r_0232__kmp_s_1073r_0232': 0.549,
						 'r_0859__kms_s_0446r_0859': 1.09208,
						 'r_1038__Keq_r_1038': 1.1,
						 'r_0015__Vmax_r_0015': 0.00605002,
						 'r_0934__kmp_s_0320r_0934': 0.549,
						 'r_0290__kms_s_1355r_0290': 0.549,
						 'r_0268__kms_s_0763_br_0268': 0.549,
						 'r_0118__kmp_s_0374r_0118': 0.549,
						 'r_0582__kmp_s_0514r_0582': 0.549,
						 'r_0298__Vmax_r_0298': 0.0918388,
						 'r_0719__kmp_s_1096r_0719': 0.549,
						 'r_0112__kms_s_1277r_0112': 0.0605905,
						 'r_0562__kmp_s_0763_br_0562': 0.549,
						 'r_0238__kms_s_0763_br_0238': 0.549,
						 'r_0221__kms_s_0907r_0221': 0.549,
						 'r_0249__Vmax_r_0249': 50.4568,
						 'r_0277__kms_s_0446r_0277': 1.09208,
						 'r_0890__kmp_s_0763_br_0890': 0.549,
						 'r_0589__Keq_r_0589': 1.1,
						 'r_0634__kms_s_0899r_0634': 0.549,
						 'r_1812__s_0416_or_1812': 0.549,
						 'r_0127__kmp_s_0446r_0127': 1.09208,
						 'r_1003__kms_s_1338r_1003': 0.549,
						 'r_0967__Vmax_r_0967': 0.00141569,
						 'r_0467__kmp_s_1091r_0467': 0.549,
						 'r_1812__s_0564_or_1812': 0.549,
						 'r_0551__kmp_s_0752r_0551': 0.549,
						 'r_0638__kms_s_0850r_0638': 0.549,
						 'r_0582__kms_s_1434_br_0582': 0.549,
						 'r_0014__kms_s_1434_br_0014': 0.549,
						 'r_0336__kms_s_0430r_0336': 0.549,
						 'r_0771__Keq_r_0771': 0.698801,
						 'r_0525__Keq_r_0525': 3200.0,
						 'r_0621__kmp_s_0828r_0621': 0.549,
						 'r_0425__kmp_s_0470r_0425': 1.0,
						 'r_0534__kmp_s_0514r_0534': 0.549,
						 'r_0534__Keq_r_0534': 0.0141635,
						 'r_0699__kms_s_1434_br_0699': 0.549,
						 'r_0169__kmp_s_0317r_0169': 0.549,
						 'r_0993__kmp_s_1327r_0993': 0.549,
						 'r_0425__kmp_s_0514r_0425': 0.549,
						 'r_0779__kmp_s_0400r_0779': 1.71907,
						 'r_0972__kms_s_0943r_0972': 0.549,
						 'r_1812__s_0933_or_1812': 0.549,
						 'r_0423__Keq_r_0423': 3.64962,
						 'r_1073__kms_s_0238r_1073': 0.549,
						 'r_0213__kms_s_1415r_0213': 0.549,
						 'r_1816__a_s_1399r_1816': 0.000781,
						 'r_1816__s_1228_or_1816': 0.549,
						 'r_0874__kmp_s_1225r_0874': 0.549,
						 'r_0725__Keq_r_0725': 1.1,
						 'r_0191__kms_s_0366r_0191': 0.120104,
						 'r_0268__kms_s_1160r_0268': 0.549,
						 'r_0262__kms_s_1082r_0262': 1.50326,
						 'r_0425__kmp_s_1091r_0425': 0.549,
						 'r_0882__kmp_s_0080r_0882': 0.549,
						 'r_0721__Keq_r_0721': 0.6039,
						 'r_0640__kms_s_0763_br_0640': 0.549,
						 'r_0715__kmp_s_0850r_0715': 0.549,
						 'r_0526__kmp_s_1096r_0526': 0.549,
						 'r_0633__kmp_s_0749r_0633': 0.549,
						 'r_1059__kms_s_0446r_1059': 1.09208,
						 'r_0262__Vmax_r_0262': 0.0785834,
						 'r_0015__Keq_r_0015': 2.00364,
						 'r_0991__kmp_s_1082r_0991': 1.50326,
						 'r_0720__kmp_s_0257r_0720': 0.549,
						 'r_0338__kmp_s_0888r_0338': 0.549,
						 'r_0510__kms_s_0907r_0510': 0.549,
						 'r_0338__kms_s_0943r_0338': 0.549,
						 'r_0226__kms_s_0446r_0226': 1.09208,
						 'r_0423__Vmax_r_0423': 0.00599718,
						 'r_0339__Keq_r_0339': 0.6039,
						 'r_0825__kms_s_0899r_0825': 0.549,
						 'r_0853__kmp_s_0511r_0853': 0.549,
						 'r_0674__Keq_r_0674': 1.1,
						 'r_0170__kms_s_0755r_0170': 0.549,
						 'r_0386__kmp_s_0763_br_0386': 0.549,
						 'r_0375__kmp_s_1091r_0375': 0.549,
						 'r_0357__kmp_s_0763_br_0357': 0.549,
						 'r_0338__Vmax_r_0338': 0.18326,
						 'r_1007__kmp_s_0304r_1007': 0.549,
						 'r_0957__kmp_s_0622r_0957': 0.549,
						 'r_0466__kms_s_1005r_0466': 0.549,
						 'r_0538__kms_s_0740r_0538': 0.549,
						 'r_0575__kmp_s_0911r_0575': 0.549,
						 'r_0850__Vmax_r_0850': 0.0109449,
						 'r_0123__Keq_r_0123': 0.950614,
						 'r_0264__kms_s_1458r_0264': 0.549,
						 'r_0707__Vmax_r_0707': 1.2166,
						 'r_1812__s_0881_or_1812': 0.549,
						 'r_0421__Vmax_r_0421': 0.00599719,
						 'r_0515__Vmax_r_0515': 53.3829,
						 'r_0374__Keq_r_0374': 1.1,
						 'r_1816__s_0124_or_1816': 0.549,
						 'r_0393__kms_s_0710r_0393': 0.549,
						 'r_0526__Keq_r_0526': 2.21027,
						 'r_0586__kms_s_1087r_0586': 0.0867353,
						 'r_1672__Vmax_r_1672': 0.026268,
						 'r_0993__Vmax_r_0993': 0.0627,
						 'r_1038__kms_s_0419r_1038': 0.549,
						 'r_0538__kmp_s_0470r_0538': 1.0,
						 'r_0387__kmp_s_0605r_0387': 0.549,
						 'r_0058__kmp_s_1082r_0058': 1.50326,
						 'r_0429__kms_s_0763_br_0429': 0.549,
						 'r_0674__Vmax_r_0674': 1.0703,
						 'r_0170__kmp_s_1053r_0170': 0.549,
						 'r_0539__kms_s_0740r_0539': 0.549,
						 'r_1812__a_s_0446r_1812': 59.276,
						 'r_0267__kmp_s_1091r_0267': 0.549,
						 'r_0232__kmp_s_1207r_0232': 0.549,
						 'r_0888__kmp_s_0158r_0888': 0.549,
						 'r_0235__kms_s_0899r_0235': 0.549,
						 'r_1812__V_o': 0.0555,
						 'r_0221__kmp_s_1277r_0221': 0.0605905,
						 'r_1812__a_s_0911r_1812': 0.075041,
						 'r_0873__Vmax_r_0873': 0.01232,
						 'r_0721__kmp_s_1096r_0721': 0.549,
						 'r_0233__Vmax_r_0233': 6.2447,
						 'r_1042__kms_s_0088r_1042': 0.549,
						 'r_1042__Keq_r_1042': 0.0874316,
						 'r_0707__Keq_r_0707': 1.1,
						 'r_0464__kmp_s_0470r_0464': 1.0,
						 'r_0394__Keq_r_0394': 0.331541,
						 'r_0268__kms_s_0124r_0268': 0.549,
						 'r_1042__Vmax_r_1042': 0.187549,
						 'r_0025__Vmax_r_0025': 0.764496,
						 'r_0951__kms_s_1521r_0951': 0.549,
						 'r_0246__kmp_s_0763_br_0246': 0.549,
						 'r_0439__kmp_s_1329r_0439': 0.549,
						 'r_0345__kms_s_0400r_0345': 1.71907,
						 'r_0547__kmp_s_1411r_0547': 0.549,
						 'r_0538__Vmax_r_0538': 9.5887,
						 'r_0547__Keq_r_0547': 0.6039,
						 'r_0488__kms_s_0692r_0488': 0.549,
						 'r_0887__kms_s_1066r_0887': 0.549,
						 'r_1066__Keq_r_1066': 0.698801,
						 'r_1812__a_s_0899r_1812': 0.268,
						 'r_0588__kms_s_0919r_0588': 0.549,
						 'r_0688__kmp_s_1082r_0688': 1.50326,
						 'r_0575__kms_s_1082r_0575': 1.50326,
						 'r_0539__kmp_s_0943r_0539': 0.549,
						 'r_1816__s_0663_or_1816': 0.549,
						 'r_0442__kms_s_1140r_0442': 0.549,
						 'r_0249__kmp_s_0766_br_0249': 0.1,
						 'r_0485__kmp_s_1434_br_0485': 0.549,
						 'r_0277__kmp_s_0899r_0277': 0.549,
						 'r_0347__kms_s_1087r_0347': 0.0867353,
						 'r_0425__kms_s_1096r_0425': 0.549,
						 'r_0496__kmp_s_0195r_0496': 0.549,
						 'r_0467__kmp_s_1434_br_0467': 0.549,
						 'r_0640__Vmax_r_0640': 1.15192,
						 'r_1247__kms_s_0650r_1247': 50.0,
						 'r_0793__Vmax_r_0793': 0.52591,
						 'r_0702__Vmax_r_0702': 0.439228,
						 'r_0608__kmp_s_0470r_0608': 1.0,
						 'r_1066__kmp_s_0624r_1066': 0.549,
						 'r_0940__kmp_s_0380r_0940': 0.549,
						 'r_0794__kmp_s_0470r_0794': 1.0,
						 'r_0977__kmp_s_0400r_0977': 1.71907,
						 'r_0936__kmp_s_0939r_0936': 0.549,
						 'r_0360__kms_s_0562r_0360': 0.549,
						 'r_0941__Keq_r_0941': 2.8449,
						 'r_1812__a_s_0920r_1812': 0.17152,
						 'r_0467__kms_s_0763_br_0467': 0.549,
						 'r_0771__kms_s_0521r_0771': 0.549,
						 'r_0674__kmp_s_0925r_0674': 0.549,
						 'r_0170__kms_s_0816r_0170': 0.549,
						 'r_0398__kms_s_0193r_0398': 0.0515066,
						 'r_0298__Keq_r_0298': 0.331541,
						 'r_0551__kmp_s_0605r_0551': 0.549,
						 'r_1672__kmp_s_0386r_1672': 0.549,
						 'r_1816__s_0824_or_1816': 0.549,
						 'r_1073__Keq_r_1073': 2.00364,
						 'r_0606__kmp_s_1434_br_0606': 0.549,
						 'r_0883__kms_s_0470r_0883': 1.0,
						 'r_0340__kms_s_1117r_0340': 0.549,
						 'r_1066__Vmax_r_1066': 0.025718,
						 'r_0021__kms_s_1434_br_0021': 0.549,
						 'r_0393__kmp_s_0706r_0393': 0.549,
						 'r_0783__kmp_s_0763_br_0783': 0.549,
						 'r_0304__Keq_r_0304': 1.1,
						 'r_0425__kmp_s_0987r_0425': 0.549,
						 'r_0245__Vmax_r_0245': 0.32109,
						 'r_0853__kms_s_0485r_0853': 0.549,
						 'r_0866__Keq_r_0866': 6.7,
						 'r_0853__kms_s_0943r_0853': 0.549,
						 'r_0567__Keq_r_0567': 1.73154,
						 'r_1073__kmp_s_0960r_1073': 1.0,
						 'r_0551__kmp_s_0899r_0551': 0.549,
						 'r_0112__kmp_s_0150r_0112': 0.549,
						 'r_0621__Vmax_r_0621': 0.00127051,
						 'r_0720__kmp_s_0763_br_0720': 0.549,
						 'r_1007__kmp_s_1207r_1007': 0.549,
						 'r_0465__Vmax_r_0465': 0.0179399,
						 'r_0567__kms_s_0752r_0567': 0.549,
						 'r_0888__kmp_s_0899r_0888': 0.549,
						 'r_0261__kms_s_1457r_0261': 0.549,
						 'r_1816__a_s_0090r_1816': 0.001531,
						 'r_0063__kms_s_0170r_0063': 0.549,
						 'r_0423__kms_s_0763_br_0423': 0.549,
						 'r_0059__kms_s_0763_br_0059': 0.549,
						 'r_0976__kmp_s_1091r_0976': 0.549,
						 'r_0229__kmp_s_0877r_0229': 0.549,
						 'r_0607__kms_s_1082r_0607': 1.50326,
						 'r_0093__kms_s_1096r_0093': 0.549,
						 'r_0530__kms_s_1087r_0530': 0.0867353,
						 'r_0232__kms_s_0881r_0232': 0.549,
						 'r_0515__kms_s_0446r_0515': 1.09208,
						 'r_1812__s_0446_or_1812': 1.09208,
						 'r_0111__kms_s_0150r_0111': 0.549,
						 'r_0991__kmp_s_0040r_0991': 0.549,
						 'r_0225__kms_s_0017r_0225': 0.549}


	### reactions with pathway annotation

	########### CDP-diacylglycerol biosynthesis ###########

	# CDP-diacylglycerol synthase
	r_0284 = 'intracellular * r_0284__Vmax_r_0284 * ( pow ( 1.0 / r_0284__kms_s_0521r_0284 , 1.0 ) * pow ( 1.0 / r_0284__kms_s_0763_br_0284 , 1.0 ) * pow ( 1.0 / r_0284__kms_s_1215r_0284 , 1.0 ) * ( pow ( s_0521 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1215 , 1.0 ) - pow ( s_0485 , 1.0 ) * pow ( s_0605 , 1.0 ) / r_0284__Keq_r_0284 ) / ( ( 1.0 + s_0521 / r_0284__kms_s_0521r_0284 ) * ( 1.0 + s_0763_b / r_0284__kms_s_0763_br_0284 ) * ( 1.0 + s_1215 / r_0284__kms_s_1215r_0284 ) + ( 1.0 + s_0485 / r_0284__kmp_s_0485r_0284 ) * ( 1.0 + s_0605 / r_0284__kmp_s_0605r_0284 ) - 1.0 ) ) / intracellular '

	########### S-adenosylmethionine biosynthesis ###########

	# methionine adenosyltransferase
	r_0701 = 'intracellular * r_0701__Vmax_r_0701 * ( pow ( 1.0 / r_0701__kms_s_0446r_0701 , 1.0 ) * pow ( 1.0 / r_0701__kms_s_0933r_0701 , 1.0 ) * pow ( 1.0 / r_0701__kms_s_1434_br_0701 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_0933 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0605 , 1.0 ) * pow ( s_1207 , 1.0 ) * pow ( s_1293 , 1.0 ) / r_0701__Keq_r_0701 ) / ( ( 1.0 + s_0446 / r_0701__kms_s_0446r_0701 ) * ( 1.0 + s_0933 / r_0701__kms_s_0933r_0701 ) * ( 1.0 + s_1434_b / r_0701__kms_s_1434_br_0701 ) + ( 1.0 + s_0605 / r_0701__kmp_s_0605r_0701 ) * ( 1.0 + s_1207 / r_0701__kmp_s_1207r_0701 ) * ( 1.0 + s_1293 / r_0701__kmp_s_1293r_0701 ) - 1.0 ) ) / intracellular '

	########### S-adenosylmethionine cycle ###########

	# adenosylhomocysteinase
	r_0159 = 'intracellular * r_0159__Vmax_r_0159 * ( pow ( 1.0 / r_0159__kms_s_1290r_0159 , 1.0 ) * pow ( 1.0 / r_0159__kms_s_1434_br_0159 , 1.0 ) * ( pow ( s_1290 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0393 , 1.0 ) * pow ( s_0917 , 1.0 ) / r_0159__Keq_r_0159 ) / ( ( 1.0 + s_1290 / r_0159__kms_s_1290r_0159 ) * ( 1.0 + s_1434_b / r_0159__kms_s_1434_br_0159 ) + ( 1.0 + s_0393 / r_0159__kmp_s_0393r_0159 ) * ( 1.0 + s_0917 / r_0159__kmp_s_0917r_0159 ) - 1.0 ) ) / intracellular '

	########### TCA cycle, aerobic respiration ###########

	# cis-aconitate(3-) to isocitrate
	r_0307 = 'intracellular * r_0307__Vmax_r_0307 * ( pow ( 1.0 / r_0307__kms_s_0501r_0307 , 1.0 ) * pow ( 1.0 / r_0307__kms_s_1434_br_0307 , 1.0 ) * ( pow ( s_0501 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0847 , 1.0 ) / r_0307__Keq_r_0307 ) / ( ( 1.0 + s_0501 / r_0307__kms_s_0501r_0307 ) * ( 1.0 + s_1434_b / r_0307__kms_s_1434_br_0307 ) + 1.0 + s_0847 / r_0307__kmp_s_0847r_0307 - 1.0 ) ) / intracellular '
	# citrate synthase
	r_0328 = 'intracellular * r_0328__Vmax_r_0328 * ( pow ( 1.0 / r_0328__kms_s_0380r_0328 , 1.0 ) * pow ( 1.0 / r_0328__kms_s_1156r_0328 , 1.0 ) * pow ( 1.0 / r_0328__kms_s_1434_br_0328 , 1.0 ) * ( pow ( s_0380 , 1.0 ) * pow ( s_1156 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0507 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0328__Keq_r_0328 ) / ( ( 1.0 + s_0380 / r_0328__kms_s_0380r_0328 ) * ( 1.0 + s_1156 / r_0328__kms_s_1156r_0328 ) * ( 1.0 + s_1434_b / r_0328__kms_s_1434_br_0328 ) + ( 1.0 + s_0507 / r_0328__kmp_s_0507r_0328 ) * ( 1.0 + s_0514 / r_0328__kmp_s_0514r_0328 ) * ( 1.0 + s_0763_b / r_0328__kmp_s_0763_br_0328 ) - 1.0 ) ) / intracellular '
	# citrate to cis-aconitate(3-)
	r_0330 = 'intracellular * r_0330__Vmax_r_0330 * ( pow ( 1.0 / r_0330__kms_s_0507r_0330 , 1.0 ) * ( pow ( s_0507 , 1.0 ) - pow ( s_0501 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0330__Keq_r_0330 ) / ( 1.0 + s_0507 / r_0330__kms_s_0507r_0330 + ( 1.0 + s_0501 / r_0330__kmp_s_0501r_0330 ) * ( 1.0 + s_1434_b / r_0330__kmp_s_1434_br_0330 ) - 1.0 ) ) / intracellular '
	# fumarase
	r_0485 = 'intracellular * r_0485__Vmax_r_0485 * ( pow ( 1.0 / r_0485__kms_s_0069r_0485 , 1.0 ) * ( pow ( s_0069 , 1.0 ) - pow ( s_0692 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0485__Keq_r_0485 ) / ( 1.0 + s_0069 / r_0485__kms_s_0069r_0485 + ( 1.0 + s_0692 / r_0485__kmp_s_0692r_0485 ) * ( 1.0 + s_1434_b / r_0485__kmp_s_1434_br_0485 ) - 1.0 ) ) / intracellular '
	# fumarate reductase
	r_0488 = 'intracellular * r_0488__Vmax_r_0488 * ( pow ( 1.0 / r_0488__kms_s_0659r_0488 , 1.0 ) * pow ( 1.0 / r_0488__kms_s_0692r_0488 , 1.0 ) * ( pow ( s_0659 , 1.0 ) * pow ( s_0692 , 1.0 ) - pow ( s_0657 , 1.0 ) * pow ( s_1338 , 1.0 ) / r_0488__Keq_r_0488 ) / ( ( 1.0 + s_0659 / r_0488__kms_s_0659r_0488 ) * ( 1.0 + s_0692 / r_0488__kms_s_0692r_0488 ) + ( 1.0 + s_0657 / r_0488__kmp_s_0657r_0488 ) * ( 1.0 + s_1338 / r_0488__kmp_s_1338r_0488 ) - 1.0 ) ) / intracellular '
	# glycine cleavage system
	r_0538 = 'intracellular * r_0538__Vmax_r_0538 * ( pow ( 1.0 / r_0538__kms_s_0309r_0538 , 1.0 ) * pow ( 1.0 / r_0538__kms_s_0740r_0538 , 1.0 ) * pow ( 1.0 / r_0538__kms_s_1082r_0538 , 1.0 ) * ( pow ( s_0309 , 1.0 ) * pow ( s_0740 , 1.0 ) * pow ( s_1082 , 1.0 ) - pow ( s_0307 , 1.0 ) * pow ( s_0430 , 1.0 ) * pow ( s_0470 , 1.0 ) * pow ( s_1087 , 1.0 ) / r_0538__Keq_r_0538 ) / ( ( 1.0 + s_0309 / r_0538__kms_s_0309r_0538 ) * ( 1.0 + s_0740 / r_0538__kms_s_0740r_0538 ) * ( 1.0 + s_1082 / r_0538__kms_s_1082r_0538 ) + ( 1.0 + s_0307 / r_0538__kmp_s_0307r_0538 ) * ( 1.0 + s_0430 / r_0538__kmp_s_0430r_0538 ) * ( 1.0 + s_0470 / r_0538__kmp_s_0470r_0538 ) * ( 1.0 + s_1087 / r_0538__kmp_s_1087r_0538 ) - 1.0 ) ) / intracellular '
	# malate dehydrogenase
	r_0688 = 'intracellular * r_0688__Vmax_r_0688 * ( pow ( 1.0 / r_0688__kms_s_0763_br_0688 , 1.0 ) * pow ( 1.0 / r_0688__kms_s_1087r_0688 , 1.0 ) * pow ( 1.0 / r_0688__kms_s_1156r_0688 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_1087 , 1.0 ) * pow ( s_1156 , 1.0 ) - pow ( s_0069 , 1.0 ) * pow ( s_1082 , 1.0 ) / r_0688__Keq_r_0688 ) / ( ( 1.0 + s_0763_b / r_0688__kms_s_0763_br_0688 ) * ( 1.0 + s_1087 / r_0688__kms_s_1087r_0688 ) * ( 1.0 + s_1156 / r_0688__kms_s_1156r_0688 ) + ( 1.0 + s_0069 / r_0688__kmp_s_0069r_0688 ) * ( 1.0 + s_1082 / r_0688__kmp_s_1082r_0688 ) - 1.0 ) ) / intracellular '
	# pyruvate carboxylase
	r_0937 = 'intracellular * r_0937__Vmax_r_0937 * ( pow ( 1.0 / r_0937__kms_s_0446r_0937 , 1.0 ) * pow ( 1.0 / r_0937__kms_s_0458r_0937 , 1.0 ) * pow ( 1.0 / r_0937__kms_s_1277r_0937 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_0458 , 1.0 ) * pow ( s_1277 , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1156 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0937__Keq_r_0937 ) / ( ( 1.0 + s_0446 / r_0937__kms_s_0446r_0937 ) * ( 1.0 + s_0458 / r_0937__kms_s_0458r_0937 ) * ( 1.0 + s_1277 / r_0937__kms_s_1277r_0937 ) + ( 1.0 + s_0400 / r_0937__kmp_s_0400r_0937 ) * ( 1.0 + s_0763_b / r_0937__kmp_s_0763_br_0937 ) * ( 1.0 + s_1156 / r_0937__kmp_s_1156r_0937 ) * ( 1.0 + s_1207 / r_0937__kmp_s_1207r_0937 ) - 1.0 ) ) / intracellular '
	# pyruvate dehydrogenase
	r_0940 = 'intracellular * r_0940__Vmax_r_0940 * ( pow ( 1.0 / r_0940__kms_s_0514r_0940 , 1.0 ) * pow ( 1.0 / r_0940__kms_s_1082r_0940 , 1.0 ) * pow ( 1.0 / r_0940__kms_s_1277r_0940 , 1.0 ) * ( pow ( s_0514 , 1.0 ) * pow ( s_1082 , 1.0 ) * pow ( s_1277 , 1.0 ) - pow ( s_0380 , 1.0 ) * pow ( s_0470 , 1.0 ) * pow ( s_1087 , 1.0 ) / r_0940__Keq_r_0940 ) / ( ( 1.0 + s_0514 / r_0940__kms_s_0514r_0940 ) * ( 1.0 + s_1082 / r_0940__kms_s_1082r_0940 ) * ( 1.0 + s_1277 / r_0940__kms_s_1277r_0940 ) + ( 1.0 + s_0380 / r_0940__kmp_s_0380r_0940 ) * ( 1.0 + s_0470 / r_0940__kmp_s_0470r_0940 ) * ( 1.0 + s_1087 / r_0940__kmp_s_1087r_0940 ) - 1.0 ) ) / intracellular '
	# succinate-CoA ligase (ADP-forming)
	r_1003 = 'intracellular * r_1003__Vmax_r_1003 * ( pow ( 1.0 / r_1003__kms_s_0446r_1003 , 1.0 ) * pow ( 1.0 / r_1003__kms_s_0514r_1003 , 1.0 ) * pow ( 1.0 / r_1003__kms_s_1338r_1003 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_1338 , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_1207 , 1.0 ) * pow ( s_1342 , 1.0 ) / r_1003__Keq_r_1003 ) / ( ( 1.0 + s_0446 / r_1003__kms_s_0446r_1003 ) * ( 1.0 + s_0514 / r_1003__kms_s_0514r_1003 ) * ( 1.0 + s_1338 / r_1003__kms_s_1338r_1003 ) + ( 1.0 + s_0400 / r_1003__kmp_s_0400r_1003 ) * ( 1.0 + s_1207 / r_1003__kmp_s_1207r_1003 ) * ( 1.0 + s_1342 / r_1003__kmp_s_1342r_1003 ) - 1.0 ) ) / intracellular '

	########### alanine biosynthesis ###########

	# L-alanine transaminase
	r_0647 = 'intracellular * r_0647__Vmax_r_0647 * ( pow ( 1.0 / r_0647__kms_s_0899r_0647 , 1.0 ) * pow ( 1.0 / r_0647__kms_s_1277r_0647 , 1.0 ) * ( pow ( s_0899 , 1.0 ) * pow ( s_1277 , 1.0 ) - pow ( s_0185 , 1.0 ) * pow ( s_0863 , 1.0 ) / r_0647__Keq_r_0647 ) / ( ( 1.0 + s_0899 / r_0647__kms_s_0899r_0647 ) * ( 1.0 + s_1277 / r_0647__kms_s_1277r_0647 ) + ( 1.0 + s_0185 / r_0647__kmp_s_0185r_0647 ) * ( 1.0 + s_0863 / r_0647__kmp_s_0863r_0647 ) - 1.0 ) ) / intracellular '

	########### arginine biosynthesis ###########

	# acteylornithine transaminase
	r_0133 = 'intracellular * r_0133__Vmax_r_0133 * ( pow ( 1.0 / r_0133__kms_s_0149r_0133 , 1.0 ) * pow ( 1.0 / r_0133__kms_s_0899r_0133 , 1.0 ) * ( pow ( s_0149 , 1.0 ) * pow ( s_0899 , 1.0 ) - pow ( s_0185 , 1.0 ) * pow ( s_1051 , 1.0 ) / r_0133__Keq_r_0133 ) / ( ( 1.0 + s_0149 / r_0133__kms_s_0149r_0133 ) * ( 1.0 + s_0899 / r_0133__kms_s_0899r_0133 ) + ( 1.0 + s_0185 / r_0133__kmp_s_0185r_0133 ) * ( 1.0 + s_1051 / r_0133__kmp_s_1051r_0133 ) - 1.0 ) ) / intracellular '
	# argininosuccinate lyase
	r_0225 = 'intracellular * r_0225__Vmax_r_0225 * ( pow ( 1.0 / r_0225__kms_s_0017r_0225 , 1.0 ) * ( pow ( s_0017 , 1.0 ) - pow ( s_0692 , 1.0 ) * pow ( s_0873 , 1.0 ) / r_0225__Keq_r_0225 ) / ( 1.0 + s_0017 / r_0225__kms_s_0017r_0225 + ( 1.0 + s_0692 / r_0225__kmp_s_0692r_0225 ) * ( 1.0 + s_0873 / r_0225__kmp_s_0873r_0225 ) - 1.0 ) ) / intracellular '
	# argininosuccinate synthase
	r_0226 = 'intracellular * r_0226__Vmax_r_0226 * ( pow ( 1.0 / r_0226__kms_s_0446r_0226 , 1.0 ) * pow ( 1.0 / r_0226__kms_s_0881r_0226 , 1.0 ) * pow ( 1.0 / r_0226__kms_s_0887r_0226 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_0881 , 1.0 ) * pow ( s_0887 , 1.0 ) - pow ( s_0017 , 1.0 ) * pow ( s_0434 , 1.0 ) * pow ( s_0605 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0226__Keq_r_0226 ) / ( ( 1.0 + s_0446 / r_0226__kms_s_0446r_0226 ) * ( 1.0 + s_0881 / r_0226__kms_s_0881r_0226 ) * ( 1.0 + s_0887 / r_0226__kms_s_0887r_0226 ) + ( 1.0 + s_0017 / r_0226__kmp_s_0017r_0226 ) * ( 1.0 + s_0434 / r_0226__kmp_s_0434r_0226 ) * ( 1.0 + s_0605 / r_0226__kmp_s_0605r_0226 ) * ( 1.0 + s_0763_b / r_0226__kmp_s_0763_br_0226 ) - 1.0 ) ) / intracellular '
	# ornithine transacetylase
	r_0791 = 'intracellular * r_0791__Vmax_r_0791 * ( pow ( 1.0 / r_0791__kms_s_0899r_0791 , 1.0 ) * pow ( 1.0 / r_0791__kms_s_1051r_0791 , 1.0 ) * ( pow ( s_0899 , 1.0 ) * pow ( s_1051 , 1.0 ) - pow ( s_1071 , 1.0 ) * pow ( s_1151 , 1.0 ) / r_0791__Keq_r_0791 ) / ( ( 1.0 + s_0899 / r_0791__kms_s_0899r_0791 ) * ( 1.0 + s_1051 / r_0791__kms_s_1051r_0791 ) + ( 1.0 + s_1071 / r_0791__kmp_s_1071r_0791 ) * ( 1.0 + s_1151 / r_0791__kmp_s_1151r_0791 ) - 1.0 ) ) / intracellular '

	########### asparagine biosynthesis ###########

	# asparagine synthase (glutamine-hydrolysing)
	r_0229 = 'intracellular * r_0229__Vmax_r_0229 * ( pow ( 1.0 / r_0229__kms_s_0446r_0229 , 1.0 ) * pow ( 1.0 / r_0229__kms_s_0881r_0229 , 1.0 ) * pow ( 1.0 / r_0229__kms_s_0907r_0229 , 1.0 ) * pow ( 1.0 / r_0229__kms_s_1434_br_0229 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_0881 , 1.0 ) * pow ( s_0907 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0434 , 1.0 ) * pow ( s_0605 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_0877 , 1.0 ) * pow ( s_0899 , 1.0 ) / r_0229__Keq_r_0229 ) / ( ( 1.0 + s_0446 / r_0229__kms_s_0446r_0229 ) * ( 1.0 + s_0881 / r_0229__kms_s_0881r_0229 ) * ( 1.0 + s_0907 / r_0229__kms_s_0907r_0229 ) * ( 1.0 + s_1434_b / r_0229__kms_s_1434_br_0229 ) + ( 1.0 + s_0434 / r_0229__kmp_s_0434r_0229 ) * ( 1.0 + s_0605 / r_0229__kmp_s_0605r_0229 ) * ( 1.0 + s_0763_b / r_0229__kmp_s_0763_br_0229 ) * ( 1.0 + s_0877 / r_0229__kmp_s_0877r_0229 ) * ( 1.0 + s_0899 / r_0229__kmp_s_0899r_0229 ) - 1.0 ) ) / intracellular '

	########### citrulline biosynthesis ###########

	# carbamoyl-phosphate synthase (glutamine-hydrolysing)
	r_0277 = 'intracellular * r_0277__Vmax_r_0277 * ( pow ( 1.0 / r_0277__kms_s_0446r_0277 , 2.0 ) * pow ( 1.0 / r_0277__kms_s_0458r_0277 , 1.0 ) * pow ( 1.0 / r_0277__kms_s_0907r_0277 , 1.0 ) * pow ( 1.0 / r_0277__kms_s_1434_br_0277 , 1.0 ) * ( pow ( s_0446 , 2.0 ) * pow ( s_0458 , 1.0 ) * pow ( s_0907 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0400 , 2.0 ) * pow ( s_0469 , 1.0 ) * pow ( s_0763_b , 2.0 ) * pow ( s_0899 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0277__Keq_r_0277 ) / ( ( 1.0 + s_0446 / r_0277__kms_s_0446r_0277 ) * ( 1.0 + s_0458 / r_0277__kms_s_0458r_0277 ) * ( 1.0 + s_0907 / r_0277__kms_s_0907r_0277 ) * ( 1.0 + s_1434_b / r_0277__kms_s_1434_br_0277 ) + ( 1.0 + s_0400 / r_0277__kmp_s_0400r_0277 ) * ( 1.0 + s_0469 / r_0277__kmp_s_0469r_0277 ) * ( 1.0 + s_0763_b / r_0277__kmp_s_0763_br_0277 ) * ( 1.0 + s_0899 / r_0277__kmp_s_0899r_0277 ) * ( 1.0 + s_1207 / r_0277__kmp_s_1207r_0277 ) - 1.0 ) ) / intracellular '
	# ornithine carbamoyltransferase
	r_0789 = 'intracellular * r_0789__Vmax_r_0789 * ( pow ( 1.0 / r_0789__kms_s_0469r_0789 , 1.0 ) * pow ( 1.0 / r_0789__kms_s_1151r_0789 , 1.0 ) * ( pow ( s_0469 , 1.0 ) * pow ( s_1151 , 1.0 ) - pow ( s_0763_b , 1.0 ) * pow ( s_0887 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0789__Keq_r_0789 ) / ( ( 1.0 + s_0469 / r_0789__kms_s_0469r_0789 ) * ( 1.0 + s_1151 / r_0789__kms_s_1151r_0789 ) + ( 1.0 + s_0763_b / r_0789__kmp_s_0763_br_0789 ) * ( 1.0 + s_0887 / r_0789__kmp_s_0887r_0789 ) * ( 1.0 + s_1207 / r_0789__kmp_s_1207r_0789 ) - 1.0 ) ) / intracellular '

	########### de novo biosynthesis of pyrimidine deoxyribonucleotides ###########

	# ribonucleoside-diphosphate reductase (GDP)
	r_0955 = 'intracellular * r_0955__Vmax_r_0955 * ( pow ( 1.0 / r_0955__kms_s_0706r_0955 , 1.0 ) * pow ( 1.0 / r_0955__kms_s_1521r_0955 , 1.0 ) * ( pow ( s_0706 , 1.0 ) * pow ( s_1521 , 1.0 ) - pow ( s_0591 , 1.0 ) * pow ( s_1434_b , 1.0 ) * pow ( s_1517 , 1.0 ) / r_0955__Keq_r_0955 ) / ( ( 1.0 + s_0706 / r_0955__kms_s_0706r_0955 ) * ( 1.0 + s_1521 / r_0955__kms_s_1521r_0955 ) + ( 1.0 + s_0591 / r_0955__kmp_s_0591r_0955 ) * ( 1.0 + s_1434_b / r_0955__kmp_s_1434_br_0955 ) * ( 1.0 + s_1517 / r_0955__kmp_s_1517r_0955 ) - 1.0 ) ) / intracellular '
	# ribonucleoside-diphosphate reductase (UDP)
	r_0957 = 'intracellular * r_0957__Vmax_r_0957 * ( pow ( 1.0 / r_0957__kms_s_1411r_0957 , 1.0 ) * pow ( 1.0 / r_0957__kms_s_1521r_0957 , 1.0 ) * ( pow ( s_1411 , 1.0 ) * pow ( s_1521 , 1.0 ) - pow ( s_0622 , 1.0 ) * pow ( s_1434_b , 1.0 ) * pow ( s_1517 , 1.0 ) / r_0957__Keq_r_0957 ) / ( ( 1.0 + s_1411 / r_0957__kms_s_1411r_0957 ) * ( 1.0 + s_1521 / r_0957__kms_s_1521r_0957 ) + ( 1.0 + s_0622 / r_0957__kmp_s_0622r_0957 ) * ( 1.0 + s_1434_b / r_0957__kmp_s_1434_br_0957 ) * ( 1.0 + s_1517 / r_0957__kmp_s_1517r_0957 ) - 1.0 ) ) / intracellular '
	# thymidylate synthase
	r_1032 = 'intracellular * r_1032__Vmax_r_1032 * ( pow ( 1.0 / r_1032__kms_s_0307r_1032 , 1.0 ) * pow ( 1.0 / r_1032__kms_s_0624r_1032 , 1.0 ) * ( pow ( s_0307 , 1.0 ) * pow ( s_0624 , 1.0 ) - pow ( s_0601 , 1.0 ) * pow ( s_0619 , 1.0 ) / r_1032__Keq_r_1032 ) / ( ( 1.0 + s_0307 / r_1032__kms_s_0307r_1032 ) * ( 1.0 + s_0624 / r_1032__kms_s_0624r_1032 ) + ( 1.0 + s_0601 / r_1032__kmp_s_0601r_1032 ) * ( 1.0 + s_0619 / r_1032__kmp_s_0619r_1032 ) - 1.0 ) ) / intracellular '

	########### de novo biosynthesis of pyrimidine ribonucleotides ###########

	# aspartate carbamoyltransferase
	r_0232 = 'intracellular * r_0232__Vmax_r_0232 * ( pow ( 1.0 / r_0232__kms_s_0469r_0232 , 1.0 ) * pow ( 1.0 / r_0232__kms_s_0881r_0232 , 1.0 ) * ( pow ( s_0469 , 1.0 ) * pow ( s_0881 , 1.0 ) - pow ( s_0763_b , 1.0 ) * pow ( s_1073 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0232__Keq_r_0232 ) / ( ( 1.0 + s_0469 / r_0232__kms_s_0469r_0232 ) * ( 1.0 + s_0881 / r_0232__kms_s_0881r_0232 ) + ( 1.0 + s_0763_b / r_0232__kmp_s_0763_br_0232 ) * ( 1.0 + s_1073 / r_0232__kmp_s_1073r_0232 ) * ( 1.0 + s_1207 / r_0232__kmp_s_1207r_0232 ) - 1.0 ) ) / intracellular '
	# carbamoyl-phosphate synthase (glutamine-hydrolysing)
	r_0277 = 'intracellular * r_0277__Vmax_r_0277 * ( pow ( 1.0 / r_0277__kms_s_0446r_0277 , 2.0 ) * pow ( 1.0 / r_0277__kms_s_0458r_0277 , 1.0 ) * pow ( 1.0 / r_0277__kms_s_0907r_0277 , 1.0 ) * pow ( 1.0 / r_0277__kms_s_1434_br_0277 , 1.0 ) * ( pow ( s_0446 , 2.0 ) * pow ( s_0458 , 1.0 ) * pow ( s_0907 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0400 , 2.0 ) * pow ( s_0469 , 1.0 ) * pow ( s_0763_b , 2.0 ) * pow ( s_0899 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0277__Keq_r_0277 ) / ( ( 1.0 + s_0446 / r_0277__kms_s_0446r_0277 ) * ( 1.0 + s_0458 / r_0277__kms_s_0458r_0277 ) * ( 1.0 + s_0907 / r_0277__kms_s_0907r_0277 ) * ( 1.0 + s_1434_b / r_0277__kms_s_1434_br_0277 ) + ( 1.0 + s_0400 / r_0277__kmp_s_0400r_0277 ) * ( 1.0 + s_0469 / r_0277__kmp_s_0469r_0277 ) * ( 1.0 + s_0763_b / r_0277__kmp_s_0763_br_0277 ) * ( 1.0 + s_0899 / r_0277__kmp_s_0899r_0277 ) * ( 1.0 + s_1207 / r_0277__kmp_s_1207r_0277 ) - 1.0 ) ) / intracellular '
	# CTP synthase (NH3)
	r_0336 = 'intracellular * r_0336__Vmax_r_0336 * ( pow ( 1.0 / r_0336__kms_s_0430r_0336 , 1.0 ) * pow ( 1.0 / r_0336__kms_s_0446r_0336 , 1.0 ) * pow ( 1.0 / r_0336__kms_s_1430r_0336 , 1.0 ) * ( pow ( s_0430 , 1.0 ) * pow ( s_0446 , 1.0 ) * pow ( s_1430 , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_0521 , 1.0 ) * pow ( s_0763_b , 2.0 ) * pow ( s_1207 , 1.0 ) / r_0336__Keq_r_0336 ) / ( ( 1.0 + s_0430 / r_0336__kms_s_0430r_0336 ) * ( 1.0 + s_0446 / r_0336__kms_s_0446r_0336 ) * ( 1.0 + s_1430 / r_0336__kms_s_1430r_0336 ) + ( 1.0 + s_0400 / r_0336__kmp_s_0400r_0336 ) * ( 1.0 + s_0521 / r_0336__kmp_s_0521r_0336 ) * ( 1.0 + s_0763_b / r_0336__kmp_s_0763_br_0336 ) * ( 1.0 + s_1207 / r_0336__kmp_s_1207r_0336 ) - 1.0 ) ) / intracellular '
	# cytidylate kinase (CMP)
	r_0345 = 'intracellular * r_0345__Vmax_r_0345 * ( pow ( 1.0 / r_0345__kms_s_0400r_0345 , 1.0 ) * pow ( 1.0 / r_0345__kms_s_0481r_0345 , 1.0 ) * ( pow ( s_0400 , 1.0 ) * pow ( s_0481 , 1.0 ) - pow ( s_0446 , 1.0 ) * pow ( s_0511 , 1.0 ) / r_0345__Keq_r_0345 ) / ( ( 1.0 + s_0400 / r_0345__kms_s_0400r_0345 ) * ( 1.0 + s_0481 / r_0345__kms_s_0481r_0345 ) + ( 1.0 + s_0446 / r_0345__kmp_s_0446r_0345 ) * ( 1.0 + s_0511 / r_0345__kmp_s_0511r_0345 ) - 1.0 ) ) / intracellular '
	# dihydoorotic acid dehydrogenase
	r_0374 = 'intracellular * r_0374__Vmax_r_0374 * ( pow ( 1.0 / r_0374__kms_s_0064r_0374 , 1.0 ) * pow ( 1.0 / r_0374__kms_s_1160r_0374 , 1.0 ) * ( pow ( s_0064 , 1.0 ) * pow ( s_1160 , 1.0 ) - pow ( s_0801 , 1.0 ) * pow ( s_1154 , 1.0 ) / r_0374__Keq_r_0374 ) / ( ( 1.0 + s_0064 / r_0374__kms_s_0064r_0374 ) * ( 1.0 + s_1160 / r_0374__kms_s_1160r_0374 ) + ( 1.0 + s_0801 / r_0374__kmp_s_0801r_0374 ) * ( 1.0 + s_1154 / r_0374__kmp_s_1154r_0374 ) - 1.0 ) ) / intracellular '
	# dihydroorotase
	r_0381 = 'intracellular * r_0381__Vmax_r_0381 * ( pow ( 1.0 / r_0381__kms_s_0763_br_0381 , 1.0 ) * pow ( 1.0 / r_0381__kms_s_1073r_0381 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_1073 , 1.0 ) - pow ( s_0064 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0381__Keq_r_0381 ) / ( ( 1.0 + s_0763_b / r_0381__kms_s_0763_br_0381 ) * ( 1.0 + s_1073 / r_0381__kms_s_1073r_0381 ) + ( 1.0 + s_0064 / r_0381__kmp_s_0064r_0381 ) * ( 1.0 + s_1434_b / r_0381__kmp_s_1434_br_0381 ) - 1.0 ) ) / intracellular '
	# orotate phosphoribosyltransferase
	r_0793 = 'intracellular * r_0793__Vmax_r_0793 * ( pow ( 1.0 / r_0793__kms_s_0331r_0793 , 1.0 ) * pow ( 1.0 / r_0793__kms_s_1154r_0793 , 1.0 ) * ( pow ( s_0331 , 1.0 ) * pow ( s_1154 , 1.0 ) - pow ( s_0605 , 1.0 ) * pow ( s_1155 , 1.0 ) / r_0793__Keq_r_0793 ) / ( ( 1.0 + s_0331 / r_0793__kms_s_0331r_0793 ) * ( 1.0 + s_1154 / r_0793__kms_s_1154r_0793 ) + ( 1.0 + s_0605 / r_0793__kmp_s_0605r_0793 ) * ( 1.0 + s_1155 / r_0793__kmp_s_1155r_0793 ) - 1.0 ) ) / intracellular '
	# orotidine-5'-phosphate decarboxylase
	r_0794 = 'intracellular * r_0794__Vmax_r_0794 * ( pow ( 1.0 / r_0794__kms_s_0763_br_0794 , 1.0 ) * pow ( 1.0 / r_0794__kms_s_1155r_0794 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_1155 , 1.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_1417 , 1.0 ) / r_0794__Keq_r_0794 ) / ( ( 1.0 + s_0763_b / r_0794__kms_s_0763_br_0794 ) * ( 1.0 + s_1155 / r_0794__kms_s_1155r_0794 ) + ( 1.0 + s_0470 / r_0794__kmp_s_0470r_0794 ) * ( 1.0 + s_1417 / r_0794__kmp_s_1417r_0794 ) - 1.0 ) ) / intracellular '
	# UMP kinase
	r_1059 = 'intracellular * r_1059__Vmax_r_1059 * ( pow ( 1.0 / r_1059__kms_s_0446r_1059 , 1.0 ) * pow ( 1.0 / r_1059__kms_s_1417r_1059 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_1417 , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_1411 , 1.0 ) / r_1059__Keq_r_1059 ) / ( ( 1.0 + s_0446 / r_1059__kms_s_0446r_1059 ) * ( 1.0 + s_1417 / r_1059__kms_s_1417r_1059 ) + ( 1.0 + s_0400 / r_1059__kmp_s_0400r_1059 ) * ( 1.0 + s_1411 / r_1059__kmp_s_1411r_1059 ) - 1.0 ) ) / intracellular '
	# uridylate kinase (dUMP)
	r_1066 = 'intracellular * r_1066__Vmax_r_1066 * ( pow ( 1.0 / r_1066__kms_s_0400r_1066 , 1.0 ) * pow ( 1.0 / r_1066__kms_s_0622r_1066 , 1.0 ) * ( pow ( s_0400 , 1.0 ) * pow ( s_0622 , 1.0 ) - pow ( s_0446 , 1.0 ) * pow ( s_0624 , 1.0 ) / r_1066__Keq_r_1066 ) / ( ( 1.0 + s_0400 / r_1066__kms_s_0400r_1066 ) * ( 1.0 + s_0622 / r_1066__kms_s_0622r_1066 ) + ( 1.0 + s_0446 / r_1066__kmp_s_0446r_1066 ) * ( 1.0 + s_0624 / r_1066__kmp_s_0624r_1066 ) - 1.0 ) ) / intracellular '

	########### dehydro-D-arabinono-1,4-lactone biosynthesis ###########

	# D-arabinose 1-dehydrogenase (NAD)
	r_0351 = 'intracellular * r_0351__Vmax_r_0351 * ( pow ( 1.0 / r_0351__kms_s_0529r_0351 , 1.0 ) * pow ( 1.0 / r_0351__kms_s_0763_br_0351 , 1.0 ) * pow ( 1.0 / r_0351__kms_s_1087r_0351 , 1.0 ) * ( pow ( s_0529 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1087 , 1.0 ) - pow ( s_0530 , 1.0 ) * pow ( s_1082 , 1.0 ) / r_0351__Keq_r_0351 ) / ( ( 1.0 + s_0529 / r_0351__kms_s_0529r_0351 ) * ( 1.0 + s_0763_b / r_0351__kms_s_0763_br_0351 ) * ( 1.0 + s_1087 / r_0351__kms_s_1087r_0351 ) + ( 1.0 + s_0530 / r_0351__kmp_s_0530r_0351 ) * ( 1.0 + s_1082 / r_0351__kmp_s_1082r_0351 ) - 1.0 ) ) / intracellular '
	# D-arabinose 1-dehydrogenase (NADP)
	r_0352 = 'intracellular * r_0352__Vmax_r_0352 * ( pow ( 1.0 / r_0352__kms_s_0530r_0352 , 1.0 ) * pow ( 1.0 / r_0352__kms_s_1091r_0352 , 1.0 ) * ( pow ( s_0530 , 1.0 ) * pow ( s_1091 , 1.0 ) - pow ( s_0529 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) / r_0352__Keq_r_0352 ) / ( ( 1.0 + s_0530 / r_0352__kms_s_0530r_0352 ) * ( 1.0 + s_1091 / r_0352__kms_s_1091r_0352 ) + ( 1.0 + s_0529 / r_0352__kmp_s_0529r_0352 ) * ( 1.0 + s_0763_b / r_0352__kmp_s_0763_br_0352 ) * ( 1.0 + s_1096 / r_0352__kmp_s_1096r_0352 ) - 1.0 ) ) / intracellular '

	########### dolichyl phosphate D-mannose biosynthesis ###########

	# dolichyl-phosphate D-mannosyltransferase
	r_0393 = 'intracellular * r_0393__Vmax_r_0393 * ( pow ( 1.0 / r_0393__kms_s_0616r_0393 , 1.0 ) * pow ( 1.0 / r_0393__kms_s_0710r_0393 , 1.0 ) * ( pow ( s_0616 , 1.0 ) * pow ( s_0710 , 1.0 ) - pow ( s_0615 , 1.0 ) * pow ( s_0706 , 1.0 ) / r_0393__Keq_r_0393 ) / ( ( 1.0 + s_0616 / r_0393__kms_s_0616r_0393 ) * ( 1.0 + s_0710 / r_0393__kms_s_0710r_0393 ) + ( 1.0 + s_0615 / r_0393__kmp_s_0615r_0393 ) * ( 1.0 + s_0706 / r_0393__kmp_s_0706r_0393 ) - 1.0 ) ) / intracellular '
	# mannose-1-phosphate guanylyltransferase
	r_0697 = 'intracellular * r_0697__Vmax_r_0697 * ( pow ( 1.0 / r_0697__kms_s_0553r_0697 , 1.0 ) * pow ( 1.0 / r_0697__kms_s_0755r_0697 , 1.0 ) * pow ( 1.0 / r_0697__kms_s_0763_br_0697 , 1.0 ) * ( pow ( s_0553 , 1.0 ) * pow ( s_0755 , 1.0 ) * pow ( s_0763_b , 1.0 ) - pow ( s_0605 , 1.0 ) * pow ( s_0710 , 1.0 ) / r_0697__Keq_r_0697 ) / ( ( 1.0 + s_0553 / r_0697__kms_s_0553r_0697 ) * ( 1.0 + s_0755 / r_0697__kms_s_0755r_0697 ) * ( 1.0 + s_0763_b / r_0697__kms_s_0763_br_0697 ) + ( 1.0 + s_0605 / r_0697__kmp_s_0605r_0697 ) * ( 1.0 + s_0710 / r_0697__kmp_s_0710r_0697 ) - 1.0 ) ) / intracellular '
	# phosphomannomutase
	r_0875 = 'intracellular * r_0875__Vmax_r_0875 * ( pow ( 1.0 / r_0875__kms_s_0554r_0875 , 1.0 ) * ( pow ( s_0554 , 1.0 ) - pow ( s_0553 , 1.0 ) / r_0875__Keq_r_0875 ) / ( 1.0 + s_0554 / r_0875__kms_s_0554r_0875 + 1.0 + s_0553 / r_0875__kmp_s_0553r_0875 - 1.0 ) ) / intracellular '

	########### ergosterol biosynthesis ###########

	# C-14 sterol reductase
	r_0258 = 'intracellular * r_0258__Vmax_r_0258 * ( pow ( 1.0 / r_0258__kms_s_0268r_0258 , 1.0 ) * pow ( 1.0 / r_0258__kms_s_0763_br_0258 , 1.0 ) * pow ( 1.0 / r_0258__kms_s_1096r_0258 , 1.0 ) * ( pow ( s_0268 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) - pow ( s_0124 , 1.0 ) * pow ( s_1091 , 1.0 ) / r_0258__Keq_r_0258 ) / ( ( 1.0 + s_0268 / r_0258__kms_s_0268r_0258 ) * ( 1.0 + s_0763_b / r_0258__kms_s_0763_br_0258 ) * ( 1.0 + s_1096 / r_0258__kms_s_1096r_0258 ) + ( 1.0 + s_0124 / r_0258__kmp_s_0124r_0258 ) * ( 1.0 + s_1091 / r_0258__kmp_s_1091r_0258 ) - 1.0 ) ) / intracellular '
	# C-3 sterol dehydrogenase
	r_0261 = 'intracellular * r_0261__Vmax_r_0261 * ( pow ( 1.0 / r_0261__kms_s_1091r_0261 , 1.0 ) * pow ( 1.0 / r_0261__kms_s_1457r_0261 , 1.0 ) * ( pow ( s_1091 , 1.0 ) * pow ( s_1457 , 1.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) * pow ( s_1458 , 1.0 ) / r_0261__Keq_r_0261 ) / ( ( 1.0 + s_1091 / r_0261__kms_s_1091r_0261 ) * ( 1.0 + s_1457 / r_0261__kms_s_1457r_0261 ) + ( 1.0 + s_0470 / r_0261__kmp_s_0470r_0261 ) * ( 1.0 + s_0763_b / r_0261__kmp_s_0763_br_0261 ) * ( 1.0 + s_1096 / r_0261__kmp_s_1096r_0261 ) * ( 1.0 + s_1458 / r_0261__kmp_s_1458r_0261 ) - 1.0 ) ) / intracellular '
	# C-3 sterol dehydrogenase (4-methylzymosterol)
	r_0262 = 'intracellular * r_0262__Vmax_r_0262 * ( pow ( 1.0 / r_0262__kms_s_0303r_0262 , 1.0 ) * pow ( 1.0 / r_0262__kms_s_1082r_0262 , 1.0 ) * ( pow ( s_0303 , 1.0 ) * pow ( s_1082 , 1.0 ) - pow ( s_0215 , 1.0 ) * pow ( s_0470 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1087 , 1.0 ) / r_0262__Keq_r_0262 ) / ( ( 1.0 + s_0303 / r_0262__kms_s_0303r_0262 ) * ( 1.0 + s_1082 / r_0262__kms_s_1082r_0262 ) + ( 1.0 + s_0215 / r_0262__kmp_s_0215r_0262 ) * ( 1.0 + s_0470 / r_0262__kmp_s_0470r_0262 ) * ( 1.0 + s_0763_b / r_0262__kmp_s_0763_br_0262 ) * ( 1.0 + s_1087 / r_0262__kmp_s_1087r_0262 ) - 1.0 ) ) / intracellular '
	# C-3 sterol keto reductase (4-methylzymosterol)
	r_0263 = 'intracellular * r_0263__Vmax_r_0263 * ( pow ( 1.0 / r_0263__kms_s_0215r_0263 , 1.0 ) * pow ( 1.0 / r_0263__kms_s_0763_br_0263 , 1.0 ) * pow ( 1.0 / r_0263__kms_s_1096r_0263 , 1.0 ) * ( pow ( s_0215 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) - pow ( s_0302 , 1.0 ) * pow ( s_1091 , 1.0 ) / r_0263__Keq_r_0263 ) / ( ( 1.0 + s_0215 / r_0263__kms_s_0215r_0263 ) * ( 1.0 + s_0763_b / r_0263__kms_s_0763_br_0263 ) * ( 1.0 + s_1096 / r_0263__kms_s_1096r_0263 ) + ( 1.0 + s_0302 / r_0263__kmp_s_0302r_0263 ) * ( 1.0 + s_1091 / r_0263__kmp_s_1091r_0263 ) - 1.0 ) ) / intracellular '
	# C-3 sterol keto reductase (zymosterol)
	r_0264 = 'intracellular * r_0264__Vmax_r_0264 * ( pow ( 1.0 / r_0264__kms_s_0763_br_0264 , 1.0 ) * pow ( 1.0 / r_0264__kms_s_1096r_0264 , 1.0 ) * pow ( 1.0 / r_0264__kms_s_1458r_0264 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) * pow ( s_1458 , 1.0 ) - pow ( s_1091 , 1.0 ) * pow ( s_1447 , 1.0 ) / r_0264__Keq_r_0264 ) / ( ( 1.0 + s_0763_b / r_0264__kms_s_0763_br_0264 ) * ( 1.0 + s_1096 / r_0264__kms_s_1096r_0264 ) * ( 1.0 + s_1458 / r_0264__kms_s_1458r_0264 ) + ( 1.0 + s_1091 / r_0264__kmp_s_1091r_0264 ) * ( 1.0 + s_1447 / r_0264__kmp_s_1447r_0264 ) - 1.0 ) ) / intracellular '
	# C-4 methyl sterol oxidase
	r_0265 = 'intracellular * r_0265__Vmax_r_0265 * ( pow ( 1.0 / r_0265__kms_s_0302r_0265 , 1.0 ) * pow ( 1.0 / r_0265__kms_s_0763_br_0265 , 1.0 ) * pow ( 1.0 / r_0265__kms_s_1096r_0265 , 1.0 ) * pow ( 1.0 / r_0265__kms_s_1160r_0265 , 1.0 ) * ( pow ( s_0302 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) * pow ( s_1160 , 1.0 ) - pow ( s_1091 , 1.0 ) * pow ( s_1434_b , 1.0 ) * pow ( s_1455 , 1.0 ) / r_0265__Keq_r_0265 ) / ( ( 1.0 + s_0302 / r_0265__kms_s_0302r_0265 ) * ( 1.0 + s_0763_b / r_0265__kms_s_0763_br_0265 ) * ( 1.0 + s_1096 / r_0265__kms_s_1096r_0265 ) * ( 1.0 + s_1160 / r_0265__kms_s_1160r_0265 ) + ( 1.0 + s_1091 / r_0265__kmp_s_1091r_0265 ) * ( 1.0 + s_1434_b / r_0265__kmp_s_1434_br_0265 ) * ( 1.0 + s_1455 / r_0265__kmp_s_1455r_0265 ) - 1.0 ) ) / intracellular '
	# C-4 methyl sterol oxidase_2
	r_0266 = 'intracellular * r_0266__Vmax_r_0266 * ( pow ( 1.0 / r_0266__kms_s_0763_br_0266 , 1.0 ) * pow ( 1.0 / r_0266__kms_s_1096r_0266 , 1.0 ) * pow ( 1.0 / r_0266__kms_s_1160r_0266 , 1.0 ) * pow ( 1.0 / r_0266__kms_s_1455r_0266 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) * pow ( s_1160 , 1.0 ) * pow ( s_1455 , 1.0 ) - pow ( s_1091 , 1.0 ) * pow ( s_1434_b , 2.0 ) * pow ( s_1456 , 1.0 ) / r_0266__Keq_r_0266 ) / ( ( 1.0 + s_0763_b / r_0266__kms_s_0763_br_0266 ) * ( 1.0 + s_1096 / r_0266__kms_s_1096r_0266 ) * ( 1.0 + s_1160 / r_0266__kms_s_1160r_0266 ) * ( 1.0 + s_1455 / r_0266__kms_s_1455r_0266 ) + ( 1.0 + s_1091 / r_0266__kmp_s_1091r_0266 ) * ( 1.0 + s_1434_b / r_0266__kmp_s_1434_br_0266 ) * ( 1.0 + s_1456 / r_0266__kmp_s_1456r_0266 ) - 1.0 ) ) / intracellular '
	# C-4 methyl sterol oxidase_3
	r_0267 = 'intracellular * r_0267__Vmax_r_0267 * ( pow ( 1.0 / r_0267__kms_s_0763_br_0267 , 1.0 ) * pow ( 1.0 / r_0267__kms_s_1096r_0267 , 1.0 ) * pow ( 1.0 / r_0267__kms_s_1160r_0267 , 1.0 ) * pow ( 1.0 / r_0267__kms_s_1456r_0267 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) * pow ( s_1160 , 1.0 ) * pow ( s_1456 , 1.0 ) - pow ( s_1091 , 1.0 ) * pow ( s_1434_b , 1.0 ) * pow ( s_1457 , 1.0 ) / r_0267__Keq_r_0267 ) / ( ( 1.0 + s_0763_b / r_0267__kms_s_0763_br_0267 ) * ( 1.0 + s_1096 / r_0267__kms_s_1096r_0267 ) * ( 1.0 + s_1160 / r_0267__kms_s_1160r_0267 ) * ( 1.0 + s_1456 / r_0267__kms_s_1456r_0267 ) + ( 1.0 + s_1091 / r_0267__kmp_s_1091r_0267 ) * ( 1.0 + s_1434_b / r_0267__kmp_s_1434_br_0267 ) * ( 1.0 + s_1457 / r_0267__kmp_s_1457r_0267 ) - 1.0 ) ) / intracellular '
	# C-4 sterol methyl oxidase (4,4-dimethylzymosterol)
	r_0268 = 'intracellular * r_0268__Vmax_r_0268 * ( pow ( 1.0 / r_0268__kms_s_0124r_0268 , 1.0 ) * pow ( 1.0 / r_0268__kms_s_0763_br_0268 , 3.0 ) * pow ( 1.0 / r_0268__kms_s_1096r_0268 , 3.0 ) * pow ( 1.0 / r_0268__kms_s_1160r_0268 , 3.0 ) * ( pow ( s_0124 , 1.0 ) * pow ( s_0763_b , 3.0 ) * pow ( s_1096 , 3.0 ) * pow ( s_1160 , 3.0 ) - pow ( s_0303 , 1.0 ) * pow ( s_1091 , 3.0 ) * pow ( s_1434_b , 4.0 ) / r_0268__Keq_r_0268 ) / ( ( 1.0 + s_0124 / r_0268__kms_s_0124r_0268 ) * ( 1.0 + s_0763_b / r_0268__kms_s_0763_br_0268 ) * ( 1.0 + s_1096 / r_0268__kms_s_1096r_0268 ) * ( 1.0 + s_1160 / r_0268__kms_s_1160r_0268 ) + ( 1.0 + s_0303 / r_0268__kmp_s_0303r_0268 ) * ( 1.0 + s_1091 / r_0268__kmp_s_1091r_0268 ) * ( 1.0 + s_1434_b / r_0268__kmp_s_1434_br_0268 ) - 1.0 ) ) / intracellular '
	# C-8 sterol isomerase
	r_0270 = 'intracellular * r_0270__Vmax_r_0270 * ( pow ( 1.0 / r_0270__kms_s_0669r_0270 , 1.0 ) * ( pow ( s_0669 , 1.0 ) - pow ( s_0627 , 1.0 ) / r_0270__Keq_r_0270 ) / ( 1.0 + s_0669 / r_0270__kms_s_0669r_0270 + 1.0 + s_0627 / r_0270__kmp_s_0627r_0270 - 1.0 ) ) / intracellular '
	# C-s24 sterol reductase
	r_0271 = 'intracellular * r_0271__Vmax_r_0271 * ( pow ( 1.0 / r_0271__kms_s_0632r_0271 , 1.0 ) * pow ( 1.0 / r_0271__kms_s_0763_br_0271 , 1.0 ) * pow ( 1.0 / r_0271__kms_s_1096r_0271 , 1.0 ) * ( pow ( s_0632 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) - pow ( s_0635 , 1.0 ) * pow ( s_1091 , 1.0 ) / r_0271__Keq_r_0271 ) / ( ( 1.0 + s_0632 / r_0271__kms_s_0632r_0271 ) * ( 1.0 + s_0763_b / r_0271__kms_s_0763_br_0271 ) * ( 1.0 + s_1096 / r_0271__kms_s_1096r_0271 ) + ( 1.0 + s_0635 / r_0271__kmp_s_0635r_0271 ) * ( 1.0 + s_1091 / r_0271__kmp_s_1091r_0271 ) - 1.0 ) ) / intracellular '
	# lanosterol synthase
	r_0673 = 'intracellular * r_0673__Vmax_r_0673 * ( pow ( 1.0 / r_0673__kms_s_0040r_0673 , 1.0 ) * ( pow ( s_0040 , 1.0 ) - pow ( s_0963 , 1.0 ) / r_0673__Keq_r_0673 ) / ( 1.0 + s_0040 / r_0673__kms_s_0040r_0673 + 1.0 + s_0963 / r_0673__kmp_s_0963r_0673 - 1.0 ) ) / intracellular '
	# S-adenosyl-methionine delta-24-sterol-c-methyltransferase
	r_0967 = 'intracellular * r_0967__Vmax_r_0967 * ( pow ( 1.0 / r_0967__kms_s_1293r_0967 , 1.0 ) * pow ( 1.0 / r_0967__kms_s_1447r_0967 , 1.0 ) * ( pow ( s_1293 , 1.0 ) * pow ( s_1447 , 1.0 ) - pow ( s_0669 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1290 , 1.0 ) / r_0967__Keq_r_0967 ) / ( ( 1.0 + s_1293 / r_0967__kms_s_1293r_0967 ) * ( 1.0 + s_1447 / r_0967__kms_s_1447r_0967 ) + ( 1.0 + s_0669 / r_0967__kmp_s_0669r_0967 ) * ( 1.0 + s_0763_b / r_0967__kmp_s_0763_br_0967 ) * ( 1.0 + s_1290 / r_0967__kmp_s_1290r_0967 ) - 1.0 ) ) / intracellular '
	# squalene epoxidase (NAD)
	r_0991 = 'intracellular * r_0991__Vmax_r_0991 * ( pow ( 1.0 / r_0991__kms_s_0763_br_0991 , 1.0 ) * pow ( 1.0 / r_0991__kms_s_1087r_0991 , 1.0 ) * pow ( 1.0 / r_0991__kms_s_1160r_0991 , 1.0 ) * pow ( 1.0 / r_0991__kms_s_1327r_0991 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_1087 , 1.0 ) * pow ( s_1160 , 1.0 ) * pow ( s_1327 , 1.0 ) - pow ( s_0040 , 1.0 ) * pow ( s_1082 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0991__Keq_r_0991 ) / ( ( 1.0 + s_0763_b / r_0991__kms_s_0763_br_0991 ) * ( 1.0 + s_1087 / r_0991__kms_s_1087r_0991 ) * ( 1.0 + s_1160 / r_0991__kms_s_1160r_0991 ) * ( 1.0 + s_1327 / r_0991__kms_s_1327r_0991 ) + ( 1.0 + s_0040 / r_0991__kmp_s_0040r_0991 ) * ( 1.0 + s_1082 / r_0991__kmp_s_1082r_0991 ) * ( 1.0 + s_1434_b / r_0991__kmp_s_1434_br_0991 ) - 1.0 ) ) / intracellular '
	# squalene synthase
	r_0993 = 'intracellular * r_0993__Vmax_r_0993 * ( pow ( 1.0 / r_0993__kms_s_0195r_0993 , 2.0 ) * pow ( 1.0 / r_0993__kms_s_0763_br_0993 , 1.0 ) * pow ( 1.0 / r_0993__kms_s_1096r_0993 , 1.0 ) * ( pow ( s_0195 , 2.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) - pow ( s_0605 , 2.0 ) * pow ( s_1091 , 1.0 ) * pow ( s_1327 , 1.0 ) / r_0993__Keq_r_0993 ) / ( ( 1.0 + s_0195 / r_0993__kms_s_0195r_0993 ) * ( 1.0 + s_0763_b / r_0993__kms_s_0763_br_0993 ) * ( 1.0 + s_1096 / r_0993__kms_s_1096r_0993 ) + ( 1.0 + s_0605 / r_0993__kmp_s_0605r_0993 ) * ( 1.0 + s_1091 / r_0993__kmp_s_1091r_0993 ) * ( 1.0 + s_1327 / r_0993__kmp_s_1327r_0993 ) - 1.0 ) ) / intracellular '

	########### ethanol degradation ###########

	# acetyl-CoA synthetase
	r_0127 = 'intracellular * r_0127__Vmax_r_0127 * ( pow ( 1.0 / r_0127__kms_s_0380r_0127 , 1.0 ) * pow ( 1.0 / r_0127__kms_s_0434r_0127 , 1.0 ) * pow ( 1.0 / r_0127__kms_s_0605r_0127 , 1.0 ) * ( pow ( s_0380 , 1.0 ) * pow ( s_0434 , 1.0 ) * pow ( s_0605 , 1.0 ) - pow ( s_0369 , 1.0 ) * pow ( s_0446 , 1.0 ) * pow ( s_0514 , 1.0 ) / r_0127__Keq_r_0127 ) / ( ( 1.0 + s_0380 / r_0127__kms_s_0380r_0127 ) * ( 1.0 + s_0434 / r_0127__kms_s_0434r_0127 ) * ( 1.0 + s_0605 / r_0127__kms_s_0605r_0127 ) + ( 1.0 + s_0369 / r_0127__kmp_s_0369r_0127 ) * ( 1.0 + s_0446 / r_0127__kmp_s_0446r_0127 ) * ( 1.0 + s_0514 / r_0127__kmp_s_0514r_0127 ) - 1.0 ) ) / intracellular '

	########### fatty acid oxidation pathway ###########

	# 3-hydroxyacyl-CoA dehydrogenase (3-oxohexacosyl-CoA)
	r_0057 = 'intracellular * r_0057__Vmax_r_0057 * ( pow ( 1.0 / r_0057__kms_s_0247r_0057 , 1.0 ) * pow ( 1.0 / r_0057__kms_s_0763_br_0057 , 1.0 ) * pow ( 1.0 / r_0057__kms_s_1087r_0057 , 1.0 ) * ( pow ( s_0247 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1087 , 1.0 ) - pow ( s_0046 , 1.0 ) * pow ( s_1082 , 1.0 ) / r_0057__Keq_r_0057 ) / ( ( 1.0 + s_0247 / r_0057__kms_s_0247r_0057 ) * ( 1.0 + s_0763_b / r_0057__kms_s_0763_br_0057 ) * ( 1.0 + s_1087 / r_0057__kms_s_1087r_0057 ) + ( 1.0 + s_0046 / r_0057__kmp_s_0046r_0057 ) * ( 1.0 + s_1082 / r_0057__kmp_s_1082r_0057 ) - 1.0 ) ) / intracellular '
	# 3-hydroxyacyl-CoA dehydrogenase (3-oxohexadecanoyl-CoA)
	r_0058 = 'intracellular * r_0058__Vmax_r_0058 * ( pow ( 1.0 / r_0058__kms_s_0257r_0058 , 1.0 ) * pow ( 1.0 / r_0058__kms_s_0763_br_0058 , 1.0 ) * pow ( 1.0 / r_0058__kms_s_1087r_0058 , 1.0 ) * ( pow ( s_0257 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1087 , 1.0 ) - pow ( s_0052 , 1.0 ) * pow ( s_1082 , 1.0 ) / r_0058__Keq_r_0058 ) / ( ( 1.0 + s_0257 / r_0058__kms_s_0257r_0058 ) * ( 1.0 + s_0763_b / r_0058__kms_s_0763_br_0058 ) * ( 1.0 + s_1087 / r_0058__kms_s_1087r_0058 ) + ( 1.0 + s_0052 / r_0058__kmp_s_0052r_0058 ) * ( 1.0 + s_1082 / r_0058__kmp_s_1082r_0058 ) - 1.0 ) ) / intracellular '
	# 3-hydroxyacyl-CoA dehydrogenase (3-oxooctadecanoyl-CoA)
	r_0059 = 'intracellular * r_0059__Vmax_r_0059 * ( pow ( 1.0 / r_0059__kms_s_0254r_0059 , 1.0 ) * pow ( 1.0 / r_0059__kms_s_0763_br_0059 , 1.0 ) * pow ( 1.0 / r_0059__kms_s_1087r_0059 , 1.0 ) * ( pow ( s_0254 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1087 , 1.0 ) - pow ( s_0234 , 1.0 ) * pow ( s_1082 , 1.0 ) / r_0059__Keq_r_0059 ) / ( ( 1.0 + s_0254 / r_0059__kms_s_0254r_0059 ) * ( 1.0 + s_0763_b / r_0059__kms_s_0763_br_0059 ) * ( 1.0 + s_1087 / r_0059__kms_s_1087r_0059 ) + ( 1.0 + s_0234 / r_0059__kmp_s_0234r_0059 ) * ( 1.0 + s_1082 / r_0059__kmp_s_1082r_0059 ) - 1.0 ) ) / intracellular '
	# 3-hydroxyacyl-CoA dehydrogenase (3-oxotetradecanoyl-CoA)
	r_0060 = 'intracellular * r_0060__Vmax_r_0060 * ( pow ( 1.0 / r_0060__kms_s_0261r_0060 , 1.0 ) * pow ( 1.0 / r_0060__kms_s_0763_br_0060 , 1.0 ) * pow ( 1.0 / r_0060__kms_s_1087r_0060 , 1.0 ) * ( pow ( s_0261 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1087 , 1.0 ) - pow ( s_0055 , 1.0 ) * pow ( s_1082 , 1.0 ) / r_0060__Keq_r_0060 ) / ( ( 1.0 + s_0261 / r_0060__kms_s_0261r_0060 ) * ( 1.0 + s_0763_b / r_0060__kms_s_0763_br_0060 ) * ( 1.0 + s_1087 / r_0060__kms_s_1087r_0060 ) + ( 1.0 + s_0055 / r_0060__kmp_s_0055r_0060 ) * ( 1.0 + s_1082 / r_0060__kmp_s_1082r_0060 ) - 1.0 ) ) / intracellular '
	# fatty-acid--CoA ligase (n-C24:0)
	r_0437 = 'intracellular * r_0437__Vmax_r_0437 * ( pow ( 1.0 / r_0437__kms_s_0446r_0437 , 1.0 ) * pow ( 1.0 / r_0437__kms_s_0514r_0437 , 1.0 ) * pow ( 1.0 / r_0437__kms_s_0987r_0437 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_0987 , 1.0 ) - pow ( s_0434 , 1.0 ) * pow ( s_0605 , 1.0 ) * pow ( s_1355 , 1.0 ) / r_0437__Keq_r_0437 ) / ( ( 1.0 + s_0446 / r_0437__kms_s_0446r_0437 ) * ( 1.0 + s_0514 / r_0437__kms_s_0514r_0437 ) * ( 1.0 + s_0987 / r_0437__kms_s_0987r_0437 ) + ( 1.0 + s_0434 / r_0437__kmp_s_0434r_0437 ) * ( 1.0 + s_0605 / r_0437__kmp_s_0605r_0437 ) * ( 1.0 + s_1355 / r_0437__kmp_s_1355r_0437 ) - 1.0 ) ) / intracellular '
	# fatty-acid--CoA ligase (octadecanoate)
	r_0439 = 'intracellular * r_0439__Vmax_r_0439 * ( pow ( 1.0 / r_0439__kms_s_0434r_0439 , 1.0 ) * pow ( 1.0 / r_0439__kms_s_0605r_0439 , 1.0 ) * pow ( 1.0 / r_0439__kms_s_1334r_0439 , 1.0 ) * ( pow ( s_0434 , 1.0 ) * pow ( s_0605 , 1.0 ) * pow ( s_1334 , 1.0 ) - pow ( s_0446 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_1329 , 1.0 ) / r_0439__Keq_r_0439 ) / ( ( 1.0 + s_0434 / r_0439__kms_s_0434r_0439 ) * ( 1.0 + s_0605 / r_0439__kms_s_0605r_0439 ) * ( 1.0 + s_1334 / r_0439__kms_s_1334r_0439 ) + ( 1.0 + s_0446 / r_0439__kmp_s_0446r_0439 ) * ( 1.0 + s_0514 / r_0439__kmp_s_0514r_0439 ) * ( 1.0 + s_1329 / r_0439__kmp_s_1329r_0439 ) - 1.0 ) ) / intracellular '
	# fatty-acid--CoA ligase (octanoate)
	r_0442 = 'intracellular * r_0442__Vmax_r_0442 * ( pow ( 1.0 / r_0442__kms_s_0434r_0442 , 1.0 ) * pow ( 1.0 / r_0442__kms_s_0605r_0442 , 1.0 ) * pow ( 1.0 / r_0442__kms_s_1140r_0442 , 1.0 ) * ( pow ( s_0434 , 1.0 ) * pow ( s_0605 , 1.0 ) * pow ( s_1140 , 1.0 ) - pow ( s_0446 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_1132 , 1.0 ) / r_0442__Keq_r_0442 ) / ( ( 1.0 + s_0434 / r_0442__kms_s_0434r_0442 ) * ( 1.0 + s_0605 / r_0442__kms_s_0605r_0442 ) * ( 1.0 + s_1140 / r_0442__kms_s_1140r_0442 ) + ( 1.0 + s_0446 / r_0442__kmp_s_0446r_0442 ) * ( 1.0 + s_0514 / r_0442__kmp_s_0514r_0442 ) * ( 1.0 + s_1132 / r_0442__kmp_s_1132r_0442 ) - 1.0 ) ) / intracellular '

	########### folate biosynthesis ###########

	# dihydrofolate reductase
	r_0375 = 'intracellular * r_0375__Vmax_r_0375 * ( pow ( 1.0 / r_0375__kms_s_0601r_0375 , 1.0 ) * pow ( 1.0 / r_0375__kms_s_0763_br_0375 , 1.0 ) * pow ( 1.0 / r_0375__kms_s_1096r_0375 , 1.0 ) * ( pow ( s_0601 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) - pow ( s_0309 , 1.0 ) * pow ( s_1091 , 1.0 ) / r_0375__Keq_r_0375 ) / ( ( 1.0 + s_0601 / r_0375__kms_s_0601r_0375 ) * ( 1.0 + s_0763_b / r_0375__kms_s_0763_br_0375 ) * ( 1.0 + s_1096 / r_0375__kms_s_1096r_0375 ) + ( 1.0 + s_0309 / r_0375__kmp_s_0309r_0375 ) * ( 1.0 + s_1091 / r_0375__kmp_s_1091r_0375 ) - 1.0 ) ) / intracellular '

	########### folate polyglutamylation ###########

	# 5,10-methylenetetrahydrofolatereductase (NADPH)
	r_0093 = 'intracellular * r_0093__Vmax_r_0093 * ( pow ( 1.0 / r_0093__kms_s_0307r_0093 , 1.0 ) * pow ( 1.0 / r_0093__kms_s_0763_br_0093 , 2.0 ) * pow ( 1.0 / r_0093__kms_s_1096r_0093 , 1.0 ) * ( pow ( s_0307 , 1.0 ) * pow ( s_0763_b , 2.0 ) * pow ( s_1096 , 1.0 ) - pow ( s_0328 , 1.0 ) * pow ( s_1091 , 1.0 ) / r_0093__Keq_r_0093 ) / ( ( 1.0 + s_0307 / r_0093__kms_s_0307r_0093 ) * ( 1.0 + s_0763_b / r_0093__kms_s_0763_br_0093 ) * ( 1.0 + s_1096 / r_0093__kms_s_1096r_0093 ) + ( 1.0 + s_0328 / r_0093__kmp_s_0328r_0093 ) * ( 1.0 + s_1091 / r_0093__kmp_s_1091r_0093 ) - 1.0 ) ) / intracellular '
	# formate-tetrahydrofolate ligase
	r_0479 = 'intracellular * r_0479__Vmax_r_0479 * ( pow ( 1.0 / r_0479__kms_s_0309r_0479 , 1.0 ) * pow ( 1.0 / r_0479__kms_s_0446r_0479 , 1.0 ) * pow ( 1.0 / r_0479__kms_s_0689r_0479 , 1.0 ) * ( pow ( s_0309 , 1.0 ) * pow ( s_0446 , 1.0 ) * pow ( s_0689 , 1.0 ) - pow ( s_0122 , 1.0 ) * pow ( s_0400 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0479__Keq_r_0479 ) / ( ( 1.0 + s_0309 / r_0479__kms_s_0309r_0479 ) * ( 1.0 + s_0446 / r_0479__kms_s_0446r_0479 ) * ( 1.0 + s_0689 / r_0479__kms_s_0689r_0479 ) + ( 1.0 + s_0122 / r_0479__kmp_s_0122r_0479 ) * ( 1.0 + s_0400 / r_0479__kmp_s_0400r_0479 ) * ( 1.0 + s_1207 / r_0479__kmp_s_1207r_0479 ) - 1.0 ) ) / intracellular '
	# methenyltetrahydrifikate cyclohydrolase
	r_0699 = 'intracellular * r_0699__Vmax_r_0699 * ( pow ( 1.0 / r_0699__kms_s_0015r_0699 , 1.0 ) * pow ( 1.0 / r_0699__kms_s_1434_br_0699 , 1.0 ) * ( pow ( s_0015 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0122 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0699__Keq_r_0699 ) / ( ( 1.0 + s_0015 / r_0699__kms_s_0015r_0699 ) * ( 1.0 + s_1434_b / r_0699__kms_s_1434_br_0699 ) + ( 1.0 + s_0122 / r_0699__kmp_s_0122r_0699 ) * ( 1.0 + s_0763_b / r_0699__kmp_s_0763_br_0699 ) - 1.0 ) ) / intracellular '
	# methylenetetrahydrofolate dehydrogenase (NADP)
	r_0707 = 'intracellular * r_0707__Vmax_r_0707 * ( pow ( 1.0 / r_0707__kms_s_0307r_0707 , 1.0 ) * pow ( 1.0 / r_0707__kms_s_1091r_0707 , 1.0 ) * ( pow ( s_0307 , 1.0 ) * pow ( s_1091 , 1.0 ) - pow ( s_0015 , 1.0 ) * pow ( s_1096 , 1.0 ) / r_0707__Keq_r_0707 ) / ( ( 1.0 + s_0307 / r_0707__kms_s_0307r_0707 ) * ( 1.0 + s_1091 / r_0707__kms_s_1091r_0707 ) + ( 1.0 + s_0015 / r_0707__kmp_s_0015r_0707 ) * ( 1.0 + s_1096 / r_0707__kmp_s_1096r_0707 ) - 1.0 ) ) / intracellular '

	########### galactose degradation ###########

	# phosphoglucomutase
	r_0861 = 'intracellular * r_0861__Vmax_r_0861 * ( pow ( 1.0 / r_0861__kms_s_0410r_0861 , 1.0 ) * ( pow ( s_0410 , 1.0 ) - pow ( s_0549 , 1.0 ) / r_0861__Keq_r_0861 ) / ( 1.0 + s_0410 / r_0861__kms_s_0410r_0861 + 1.0 + s_0549 / r_0861__kmp_s_0549r_0861 - 1.0 ) ) / intracellular '

	########### glucose fermentation ###########

	# aldehyde dehydrogenase (acetaldehyde, NADP)
	r_0191 = 'intracellular * r_0191__Vmax_r_0191 * ( pow ( 1.0 / r_0191__kms_s_0366r_0191 , 1.0 ) * pow ( 1.0 / r_0191__kms_s_1091r_0191 , 1.0 ) * pow ( 1.0 / r_0191__kms_s_1434_br_0191 , 1.0 ) * ( pow ( s_0366 , 1.0 ) * pow ( s_1091 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0369 , 1.0 ) * pow ( s_0763_b , 2.0 ) * pow ( s_1096 , 1.0 ) / r_0191__Keq_r_0191 ) / ( ( 1.0 + s_0366 / r_0191__kms_s_0366r_0191 ) * ( 1.0 + s_1091 / r_0191__kms_s_1091r_0191 ) * ( 1.0 + s_1434_b / r_0191__kms_s_1434_br_0191 ) + ( 1.0 + s_0369 / r_0191__kmp_s_0369r_0191 ) * ( 1.0 + s_0763_b / r_0191__kmp_s_0763_br_0191 ) * ( 1.0 + s_1096 / r_0191__kmp_s_1096r_0191 ) - 1.0 ) ) / intracellular '

	########### glucose-6-phosphate biosynthesis ###########

	# glucokinase
	r_0499 = 'intracellular * r_0499__Vmax_r_0499 * ( pow ( 1.0 / r_0499__kms_s_0446r_0499 , 1.0 ) * pow ( 1.0 / r_0499__kms_s_0545r_0499 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_0545 , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_0455 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0499__Keq_r_0499 ) / ( ( 1.0 + s_0446 / r_0499__kms_s_0446r_0499 ) * ( 1.0 + s_0545 / r_0499__kms_s_0545r_0499 ) + ( 1.0 + s_0400 / r_0499__kmp_s_0400r_0499 ) * ( 1.0 + s_0455 / r_0499__kmp_s_0455r_0499 ) * ( 1.0 + s_0763_b / r_0499__kmp_s_0763_br_0499 ) - 1.0 ) ) / intracellular '
	# hexokinase (D-glucose:ATP)
	r_0573 = 'intracellular * r_0573__Vmax_r_0573 * ( pow ( 1.0 / r_0573__kms_s_0446r_0573 , 1.0 ) * pow ( 1.0 / r_0573__kms_s_0545r_0573 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_0545 , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_0410 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0573__Keq_r_0573 ) / ( ( 1.0 + s_0446 / r_0573__kms_s_0446r_0573 ) * ( 1.0 + s_0545 / r_0573__kms_s_0545r_0573 ) + ( 1.0 + s_0400 / r_0573__kmp_s_0400r_0573 ) * ( 1.0 + s_0410 / r_0573__kmp_s_0410r_0573 ) * ( 1.0 + s_0763_b / r_0573__kmp_s_0763_br_0573 ) - 1.0 ) ) / intracellular '

	########### glutathione-glutaredoxin system ###########

	# thioredoxin reductase (NADPH)
	r_1024 = 'intracellular * r_1024__Vmax_r_1024 * ( pow ( 1.0 / r_1024__kms_s_0763_br_1024 , 1.0 ) * pow ( 1.0 / r_1024__kms_s_1096r_1024 , 1.0 ) * pow ( 1.0 / r_1024__kms_s_1517r_1024 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) * pow ( s_1517 , 1.0 ) - pow ( s_1091 , 1.0 ) * pow ( s_1521 , 1.0 ) / r_1024__Keq_r_1024 ) / ( ( 1.0 + s_0763_b / r_1024__kms_s_0763_br_1024 ) * ( 1.0 + s_1096 / r_1024__kms_s_1096r_1024 ) * ( 1.0 + s_1517 / r_1024__kms_s_1517r_1024 ) + ( 1.0 + s_1091 / r_1024__kmp_s_1091r_1024 ) * ( 1.0 + s_1521 / r_1024__kmp_s_1521r_1024 ) - 1.0 ) ) / intracellular '

	########### glycerol biosynthesis ###########

	# glycerol-3-phosphatase
	r_0528 = 'intracellular * r_0528__Vmax_r_0528 * ( pow ( 1.0 / r_0528__kms_s_1315r_0528 , 1.0 ) * pow ( 1.0 / r_0528__kms_s_1434_br_0528 , 1.0 ) * ( pow ( s_1315 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0732 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0528__Keq_r_0528 ) / ( ( 1.0 + s_1315 / r_0528__kms_s_1315r_0528 ) * ( 1.0 + s_1434_b / r_0528__kms_s_1434_br_0528 ) + ( 1.0 + s_0732 / r_0528__kmp_s_0732r_0528 ) * ( 1.0 + s_1207 / r_0528__kmp_s_1207r_0528 ) - 1.0 ) ) / intracellular '

	########### glycerol degradation ###########

	# glycerol-3-phosphate dehydrogenase (fad)
	r_0529 = 'intracellular * r_0529__Vmax_r_0529 * ( pow ( 1.0 / r_0529__kms_s_0657r_0529 , 1.0 ) * pow ( 1.0 / r_0529__kms_s_1315r_0529 , 1.0 ) * ( pow ( s_0657 , 1.0 ) * pow ( s_1315 , 1.0 ) - pow ( s_0659 , 1.0 ) * pow ( s_0735 , 1.0 ) / r_0529__Keq_r_0529 ) / ( ( 1.0 + s_0657 / r_0529__kms_s_0657r_0529 ) * ( 1.0 + s_1315 / r_0529__kms_s_1315r_0529 ) + ( 1.0 + s_0659 / r_0529__kmp_s_0659r_0529 ) * ( 1.0 + s_0735 / r_0529__kmp_s_0735r_0529 ) - 1.0 ) ) / intracellular '

	########### glycine cleavage complex ###########

	# glycine cleavage system
	r_0538 = 'intracellular * r_0538__Vmax_r_0538 * ( pow ( 1.0 / r_0538__kms_s_0309r_0538 , 1.0 ) * pow ( 1.0 / r_0538__kms_s_0740r_0538 , 1.0 ) * pow ( 1.0 / r_0538__kms_s_1082r_0538 , 1.0 ) * ( pow ( s_0309 , 1.0 ) * pow ( s_0740 , 1.0 ) * pow ( s_1082 , 1.0 ) - pow ( s_0307 , 1.0 ) * pow ( s_0430 , 1.0 ) * pow ( s_0470 , 1.0 ) * pow ( s_1087 , 1.0 ) / r_0538__Keq_r_0538 ) / ( ( 1.0 + s_0309 / r_0538__kms_s_0309r_0538 ) * ( 1.0 + s_0740 / r_0538__kms_s_0740r_0538 ) * ( 1.0 + s_1082 / r_0538__kms_s_1082r_0538 ) + ( 1.0 + s_0307 / r_0538__kmp_s_0307r_0538 ) * ( 1.0 + s_0430 / r_0538__kmp_s_0430r_0538 ) * ( 1.0 + s_0470 / r_0538__kmp_s_0470r_0538 ) * ( 1.0 + s_1087 / r_0538__kmp_s_1087r_0538 ) - 1.0 ) ) / intracellular '

	########### glycogen biosynthesis ###########

	# 1,4-alpha-glucan branching enzyme
	r_0006 = 'intracellular * r_0006__Vmax_r_0006 * ( pow ( 1.0 / r_0006__kms_s_0438r_0006 , 1.0 ) * ( pow ( s_0438 , 1.0 ) - pow ( s_0743 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0006__Keq_r_0006 ) / ( 1.0 + s_0438 / r_0006__kms_s_0438r_0006 + ( 1.0 + s_0743 / r_0006__kmp_s_0743r_0006 ) * ( 1.0 + s_1434_b / r_0006__kmp_s_1434_br_0006 ) - 1.0 ) ) / intracellular '
	# glycogen (starch) synthase
	r_0547 = 'intracellular * r_0547__Vmax_r_0547 * ( pow ( 1.0 / r_0547__kms_s_1415r_0547 , 1.0 ) * pow ( 1.0 / r_0547__kms_s_1434_br_0547 , 1.0 ) * ( pow ( s_1415 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0438 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1411 , 1.0 ) / r_0547__Keq_r_0547 ) / ( ( 1.0 + s_1415 / r_0547__kms_s_1415r_0547 ) * ( 1.0 + s_1434_b / r_0547__kms_s_1434_br_0547 ) + ( 1.0 + s_0438 / r_0547__kmp_s_0438r_0547 ) * ( 1.0 + s_0763_b / r_0547__kmp_s_0763_br_0547 ) * ( 1.0 + s_1411 / r_0547__kmp_s_1411r_0547 ) - 1.0 ) ) / intracellular '
	# UTP-glucose-1-phosphate uridylyltransferase
	r_1072 = 'intracellular * r_1072__Vmax_r_1072 * ( pow ( 1.0 / r_1072__kms_s_0549r_1072 , 1.0 ) * pow ( 1.0 / r_1072__kms_s_0763_br_1072 , 1.0 ) * pow ( 1.0 / r_1072__kms_s_1430r_1072 , 1.0 ) * ( pow ( s_0549 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1430 , 1.0 ) - pow ( s_0605 , 1.0 ) * pow ( s_1415 , 1.0 ) / r_1072__Keq_r_1072 ) / ( ( 1.0 + s_0549 / r_1072__kms_s_0549r_1072 ) * ( 1.0 + s_0763_b / r_1072__kms_s_0763_br_1072 ) * ( 1.0 + s_1430 / r_1072__kms_s_1430r_1072 ) + ( 1.0 + s_0605 / r_1072__kmp_s_0605r_1072 ) * ( 1.0 + s_1415 / r_1072__kmp_s_1415r_1072 ) - 1.0 ) ) / intracellular '

	########### glycolysis ###########

	# enolase
	r_0398 = 'intracellular * r_0398__Vmax_r_0398 * ( pow ( 1.0 / r_0398__kms_s_0193r_0398 , 1.0 ) * ( pow ( s_0193 , 1.0 ) - pow ( s_1243 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0398__Keq_r_0398 ) / ( 1.0 + s_0193 / r_0398__kms_s_0193r_0398 + ( 1.0 + s_1243 / r_0398__kmp_s_1243r_0398 ) * ( 1.0 + s_1434_b / r_0398__kmp_s_1434_br_0398 ) - 1.0 ) ) / intracellular '
	# fructose-bisphosphate aldolase
	r_0484 = 'intracellular * r_0484__Vmax_r_0484 * ( pow ( 1.0 / r_0484__kms_s_0537r_0484 , 1.0 ) * ( pow ( s_0537 , 1.0 ) - pow ( s_0731 , 1.0 ) * pow ( s_0735 , 1.0 ) / r_0484__Keq_r_0484 ) / ( 1.0 + s_0537 / r_0484__kms_s_0537r_0484 + ( 1.0 + s_0731 / r_0484__kmp_s_0731r_0484 ) * ( 1.0 + s_0735 / r_0484__kmp_s_0735r_0484 ) - 1.0 ) ) / intracellular '
	# glucose-6-phosphate isomerase
	r_0504 = 'intracellular * r_0504__Vmax_r_0504 * ( pow ( 1.0 / r_0504__kms_s_0455r_0504 , 1.0 ) * ( pow ( s_0455 , 1.0 ) - pow ( s_0539 , 1.0 ) / r_0504__Keq_r_0504 ) / ( 1.0 + s_0455 / r_0504__kms_s_0455r_0504 + 1.0 + s_0539 / r_0504__kmp_s_0539r_0504 - 1.0 ) ) / intracellular '
	# glucose-6-phosphate isomerase_2
	r_0505 = 'intracellular * r_0505__Vmax_r_0505 * ( pow ( 1.0 / r_0505__kms_s_0410r_0505 , 1.0 ) * ( pow ( s_0410 , 1.0 ) - pow ( s_0539 , 1.0 ) / r_0505__Keq_r_0505 ) / ( 1.0 + s_0410 / r_0505__kms_s_0410r_0505 + 1.0 + s_0539 / r_0505__kmp_s_0539r_0505 - 1.0 ) ) / intracellular '
	# glyceraldehyde-3-phosphate dehydrogenase
	r_0525 = 'intracellular * r_0525__Vmax_r_0525 * ( pow ( 1.0 / r_0525__kms_s_0731r_0525 , 1.0 ) * pow ( 1.0 / r_0525__kms_s_1082r_0525 , 1.0 ) * pow ( 1.0 / r_0525__kms_s_1207r_0525 , 1.0 ) * ( pow ( s_0731 , 1.0 ) * pow ( s_1082 , 1.0 ) * pow ( s_1207 , 1.0 ) - pow ( s_0265 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1087 , 1.0 ) / r_0525__Keq_r_0525 ) / ( ( 1.0 + s_0731 / r_0525__kms_s_0731r_0525 ) * ( 1.0 + s_1082 / r_0525__kms_s_1082r_0525 ) * ( 1.0 + s_1207 / r_0525__kms_s_1207r_0525 ) + ( 1.0 + s_0265 / r_0525__kmp_s_0265r_0525 ) * ( 1.0 + s_0763_b / r_0525__kmp_s_0763_br_0525 ) * ( 1.0 + s_1087 / r_0525__kmp_s_1087r_0525 ) - 1.0 ) ) / intracellular '
	# phosphofructokinase
	r_0859 = 'intracellular * r_0859__Vmax_r_0859 * ( pow ( 1.0 / r_0859__kms_s_0446r_0859 , 1.0 ) * pow ( 1.0 / r_0859__kms_s_0539r_0859 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_0539 , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_0537 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0859__Keq_r_0859 ) / ( ( 1.0 + s_0446 / r_0859__kms_s_0446r_0859 ) * ( 1.0 + s_0539 / r_0859__kms_s_0539r_0859 ) + ( 1.0 + s_0400 / r_0859__kmp_s_0400r_0859 ) * ( 1.0 + s_0537 / r_0859__kmp_s_0537r_0859 ) * ( 1.0 + s_0763_b / r_0859__kmp_s_0763_br_0859 ) - 1.0 ) ) / intracellular '
	# phosphoglycerate kinase
	r_0865 = 'intracellular * r_0865__Vmax_r_0865 * ( pow ( 1.0 / r_0865__kms_s_0265r_0865 , 1.0 ) * pow ( 1.0 / r_0865__kms_s_0400r_0865 , 1.0 ) * ( pow ( s_0265 , 1.0 ) * pow ( s_0400 , 1.0 ) - pow ( s_0264 , 1.0 ) * pow ( s_0446 , 1.0 ) / r_0865__Keq_r_0865 ) / ( ( 1.0 + s_0265 / r_0865__kms_s_0265r_0865 ) * ( 1.0 + s_0400 / r_0865__kms_s_0400r_0865 ) + ( 1.0 + s_0264 / r_0865__kmp_s_0264r_0865 ) * ( 1.0 + s_0446 / r_0865__kmp_s_0446r_0865 ) - 1.0 ) ) / intracellular '
	# phosphoglycerate mutase
	r_0866 = 'intracellular * r_0866__Vmax_r_0866 * ( pow ( 1.0 / r_0866__kms_s_0264r_0866 , 1.0 ) * ( pow ( s_0264 , 1.0 ) - pow ( s_0193 , 1.0 ) / r_0866__Keq_r_0866 ) / ( 1.0 + s_0264 / r_0866__kms_s_0264r_0866 + 1.0 + s_0193 / r_0866__kmp_s_0193r_0866 - 1.0 ) ) / intracellular '
	# pyruvate kinase
	r_0941 = 'intracellular * r_0941__Vmax_r_0941 * ( pow ( 1.0 / r_0941__kms_s_0400r_0941 , 1.0 ) * pow ( 1.0 / r_0941__kms_s_0763_br_0941 , 1.0 ) * pow ( 1.0 / r_0941__kms_s_1243r_0941 , 1.0 ) * ( pow ( s_0400 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1243 , 1.0 ) - pow ( s_0446 , 1.0 ) * pow ( s_1277 , 1.0 ) / r_0941__Keq_r_0941 ) / ( ( 1.0 + s_0400 / r_0941__kms_s_0400r_0941 ) * ( 1.0 + s_0763_b / r_0941__kms_s_0763_br_0941 ) * ( 1.0 + s_1243 / r_0941__kms_s_1243r_0941 ) + ( 1.0 + s_0446 / r_0941__kmp_s_0446r_0941 ) * ( 1.0 + s_1277 / r_0941__kmp_s_1277r_0941 ) - 1.0 ) ) / intracellular '
	# triose-phosphate isomerase
	r_1041 = 'intracellular * r_1041__Vmax_r_1041 * ( pow ( 1.0 / r_1041__kms_s_0735r_1041 , 1.0 ) * ( pow ( s_0735 , 1.0 ) - pow ( s_0731 , 1.0 ) / r_1041__Keq_r_1041 ) / ( 1.0 + s_0735 / r_1041__kms_s_0735r_1041 + 1.0 + s_0731 / r_1041__kmp_s_0731r_1041 - 1.0 ) ) / intracellular '

	########### glyoxylate cycle ###########

	# malate dehydrogenase
	r_0688 = 'intracellular * r_0688__Vmax_r_0688 * ( pow ( 1.0 / r_0688__kms_s_0763_br_0688 , 1.0 ) * pow ( 1.0 / r_0688__kms_s_1087r_0688 , 1.0 ) * pow ( 1.0 / r_0688__kms_s_1156r_0688 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_1087 , 1.0 ) * pow ( s_1156 , 1.0 ) - pow ( s_0069 , 1.0 ) * pow ( s_1082 , 1.0 ) / r_0688__Keq_r_0688 ) / ( ( 1.0 + s_0763_b / r_0688__kms_s_0763_br_0688 ) * ( 1.0 + s_1087 / r_0688__kms_s_1087r_0688 ) * ( 1.0 + s_1156 / r_0688__kms_s_1156r_0688 ) + ( 1.0 + s_0069 / r_0688__kmp_s_0069r_0688 ) * ( 1.0 + s_1082 / r_0688__kmp_s_1082r_0688 ) - 1.0 ) ) / intracellular '

	########### isoleucine biosynthesis ###########

	# L-threonine deaminase
	r_0667 = 'intracellular * r_0667__Vmax_r_0667 * ( pow ( 1.0 / r_0667__kms_s_0949r_0667 , 1.0 ) * ( pow ( s_0949 , 1.0 ) - pow ( s_0183 , 1.0 ) * pow ( s_0430 , 1.0 ) / r_0667__Keq_r_0667 ) / ( 1.0 + s_0949 / r_0667__kms_s_0949r_0667 + ( 1.0 + s_0183 / r_0667__kmp_s_0183r_0667 ) * ( 1.0 + s_0430 / r_0667__kmp_s_0430r_0667 ) - 1.0 ) ) / intracellular '

	########### leucine biosynthesis ###########

	# 2-isopropylmalate hydratase
	r_0025 = 'intracellular * r_0025__Vmax_r_0025 * ( pow ( 1.0 / r_0025__kms_s_0167r_0025 , 1.0 ) * ( pow ( s_0167 , 1.0 ) - pow ( s_0170 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0025__Keq_r_0025 ) / ( 1.0 + s_0167 / r_0025__kms_s_0167r_0025 + ( 1.0 + s_0170 / r_0025__kmp_s_0170r_0025 ) * ( 1.0 + s_1434_b / r_0025__kmp_s_1434_br_0025 ) - 1.0 ) ) / intracellular '
	# 2-isopropylmalate synthase
	r_0026 = 'intracellular * r_0026__Vmax_r_0026 * ( pow ( 1.0 / r_0026__kms_s_0238r_0026 , 1.0 ) * pow ( 1.0 / r_0026__kms_s_0380r_0026 , 1.0 ) * pow ( 1.0 / r_0026__kms_s_1434_br_0026 , 1.0 ) * ( pow ( s_0238 , 1.0 ) * pow ( s_0380 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0167 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0026__Keq_r_0026 ) / ( ( 1.0 + s_0238 / r_0026__kms_s_0238r_0026 ) * ( 1.0 + s_0380 / r_0026__kms_s_0380r_0026 ) * ( 1.0 + s_1434_b / r_0026__kms_s_1434_br_0026 ) + ( 1.0 + s_0167 / r_0026__kmp_s_0167r_0026 ) * ( 1.0 + s_0514 / r_0026__kmp_s_0514r_0026 ) * ( 1.0 + s_0763_b / r_0026__kmp_s_0763_br_0026 ) - 1.0 ) ) / intracellular '
	# 3-isopropylmalate dehydratase
	r_0063 = 'intracellular * r_0063__Vmax_r_0063 * ( pow ( 1.0 / r_0063__kms_s_0170r_0063 , 1.0 ) * pow ( 1.0 / r_0063__kms_s_1434_br_0063 , 1.0 ) * ( pow ( s_0170 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0008 , 1.0 ) / r_0063__Keq_r_0063 ) / ( ( 1.0 + s_0170 / r_0063__kms_s_0170r_0063 ) * ( 1.0 + s_1434_b / r_0063__kms_s_1434_br_0063 ) + 1.0 + s_0008 / r_0063__kmp_s_0008r_0063 - 1.0 ) ) / intracellular '
	# 3-isopropylmalate dehydrogenase
	r_0064 = 'intracellular * r_0064__Vmax_r_0064 * ( pow ( 1.0 / r_0064__kms_s_0008r_0064 , 1.0 ) * pow ( 1.0 / r_0064__kms_s_1082r_0064 , 1.0 ) * ( pow ( s_0008 , 1.0 ) * pow ( s_1082 , 1.0 ) - pow ( s_0010 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1087 , 1.0 ) / r_0064__Keq_r_0064 ) / ( ( 1.0 + s_0008 / r_0064__kms_s_0008r_0064 ) * ( 1.0 + s_1082 / r_0064__kms_s_1082r_0064 ) + ( 1.0 + s_0010 / r_0064__kmp_s_0010r_0064 ) * ( 1.0 + s_0763_b / r_0064__kmp_s_0763_br_0064 ) * ( 1.0 + s_1087 / r_0064__kmp_s_1087r_0064 ) - 1.0 ) ) / intracellular '

	########### lysine biosynthesis ###########

	# 2-methylcitrate dehydratase
	r_0029 = 'intracellular * r_0029__Vmax_r_0029 * ( pow ( 1.0 / r_0029__kms_s_0798r_0029 , 1.0 ) * ( pow ( s_0798 , 1.0 ) - pow ( s_0468 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0029__Keq_r_0029 ) / ( 1.0 + s_0798 / r_0029__kms_s_0798r_0029 + ( 1.0 + s_0468 / r_0029__kmp_s_0468r_0029 ) * ( 1.0 + s_1434_b / r_0029__kmp_s_1434_br_0029 ) - 1.0 ) ) / intracellular '
	# homoacontinate hydratase
	r_0581 = 'intracellular * r_0581__Vmax_r_0581 * ( pow ( 1.0 / r_0581__kms_s_0468r_0581 , 1.0 ) * pow ( 1.0 / r_0581__kms_s_1434_br_0581 , 1.0 ) * ( pow ( s_0468 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0800 , 1.0 ) / r_0581__Keq_r_0581 ) / ( ( 1.0 + s_0468 / r_0581__kms_s_0468r_0581 ) * ( 1.0 + s_1434_b / r_0581__kms_s_1434_br_0581 ) + 1.0 + s_0800 / r_0581__kmp_s_0800r_0581 - 1.0 ) ) / intracellular '
	# homocitrate synthase
	r_0582 = 'intracellular * r_0582__Vmax_r_0582 * ( pow ( 1.0 / r_0582__kms_s_0185r_0582 , 1.0 ) * pow ( 1.0 / r_0582__kms_s_0380r_0582 , 1.0 ) * pow ( 1.0 / r_0582__kms_s_1434_br_0582 , 1.0 ) * ( pow ( s_0185 , 1.0 ) * pow ( s_0380 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0514 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_0798 , 1.0 ) / r_0582__Keq_r_0582 ) / ( ( 1.0 + s_0185 / r_0582__kms_s_0185r_0582 ) * ( 1.0 + s_0380 / r_0582__kms_s_0380r_0582 ) * ( 1.0 + s_1434_b / r_0582__kms_s_1434_br_0582 ) + ( 1.0 + s_0514 / r_0582__kmp_s_0514r_0582 ) * ( 1.0 + s_0763_b / r_0582__kmp_s_0763_br_0582 ) * ( 1.0 + s_0798 / r_0582__kmp_s_0798r_0582 ) - 1.0 ) ) / intracellular '
	# homoisocitrate dehydrogenase
	r_0585 = 'intracellular * r_0585__Vmax_r_0585 * ( pow ( 1.0 / r_0585__kms_s_0800r_0585 , 1.0 ) * pow ( 1.0 / r_0585__kms_s_1082r_0585 , 1.0 ) * ( pow ( s_0800 , 1.0 ) * pow ( s_1082 , 1.0 ) - pow ( s_0180 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1087 , 1.0 ) / r_0585__Keq_r_0585 ) / ( ( 1.0 + s_0800 / r_0585__kms_s_0800r_0585 ) * ( 1.0 + s_1082 / r_0585__kms_s_1082r_0585 ) + ( 1.0 + s_0180 / r_0585__kmp_s_0180r_0585 ) * ( 1.0 + s_0763_b / r_0585__kmp_s_0763_br_0585 ) * ( 1.0 + s_1087 / r_0585__kmp_s_1087r_0585 ) - 1.0 ) ) / intracellular '
	# L-aminoadipate-semialdehyde dehydrogenase (NADH)
	r_0650 = 'intracellular * r_0650__Vmax_r_0650 * ( pow ( 1.0 / r_0650__kms_s_0446r_0650 , 1.0 ) * pow ( 1.0 / r_0650__kms_s_0763_br_0650 , 1.0 ) * pow ( 1.0 / r_0650__kms_s_0861r_0650 , 1.0 ) * pow ( 1.0 / r_0650__kms_s_1087r_0650 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_0861 , 1.0 ) * pow ( s_1087 , 1.0 ) - pow ( s_0434 , 1.0 ) * pow ( s_0605 , 1.0 ) * pow ( s_0867 , 1.0 ) * pow ( s_1082 , 1.0 ) / r_0650__Keq_r_0650 ) / ( ( 1.0 + s_0446 / r_0650__kms_s_0446r_0650 ) * ( 1.0 + s_0763_b / r_0650__kms_s_0763_br_0650 ) * ( 1.0 + s_0861 / r_0650__kms_s_0861r_0650 ) * ( 1.0 + s_1087 / r_0650__kms_s_1087r_0650 ) + ( 1.0 + s_0434 / r_0650__kmp_s_0434r_0650 ) * ( 1.0 + s_0605 / r_0650__kmp_s_0605r_0650 ) * ( 1.0 + s_0867 / r_0650__kmp_s_0867r_0650 ) * ( 1.0 + s_1082 / r_0650__kmp_s_1082r_0650 ) - 1.0 ) ) / intracellular '
	# saccharopine dehydrogenase (NAD, L-lysine forming)
	r_0969 = 'intracellular * r_0969__Vmax_r_0969 * ( pow ( 1.0 / r_0969__kms_s_0942r_0969 , 1.0 ) * pow ( 1.0 / r_0969__kms_s_1082r_0969 , 1.0 ) * pow ( 1.0 / r_0969__kms_s_1434_br_0969 , 1.0 ) * ( pow ( s_0942 , 1.0 ) * pow ( s_1082 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0185 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_0929 , 1.0 ) * pow ( s_1087 , 1.0 ) / r_0969__Keq_r_0969 ) / ( ( 1.0 + s_0942 / r_0969__kms_s_0942r_0969 ) * ( 1.0 + s_1082 / r_0969__kms_s_1082r_0969 ) * ( 1.0 + s_1434_b / r_0969__kms_s_1434_br_0969 ) + ( 1.0 + s_0185 / r_0969__kmp_s_0185r_0969 ) * ( 1.0 + s_0763_b / r_0969__kmp_s_0763_br_0969 ) * ( 1.0 + s_0929 / r_0969__kmp_s_0929r_0969 ) * ( 1.0 + s_1087 / r_0969__kmp_s_1087r_0969 ) - 1.0 ) ) / intracellular '
	# saccharopine dehydrogenase (NADP, L-glutamate forming)
	r_0970 = 'intracellular * r_0970__Vmax_r_0970 * ( pow ( 1.0 / r_0970__kms_s_0763_br_0970 , 1.0 ) * pow ( 1.0 / r_0970__kms_s_0867r_0970 , 1.0 ) * pow ( 1.0 / r_0970__kms_s_0899r_0970 , 1.0 ) * pow ( 1.0 / r_0970__kms_s_1096r_0970 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_0867 , 1.0 ) * pow ( s_0899 , 1.0 ) * pow ( s_1096 , 1.0 ) - pow ( s_0942 , 1.0 ) * pow ( s_1091 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0970__Keq_r_0970 ) / ( ( 1.0 + s_0763_b / r_0970__kms_s_0763_br_0970 ) * ( 1.0 + s_0867 / r_0970__kms_s_0867r_0970 ) * ( 1.0 + s_0899 / r_0970__kms_s_0899r_0970 ) * ( 1.0 + s_1096 / r_0970__kms_s_1096r_0970 ) + ( 1.0 + s_0942 / r_0970__kmp_s_0942r_0970 ) * ( 1.0 + s_1091 / r_0970__kmp_s_1091r_0970 ) * ( 1.0 + s_1434_b / r_0970__kmp_s_1434_br_0970 ) - 1.0 ) ) / intracellular '

	########### mannose degradation ###########

	# mannose-6-phosphate isomerase
	r_0698 = 'intracellular * r_0698__Vmax_r_0698 * ( pow ( 1.0 / r_0698__kms_s_0539r_0698 , 1.0 ) * ( pow ( s_0539 , 1.0 ) - pow ( s_0554 , 1.0 ) / r_0698__Keq_r_0698 ) / ( 1.0 + s_0539 / r_0698__kms_s_0539r_0698 + 1.0 + s_0554 / r_0698__kmp_s_0554r_0698 - 1.0 ) ) / intracellular '

	########### methionine salvage pathway ###########

	# 2-aminoadipate transaminase
	r_0018 = 'intracellular * r_0018__Vmax_r_0018 * ( pow ( 1.0 / r_0018__kms_s_0181r_0018 , 1.0 ) * pow ( 1.0 / r_0018__kms_s_0899r_0018 , 1.0 ) * ( pow ( s_0181 , 1.0 ) * pow ( s_0899 , 1.0 ) - pow ( s_0185 , 1.0 ) * pow ( s_0861 , 1.0 ) / r_0018__Keq_r_0018 ) / ( ( 1.0 + s_0181 / r_0018__kms_s_0181r_0018 ) * ( 1.0 + s_0899 / r_0018__kms_s_0899r_0018 ) + ( 1.0 + s_0185 / r_0018__kmp_s_0185r_0018 ) * ( 1.0 + s_0861 / r_0018__kmp_s_0861r_0018 ) - 1.0 ) ) / intracellular '
	# phenylalanine transaminase
	r_0825 = 'intracellular * r_0825__Vmax_r_0825 * ( pow ( 1.0 / r_0825__kms_s_0859r_0825 , 1.0 ) * pow ( 1.0 / r_0825__kms_s_0899r_0825 , 1.0 ) * ( pow ( s_0859 , 1.0 ) * pow ( s_0899 , 1.0 ) - pow ( s_0185 , 1.0 ) * pow ( s_0936 , 1.0 ) / r_0825__Keq_r_0825 ) / ( ( 1.0 + s_0859 / r_0825__kms_s_0859r_0825 ) * ( 1.0 + s_0899 / r_0825__kms_s_0899r_0825 ) + ( 1.0 + s_0185 / r_0825__kmp_s_0185r_0825 ) * ( 1.0 + s_0936 / r_0825__kmp_s_0936r_0825 ) - 1.0 ) ) / intracellular '
	# tyrosine transaminase
	r_1050 = 'intracellular * r_1050__Vmax_r_1050 * ( pow ( 1.0 / r_1050__kms_s_0209r_1050 , 1.0 ) * pow ( 1.0 / r_1050__kms_s_0899r_1050 , 1.0 ) * ( pow ( s_0209 , 1.0 ) * pow ( s_0899 , 1.0 ) - pow ( s_0185 , 1.0 ) * pow ( s_0955 , 1.0 ) / r_1050__Keq_r_1050 ) / ( ( 1.0 + s_0209 / r_1050__kms_s_0209r_1050 ) * ( 1.0 + s_0899 / r_1050__kms_s_0899r_1050 ) + ( 1.0 + s_0185 / r_1050__kmp_s_0185r_1050 ) * ( 1.0 + s_0955 / r_1050__kmp_s_0955r_1050 ) - 1.0 ) ) / intracellular '

	########### mevalonate pathway ###########

	# acetyl-CoA C-acetyltransferase
	r_0118 = 'intracellular * r_0118__Vmax_r_0118 * ( pow ( 1.0 / r_0118__kms_s_0380r_0118 , 2.0 ) * ( pow ( s_0380 , 2.0 ) - pow ( s_0374 , 1.0 ) * pow ( s_0514 , 1.0 ) / r_0118__Keq_r_0118 ) / ( 1.0 + s_0380 / r_0118__kms_s_0380r_0118 + ( 1.0 + s_0374 / r_0118__kmp_s_0374r_0118 ) * ( 1.0 + s_0514 / r_0118__kmp_s_0514r_0118 ) - 1.0 ) ) / intracellular '
	# hydroxymethylglutaryl CoA reductase
	r_0598 = 'intracellular * r_0598__Vmax_r_0598 * ( pow ( 1.0 / r_0598__kms_s_0225r_0598 , 1.0 ) * pow ( 1.0 / r_0598__kms_s_0763_br_0598 , 2.0 ) * pow ( 1.0 / r_0598__kms_s_1096r_0598 , 2.0 ) * ( pow ( s_0225 , 1.0 ) * pow ( s_0763_b , 2.0 ) * pow ( s_1096 , 2.0 ) - pow ( s_0031 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_1091 , 2.0 ) / r_0598__Keq_r_0598 ) / ( ( 1.0 + s_0225 / r_0598__kms_s_0225r_0598 ) * ( 1.0 + s_0763_b / r_0598__kms_s_0763_br_0598 ) * ( 1.0 + s_1096 / r_0598__kms_s_1096r_0598 ) + ( 1.0 + s_0031 / r_0598__kmp_s_0031r_0598 ) * ( 1.0 + s_0514 / r_0598__kmp_s_0514r_0598 ) * ( 1.0 + s_1091 / r_0598__kmp_s_1091r_0598 ) - 1.0 ) ) / intracellular '
	# hydroxymethylglutaryl CoA synthase
	r_0599 = 'intracellular * r_0599__Vmax_r_0599 * ( pow ( 1.0 / r_0599__kms_s_0374r_0599 , 1.0 ) * pow ( 1.0 / r_0599__kms_s_0380r_0599 , 1.0 ) * pow ( 1.0 / r_0599__kms_s_1434_br_0599 , 1.0 ) * ( pow ( s_0374 , 1.0 ) * pow ( s_0380 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0225 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0599__Keq_r_0599 ) / ( ( 1.0 + s_0374 / r_0599__kms_s_0374r_0599 ) * ( 1.0 + s_0380 / r_0599__kms_s_0380r_0599 ) * ( 1.0 + s_1434_b / r_0599__kms_s_1434_br_0599 ) + ( 1.0 + s_0225 / r_0599__kmp_s_0225r_0599 ) * ( 1.0 + s_0514 / r_0599__kmp_s_0514r_0599 ) * ( 1.0 + s_0763_b / r_0599__kmp_s_0763_br_0599 ) - 1.0 ) ) / intracellular '
	# isopentenyl-diphosphate D-isomerase
	r_0638 = 'intracellular * r_0638__Vmax_r_0638 * ( pow ( 1.0 / r_0638__kms_s_0850r_0638 , 1.0 ) * ( pow ( s_0850 , 1.0 ) - pow ( s_1257 , 1.0 ) / r_0638__Keq_r_0638 ) / ( 1.0 + s_0850 / r_0638__kms_s_0850r_0638 + 1.0 + s_1257 / r_0638__kmp_s_1257r_0638 - 1.0 ) ) / intracellular '
	# mevalonate kinase (ctp)
	r_0712 = 'intracellular * r_0712__Vmax_r_0712 * ( pow ( 1.0 / r_0712__kms_s_0031r_0712 , 1.0 ) * pow ( 1.0 / r_0712__kms_s_0521r_0712 , 1.0 ) * ( pow ( s_0031 , 1.0 ) * pow ( s_0521 , 1.0 ) - pow ( s_0022 , 1.0 ) * pow ( s_0481 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0712__Keq_r_0712 ) / ( ( 1.0 + s_0031 / r_0712__kms_s_0031r_0712 ) * ( 1.0 + s_0521 / r_0712__kms_s_0521r_0712 ) + ( 1.0 + s_0022 / r_0712__kmp_s_0022r_0712 ) * ( 1.0 + s_0481 / r_0712__kmp_s_0481r_0712 ) * ( 1.0 + s_0763_b / r_0712__kmp_s_0763_br_0712 ) - 1.0 ) ) / intracellular '
	# mevalonate pyrophoshate decarboxylase
	r_0715 = 'intracellular * r_0715__Vmax_r_0715 * ( pow ( 1.0 / r_0715__kms_s_0021r_0715 , 1.0 ) * pow ( 1.0 / r_0715__kms_s_0446r_0715 , 1.0 ) * ( pow ( s_0021 , 1.0 ) * pow ( s_0446 , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_0470 , 1.0 ) * pow ( s_0850 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0715__Keq_r_0715 ) / ( ( 1.0 + s_0021 / r_0715__kms_s_0021r_0715 ) * ( 1.0 + s_0446 / r_0715__kms_s_0446r_0715 ) + ( 1.0 + s_0400 / r_0715__kmp_s_0400r_0715 ) * ( 1.0 + s_0470 / r_0715__kmp_s_0470r_0715 ) * ( 1.0 + s_0850 / r_0715__kmp_s_0850r_0715 ) * ( 1.0 + s_1207 / r_0715__kmp_s_1207r_0715 ) - 1.0 ) ) / intracellular '
	# phosphomevalonate kinase
	r_0877 = 'intracellular * r_0877__Vmax_r_0877 * ( pow ( 1.0 / r_0877__kms_s_0022r_0877 , 1.0 ) * pow ( 1.0 / r_0877__kms_s_0446r_0877 , 1.0 ) * ( pow ( s_0022 , 1.0 ) * pow ( s_0446 , 1.0 ) - pow ( s_0021 , 1.0 ) * pow ( s_0400 , 1.0 ) / r_0877__Keq_r_0877 ) / ( ( 1.0 + s_0022 / r_0877__kms_s_0022r_0877 ) * ( 1.0 + s_0446 / r_0877__kms_s_0446r_0877 ) + ( 1.0 + s_0021 / r_0877__kmp_s_0021r_0877 ) * ( 1.0 + s_0400 / r_0877__kmp_s_0400r_0877 ) - 1.0 ) ) / intracellular '

	########### myo-inositol biosynthesis ###########

	# myo-inositol 1-phosphatase
	r_0725 = 'intracellular * r_0725__Vmax_r_0725 * ( pow ( 1.0 / r_0725__kms_s_0128r_0725 , 1.0 ) * pow ( 1.0 / r_0725__kms_s_1434_br_0725 , 1.0 ) * ( pow ( s_0128 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_1020 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0725__Keq_r_0725 ) / ( ( 1.0 + s_0128 / r_0725__kms_s_0128r_0725 ) * ( 1.0 + s_1434_b / r_0725__kms_s_1434_br_0725 ) + ( 1.0 + s_1020 / r_0725__kmp_s_1020r_0725 ) * ( 1.0 + s_1207 / r_0725__kmp_s_1207r_0725 ) - 1.0 ) ) / intracellular '
	# myo-inositol-1-phosphate synthase
	r_0726 = 'intracellular * r_0726__Vmax_r_0726 * ( pow ( 1.0 / r_0726__kms_s_0410r_0726 , 1.0 ) * ( pow ( s_0410 , 1.0 ) - pow ( s_0128 , 1.0 ) / r_0726__Keq_r_0726 ) / ( 1.0 + s_0410 / r_0726__kms_s_0410r_0726 + 1.0 + s_0128 / r_0726__kmp_s_0128r_0726 - 1.0 ) ) / intracellular '

	########### myristate biosynthesis ###########

	# fatty acid synthase (n-C10:0)
	r_0417 = 'intracellular * r_0417__Vmax_r_0417 * ( pow ( 1.0 / r_0417__kms_s_0763_br_0417 , 3.0 ) * pow ( 1.0 / r_0417__kms_s_1005r_0417 , 1.0 ) * pow ( 1.0 / r_0417__kms_s_1096r_0417 , 2.0 ) * pow ( 1.0 / r_0417__kms_s_1132r_0417 , 1.0 ) * ( pow ( s_0763_b , 3.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1096 , 2.0 ) * pow ( s_1132 , 1.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_0574 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1434_b , 1.0 ) / r_0417__Keq_r_0417 ) / ( ( 1.0 + s_0763_b / r_0417__kms_s_0763_br_0417 ) * ( 1.0 + s_1005 / r_0417__kms_s_1005r_0417 ) * ( 1.0 + s_1096 / r_0417__kms_s_1096r_0417 ) * ( 1.0 + s_1132 / r_0417__kms_s_1132r_0417 ) + ( 1.0 + s_0470 / r_0417__kmp_s_0470r_0417 ) * ( 1.0 + s_0514 / r_0417__kmp_s_0514r_0417 ) * ( 1.0 + s_0574 / r_0417__kmp_s_0574r_0417 ) * ( 1.0 + s_1091 / r_0417__kmp_s_1091r_0417 ) * ( 1.0 + s_1434_b / r_0417__kmp_s_1434_br_0417 ) - 1.0 ) ) / intracellular '
	# fatty acid synthase (n-C12:0)
	r_0418 = 'intracellular * r_0418__Vmax_r_0418 * ( pow ( 1.0 / r_0418__kms_s_0574r_0418 , 1.0 ) * pow ( 1.0 / r_0418__kms_s_0763_br_0418 , 3.0 ) * pow ( 1.0 / r_0418__kms_s_1005r_0418 , 1.0 ) * pow ( 1.0 / r_0418__kms_s_1096r_0418 , 2.0 ) * ( pow ( s_0574 , 1.0 ) * pow ( s_0763_b , 3.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1096 , 2.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_0968 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1434_b , 1.0 ) / r_0418__Keq_r_0418 ) / ( ( 1.0 + s_0574 / r_0418__kms_s_0574r_0418 ) * ( 1.0 + s_0763_b / r_0418__kms_s_0763_br_0418 ) * ( 1.0 + s_1005 / r_0418__kms_s_1005r_0418 ) * ( 1.0 + s_1096 / r_0418__kms_s_1096r_0418 ) + ( 1.0 + s_0470 / r_0418__kmp_s_0470r_0418 ) * ( 1.0 + s_0514 / r_0418__kmp_s_0514r_0418 ) * ( 1.0 + s_0968 / r_0418__kmp_s_0968r_0418 ) * ( 1.0 + s_1091 / r_0418__kmp_s_1091r_0418 ) * ( 1.0 + s_1434_b / r_0418__kmp_s_1434_br_0418 ) - 1.0 ) ) / intracellular '
	# fatty acid synthase (n-C14:0)
	r_0419 = 'intracellular * r_0419__Vmax_r_0419 * ( pow ( 1.0 / r_0419__kms_s_0763_br_0419 , 3.0 ) * pow ( 1.0 / r_0419__kms_s_0968r_0419 , 1.0 ) * pow ( 1.0 / r_0419__kms_s_1005r_0419 , 1.0 ) * pow ( 1.0 / r_0419__kms_s_1096r_0419 , 2.0 ) * ( pow ( s_0763_b , 3.0 ) * pow ( s_0968 , 1.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1096 , 2.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_1028 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1434_b , 1.0 ) / r_0419__Keq_r_0419 ) / ( ( 1.0 + s_0763_b / r_0419__kms_s_0763_br_0419 ) * ( 1.0 + s_0968 / r_0419__kms_s_0968r_0419 ) * ( 1.0 + s_1005 / r_0419__kms_s_1005r_0419 ) * ( 1.0 + s_1096 / r_0419__kms_s_1096r_0419 ) + ( 1.0 + s_0470 / r_0419__kmp_s_0470r_0419 ) * ( 1.0 + s_0514 / r_0419__kmp_s_0514r_0419 ) * ( 1.0 + s_1028 / r_0419__kmp_s_1028r_0419 ) * ( 1.0 + s_1091 / r_0419__kmp_s_1091r_0419 ) * ( 1.0 + s_1434_b / r_0419__kmp_s_1434_br_0419 ) - 1.0 ) ) / intracellular '
	# fatty acid synthase (n-C16:0)
	r_0421 = 'intracellular * r_0421__Vmax_r_0421 * ( pow ( 1.0 / r_0421__kms_s_0763_br_0421 , 3.0 ) * pow ( 1.0 / r_0421__kms_s_1005r_0421 , 1.0 ) * pow ( 1.0 / r_0421__kms_s_1028r_0421 , 1.0 ) * pow ( 1.0 / r_0421__kms_s_1096r_0421 , 2.0 ) * ( pow ( s_0763_b , 3.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1028 , 1.0 ) * pow ( s_1096 , 2.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1170 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0421__Keq_r_0421 ) / ( ( 1.0 + s_0763_b / r_0421__kms_s_0763_br_0421 ) * ( 1.0 + s_1005 / r_0421__kms_s_1005r_0421 ) * ( 1.0 + s_1028 / r_0421__kms_s_1028r_0421 ) * ( 1.0 + s_1096 / r_0421__kms_s_1096r_0421 ) + ( 1.0 + s_0470 / r_0421__kmp_s_0470r_0421 ) * ( 1.0 + s_0514 / r_0421__kmp_s_0514r_0421 ) * ( 1.0 + s_1091 / r_0421__kmp_s_1091r_0421 ) * ( 1.0 + s_1170 / r_0421__kmp_s_1170r_0421 ) * ( 1.0 + s_1434_b / r_0421__kmp_s_1434_br_0421 ) - 1.0 ) ) / intracellular '
	# fatty acid synthase (n-C18:0)
	r_0423 = 'intracellular * r_0423__Vmax_r_0423 * ( pow ( 1.0 / r_0423__kms_s_0763_br_0423 , 3.0 ) * pow ( 1.0 / r_0423__kms_s_1005r_0423 , 1.0 ) * pow ( 1.0 / r_0423__kms_s_1096r_0423 , 2.0 ) * pow ( 1.0 / r_0423__kms_s_1170r_0423 , 1.0 ) * ( pow ( s_0763_b , 3.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1096 , 2.0 ) * pow ( s_1170 , 1.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1329 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0423__Keq_r_0423 ) / ( ( 1.0 + s_0763_b / r_0423__kms_s_0763_br_0423 ) * ( 1.0 + s_1005 / r_0423__kms_s_1005r_0423 ) * ( 1.0 + s_1096 / r_0423__kms_s_1096r_0423 ) * ( 1.0 + s_1170 / r_0423__kms_s_1170r_0423 ) + ( 1.0 + s_0470 / r_0423__kmp_s_0470r_0423 ) * ( 1.0 + s_0514 / r_0423__kmp_s_0514r_0423 ) * ( 1.0 + s_1091 / r_0423__kmp_s_1091r_0423 ) * ( 1.0 + s_1329 / r_0423__kmp_s_1329r_0423 ) * ( 1.0 + s_1434_b / r_0423__kmp_s_1434_br_0423 ) - 1.0 ) ) / intracellular '
	# fatty acyl-CoA synthase (n-C10:0CoA)
	r_0429 = 'intracellular * r_0429__Vmax_r_0429 * ( pow ( 1.0 / r_0429__kms_s_0763_br_0429 , 3.0 ) * pow ( 1.0 / r_0429__kms_s_1005r_0429 , 1.0 ) * pow ( 1.0 / r_0429__kms_s_1096r_0429 , 2.0 ) * pow ( 1.0 / r_0429__kms_s_1140r_0429 , 1.0 ) * ( pow ( s_0763_b , 3.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1096 , 2.0 ) * pow ( s_1140 , 1.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_0582 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1434_b , 1.0 ) / r_0429__Keq_r_0429 ) / ( ( 1.0 + s_0763_b / r_0429__kms_s_0763_br_0429 ) * ( 1.0 + s_1005 / r_0429__kms_s_1005r_0429 ) * ( 1.0 + s_1096 / r_0429__kms_s_1096r_0429 ) * ( 1.0 + s_1140 / r_0429__kms_s_1140r_0429 ) + ( 1.0 + s_0470 / r_0429__kmp_s_0470r_0429 ) * ( 1.0 + s_0514 / r_0429__kmp_s_0514r_0429 ) * ( 1.0 + s_0582 / r_0429__kmp_s_0582r_0429 ) * ( 1.0 + s_1091 / r_0429__kmp_s_1091r_0429 ) * ( 1.0 + s_1434_b / r_0429__kmp_s_1434_br_0429 ) - 1.0 ) ) / intracellular '
	# fatty acyl-CoA synthase (n-C8:0CoA), lumped reaction
	r_0430 = 'intracellular * r_0430__Vmax_r_0430 * ( pow ( 1.0 / r_0430__kms_s_0380r_0430 , 1.0 ) * pow ( 1.0 / r_0430__kms_s_0763_br_0430 , 9.0 ) * pow ( 1.0 / r_0430__kms_s_1005r_0430 , 3.0 ) * pow ( 1.0 / r_0430__kms_s_1096r_0430 , 6.0 ) * ( pow ( s_0380 , 1.0 ) * pow ( s_0763_b , 9.0 ) * pow ( s_1005 , 3.0 ) * pow ( s_1096 , 6.0 ) - pow ( s_0470 , 3.0 ) * pow ( s_0514 , 3.0 ) * pow ( s_1091 , 6.0 ) * pow ( s_1140 , 1.0 ) * pow ( s_1434_b , 3.0 ) / r_0430__Keq_r_0430 ) / ( ( 1.0 + s_0380 / r_0430__kms_s_0380r_0430 ) * ( 1.0 + s_0763_b / r_0430__kms_s_0763_br_0430 ) * ( 1.0 + s_1005 / r_0430__kms_s_1005r_0430 ) * ( 1.0 + s_1096 / r_0430__kms_s_1096r_0430 ) + ( 1.0 + s_0470 / r_0430__kmp_s_0470r_0430 ) * ( 1.0 + s_0514 / r_0430__kmp_s_0514r_0430 ) * ( 1.0 + s_1091 / r_0430__kmp_s_1091r_0430 ) * ( 1.0 + s_1140 / r_0430__kmp_s_1140r_0430 ) * ( 1.0 + s_1434_b / r_0430__kmp_s_1434_br_0430 ) - 1.0 ) ) / intracellular '
	# fatty-acyl-CoA synthase (n-C12:0CoA)
	r_0464 = 'intracellular * r_0464__Vmax_r_0464 * ( pow ( 1.0 / r_0464__kms_s_0582r_0464 , 1.0 ) * pow ( 1.0 / r_0464__kms_s_0763_br_0464 , 3.0 ) * pow ( 1.0 / r_0464__kms_s_1005r_0464 , 1.0 ) * pow ( 1.0 / r_0464__kms_s_1096r_0464 , 2.0 ) * ( pow ( s_0582 , 1.0 ) * pow ( s_0763_b , 3.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1096 , 2.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_0977 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1434_b , 1.0 ) / r_0464__Keq_r_0464 ) / ( ( 1.0 + s_0582 / r_0464__kms_s_0582r_0464 ) * ( 1.0 + s_0763_b / r_0464__kms_s_0763_br_0464 ) * ( 1.0 + s_1005 / r_0464__kms_s_1005r_0464 ) * ( 1.0 + s_1096 / r_0464__kms_s_1096r_0464 ) + ( 1.0 + s_0470 / r_0464__kmp_s_0470r_0464 ) * ( 1.0 + s_0514 / r_0464__kmp_s_0514r_0464 ) * ( 1.0 + s_0977 / r_0464__kmp_s_0977r_0464 ) * ( 1.0 + s_1091 / r_0464__kmp_s_1091r_0464 ) * ( 1.0 + s_1434_b / r_0464__kmp_s_1434_br_0464 ) - 1.0 ) ) / intracellular '
	# fatty-acyl-CoA synthase (n-C14:0CoA)
	r_0465 = 'intracellular * r_0465__Vmax_r_0465 * ( pow ( 1.0 / r_0465__kms_s_0763_br_0465 , 3.0 ) * pow ( 1.0 / r_0465__kms_s_0977r_0465 , 1.0 ) * pow ( 1.0 / r_0465__kms_s_1005r_0465 , 1.0 ) * pow ( 1.0 / r_0465__kms_s_1096r_0465 , 2.0 ) * ( pow ( s_0763_b , 3.0 ) * pow ( s_0977 , 1.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1096 , 2.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_1044 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1434_b , 1.0 ) / r_0465__Keq_r_0465 ) / ( ( 1.0 + s_0763_b / r_0465__kms_s_0763_br_0465 ) * ( 1.0 + s_0977 / r_0465__kms_s_0977r_0465 ) * ( 1.0 + s_1005 / r_0465__kms_s_1005r_0465 ) * ( 1.0 + s_1096 / r_0465__kms_s_1096r_0465 ) + ( 1.0 + s_0470 / r_0465__kmp_s_0470r_0465 ) * ( 1.0 + s_0514 / r_0465__kmp_s_0514r_0465 ) * ( 1.0 + s_1044 / r_0465__kmp_s_1044r_0465 ) * ( 1.0 + s_1091 / r_0465__kmp_s_1091r_0465 ) * ( 1.0 + s_1434_b / r_0465__kmp_s_1434_br_0465 ) - 1.0 ) ) / intracellular '
	# fatty-acyl-CoA synthase (n-C16:0CoA)
	r_0466 = 'intracellular * r_0466__Vmax_r_0466 * ( pow ( 1.0 / r_0466__kms_s_0763_br_0466 , 3.0 ) * pow ( 1.0 / r_0466__kms_s_1005r_0466 , 1.0 ) * pow ( 1.0 / r_0466__kms_s_1044r_0466 , 1.0 ) * pow ( 1.0 / r_0466__kms_s_1096r_0466 , 2.0 ) * ( pow ( s_0763_b , 3.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1044 , 1.0 ) * pow ( s_1096 , 2.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1187 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0466__Keq_r_0466 ) / ( ( 1.0 + s_0763_b / r_0466__kms_s_0763_br_0466 ) * ( 1.0 + s_1005 / r_0466__kms_s_1005r_0466 ) * ( 1.0 + s_1044 / r_0466__kms_s_1044r_0466 ) * ( 1.0 + s_1096 / r_0466__kms_s_1096r_0466 ) + ( 1.0 + s_0470 / r_0466__kmp_s_0470r_0466 ) * ( 1.0 + s_0514 / r_0466__kmp_s_0514r_0466 ) * ( 1.0 + s_1091 / r_0466__kmp_s_1091r_0466 ) * ( 1.0 + s_1187 / r_0466__kmp_s_1187r_0466 ) * ( 1.0 + s_1434_b / r_0466__kmp_s_1434_br_0466 ) - 1.0 ) ) / intracellular '
	# fatty-acyl-CoA synthase (n-C18:0CoA)
	r_0467 = 'intracellular * r_0467__Vmax_r_0467 * ( pow ( 1.0 / r_0467__kms_s_0763_br_0467 , 3.0 ) * pow ( 1.0 / r_0467__kms_s_1005r_0467 , 1.0 ) * pow ( 1.0 / r_0467__kms_s_1096r_0467 , 2.0 ) * pow ( 1.0 / r_0467__kms_s_1187r_0467 , 1.0 ) * ( pow ( s_0763_b , 3.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1096 , 2.0 ) * pow ( s_1187 , 1.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1334 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0467__Keq_r_0467 ) / ( ( 1.0 + s_0763_b / r_0467__kms_s_0763_br_0467 ) * ( 1.0 + s_1005 / r_0467__kms_s_1005r_0467 ) * ( 1.0 + s_1096 / r_0467__kms_s_1096r_0467 ) * ( 1.0 + s_1187 / r_0467__kms_s_1187r_0467 ) + ( 1.0 + s_0470 / r_0467__kmp_s_0470r_0467 ) * ( 1.0 + s_0514 / r_0467__kmp_s_0514r_0467 ) * ( 1.0 + s_1091 / r_0467__kmp_s_1091r_0467 ) * ( 1.0 + s_1334 / r_0467__kmp_s_1334r_0467 ) * ( 1.0 + s_1434_b / r_0467__kmp_s_1434_br_0467 ) - 1.0 ) ) / intracellular '

	########### pentose phosphate pathway ###########

	# ribose-5-phosphate isomerase
	r_0963 = 'intracellular * r_0963__Vmax_r_0963 * ( pow ( 1.0 / r_0963__kms_s_0557r_0963 , 1.0 ) * ( pow ( s_0557 , 1.0 ) - pow ( s_0427 , 1.0 ) / r_0963__Keq_r_0963 ) / ( 1.0 + s_0557 / r_0963__kms_s_0557r_0963 + 1.0 + s_0427 / r_0963__kmp_s_0427r_0963 - 1.0 ) ) / intracellular '
	# ribulose 5-phosphate 3-epimerase
	r_0965 = 'intracellular * r_0965__Vmax_r_0965 * ( pow ( 1.0 / r_0965__kms_s_0561r_0965 , 1.0 ) * ( pow ( s_0561 , 1.0 ) - pow ( s_0557 , 1.0 ) / r_0965__Keq_r_0965 ) / ( 1.0 + s_0561 / r_0965__kms_s_0561r_0965 + 1.0 + s_0557 / r_0965__kmp_s_0557r_0965 - 1.0 ) ) / intracellular '
	# transaldolase
	r_1035 = 'intracellular * r_1035__Vmax_r_1035 * ( pow ( 1.0 / r_1035__kms_s_0533r_1035 , 1.0 ) * pow ( 1.0 / r_1035__kms_s_0539r_1035 , 1.0 ) * ( pow ( s_0533 , 1.0 ) * pow ( s_0539 , 1.0 ) - pow ( s_0731 , 1.0 ) * pow ( s_1304 , 1.0 ) / r_1035__Keq_r_1035 ) / ( ( 1.0 + s_0533 / r_1035__kms_s_0533r_1035 ) * ( 1.0 + s_0539 / r_1035__kms_s_0539r_1035 ) + ( 1.0 + s_0731 / r_1035__kmp_s_0731r_1035 ) * ( 1.0 + s_1304 / r_1035__kmp_s_1304r_1035 ) - 1.0 ) ) / intracellular '
	# transketolase
	r_1036 = 'intracellular * r_1036__Vmax_r_1036 * ( pow ( 1.0 / r_1036__kms_s_0731r_1036 , 1.0 ) * pow ( 1.0 / r_1036__kms_s_1304r_1036 , 1.0 ) * ( pow ( s_0731 , 1.0 ) * pow ( s_1304 , 1.0 ) - pow ( s_0427 , 1.0 ) * pow ( s_0561 , 1.0 ) / r_1036__Keq_r_1036 ) / ( ( 1.0 + s_0731 / r_1036__kms_s_0731r_1036 ) * ( 1.0 + s_1304 / r_1036__kms_s_1304r_1036 ) + ( 1.0 + s_0427 / r_1036__kmp_s_0427r_1036 ) * ( 1.0 + s_0561 / r_1036__kmp_s_0561r_1036 ) - 1.0 ) ) / intracellular '
	# transketolase_2
	r_1037 = 'intracellular * r_1037__Vmax_r_1037 * ( pow ( 1.0 / r_1037__kms_s_0539r_1037 , 1.0 ) * pow ( 1.0 / r_1037__kms_s_0731r_1037 , 1.0 ) * ( pow ( s_0539 , 1.0 ) * pow ( s_0731 , 1.0 ) - pow ( s_0533 , 1.0 ) * pow ( s_0561 , 1.0 ) / r_1037__Keq_r_1037 ) / ( ( 1.0 + s_0539 / r_1037__kms_s_0539r_1037 ) * ( 1.0 + s_0731 / r_1037__kms_s_0731r_1037 ) + ( 1.0 + s_0533 / r_1037__kmp_s_0533r_1037 ) * ( 1.0 + s_0561 / r_1037__kmp_s_0561r_1037 ) - 1.0 ) ) / intracellular '

	########### phenylalanine biosynthesis ###########

	# chorismate mutase
	r_0304 = 'intracellular * r_0304__Vmax_r_0304 * ( pow ( 1.0 / r_0304__kms_s_0500r_0304 , 1.0 ) * ( pow ( s_0500 , 1.0 ) - pow ( s_1258 , 1.0 ) / r_0304__Keq_r_0304 ) / ( 1.0 + s_0500 / r_0304__kms_s_0500r_0304 + 1.0 + s_1258 / r_0304__kmp_s_1258r_0304 - 1.0 ) ) / intracellular '
	# prephenate dehydratase
	r_0911 = 'intracellular * r_0911__Vmax_r_0911 * ( pow ( 1.0 / r_0911__kms_s_0763_br_0911 , 1.0 ) * pow ( 1.0 / r_0911__kms_s_1258r_0911 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_1258 , 1.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0859 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0911__Keq_r_0911 ) / ( ( 1.0 + s_0763_b / r_0911__kms_s_0763_br_0911 ) * ( 1.0 + s_1258 / r_0911__kms_s_1258r_0911 ) + ( 1.0 + s_0470 / r_0911__kmp_s_0470r_0911 ) * ( 1.0 + s_0859 / r_0911__kmp_s_0859r_0911 ) * ( 1.0 + s_1434_b / r_0911__kmp_s_1434_br_0911 ) - 1.0 ) ) / intracellular '

	########### phenylalanine degradation ###########

	# alcohol dehydrogenase, reverse rxn (acetaldehyde -> ethanol)
	r_0183 = 'intracellular * r_0183__Vmax_r_0183 * ( pow ( 1.0 / r_0183__kms_s_0366r_0183 , 1.0 ) * pow ( 1.0 / r_0183__kms_s_0763_br_0183 , 1.0 ) * pow ( 1.0 / r_0183__kms_s_1087r_0183 , 1.0 ) * ( pow ( s_0366 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1087 , 1.0 ) - pow ( s_0650 , 1.0 ) * pow ( s_1082 , 1.0 ) / r_0183__Keq_r_0183 ) / ( ( 1.0 + s_0366 / r_0183__kms_s_0366r_0183 ) * ( 1.0 + s_0763_b / r_0183__kms_s_0763_br_0183 ) * ( 1.0 + s_1087 / r_0183__kms_s_1087r_0183 ) + ( 1.0 + s_0650 / r_0183__kmp_s_0650r_0183 ) * ( 1.0 + s_1082 / r_0183__kmp_s_1082r_0183 ) - 1.0 ) ) / intracellular '

	########### phosphatidylinositol biosynthesis ###########

	# phosphatidylinositol synthase
	r_0847 = 'intracellular * r_0847__Vmax_r_0847 * ( pow ( 1.0 / r_0847__kms_s_0485r_0847 , 1.0 ) * pow ( 1.0 / r_0847__kms_s_1020r_0847 , 1.0 ) * ( pow ( s_0485 , 1.0 ) * pow ( s_1020 , 1.0 ) - pow ( s_0090 , 1.0 ) * pow ( s_0511 , 1.0 ) * pow ( s_0763_b , 2.0 ) / r_0847__Keq_r_0847 ) / ( ( 1.0 + s_0485 / r_0847__kms_s_0485r_0847 ) * ( 1.0 + s_1020 / r_0847__kms_s_1020r_0847 ) + ( 1.0 + s_0090 / r_0847__kmp_s_0090r_0847 ) * ( 1.0 + s_0511 / r_0847__kmp_s_0511r_0847 ) * ( 1.0 + s_0763_b / r_0847__kmp_s_0763_br_0847 ) - 1.0 ) ) / intracellular '

	########### proline biosynthesis ###########

	# glutamate 5-kinase
	r_0506 = 'intracellular * r_0506__Vmax_r_0506 * ( pow ( 1.0 / r_0506__kms_s_0446r_0506 , 1.0 ) * pow ( 1.0 / r_0506__kms_s_0899r_0506 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_0899 , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_0894 , 1.0 ) / r_0506__Keq_r_0506 ) / ( ( 1.0 + s_0446 / r_0506__kms_s_0446r_0506 ) * ( 1.0 + s_0899 / r_0506__kms_s_0899r_0506 ) + ( 1.0 + s_0400 / r_0506__kmp_s_0400r_0506 ) * ( 1.0 + s_0894 / r_0506__kmp_s_0894r_0506 ) - 1.0 ) ) / intracellular '
	# glutamate-5-semialdehyde dehydrogenase
	r_0512 = 'intracellular * r_0512__Vmax_r_0512 * ( pow ( 1.0 / r_0512__kms_s_0763_br_0512 , 1.0 ) * pow ( 1.0 / r_0512__kms_s_0894r_0512 , 1.0 ) * pow ( 1.0 / r_0512__kms_s_1087r_0512 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_0894 , 1.0 ) * pow ( s_1087 , 1.0 ) - pow ( s_0905 , 1.0 ) * pow ( s_1082 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0512__Keq_r_0512 ) / ( ( 1.0 + s_0763_b / r_0512__kms_s_0763_br_0512 ) * ( 1.0 + s_0894 / r_0512__kms_s_0894r_0512 ) * ( 1.0 + s_1087 / r_0512__kms_s_1087r_0512 ) + ( 1.0 + s_0905 / r_0512__kmp_s_0905r_0512 ) * ( 1.0 + s_1082 / r_0512__kmp_s_1082r_0512 ) * ( 1.0 + s_1207 / r_0512__kmp_s_1207r_0512 ) - 1.0 ) ) / intracellular '
	# L-glutamate 5-semialdehyde dehydratase
	r_0657 = 'intracellular * r_0657__Vmax_r_0657 * ( pow ( 1.0 / r_0657__kms_s_0905r_0657 , 1.0 ) * ( pow ( s_0905 , 1.0 ) - pow ( s_0120 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0657__Keq_r_0657 ) / ( 1.0 + s_0905 / r_0657__kms_s_0905r_0657 + ( 1.0 + s_0120 / r_0657__kmp_s_0120r_0657 ) * ( 1.0 + s_0763_b / r_0657__kmp_s_0763_br_0657 ) * ( 1.0 + s_1434_b / r_0657__kmp_s_1434_br_0657 ) - 1.0 ) ) / intracellular '
	# L-hydroxyproline reductase (NAD)
	r_0661 = 'intracellular * r_0661__Vmax_r_0661 * ( pow ( 1.0 / r_0661__kms_s_0118r_0661 , 1.0 ) * pow ( 1.0 / r_0661__kms_s_0763_br_0661 , 2.0 ) * pow ( 1.0 / r_0661__kms_s_1087r_0661 , 1.0 ) * ( pow ( s_0118 , 1.0 ) * pow ( s_0763_b , 2.0 ) * pow ( s_1087 , 1.0 ) - pow ( s_1082 , 1.0 ) * pow ( s_1379 , 1.0 ) / r_0661__Keq_r_0661 ) / ( ( 1.0 + s_0118 / r_0661__kms_s_0118r_0661 ) * ( 1.0 + s_0763_b / r_0661__kms_s_0763_br_0661 ) * ( 1.0 + s_1087 / r_0661__kms_s_1087r_0661 ) + ( 1.0 + s_1082 / r_0661__kmp_s_1082r_0661 ) * ( 1.0 + s_1379 / r_0661__kmp_s_1379r_0661 ) - 1.0 ) ) / intracellular '
	# pyrroline-5-carboxylate reductase
	r_0936 = 'intracellular * r_0936__Vmax_r_0936 * ( pow ( 1.0 / r_0936__kms_s_0120r_0936 , 1.0 ) * pow ( 1.0 / r_0936__kms_s_0763_br_0936 , 2.0 ) * pow ( 1.0 / r_0936__kms_s_1096r_0936 , 1.0 ) * ( pow ( s_0120 , 1.0 ) * pow ( s_0763_b , 2.0 ) * pow ( s_1096 , 1.0 ) - pow ( s_0939 , 1.0 ) * pow ( s_1091 , 1.0 ) / r_0936__Keq_r_0936 ) / ( ( 1.0 + s_0120 / r_0936__kms_s_0120r_0936 ) * ( 1.0 + s_0763_b / r_0936__kms_s_0763_br_0936 ) * ( 1.0 + s_1096 / r_0936__kms_s_1096r_0936 ) + ( 1.0 + s_0939 / r_0936__kmp_s_0939r_0936 ) * ( 1.0 + s_1091 / r_0936__kmp_s_1091r_0936 ) - 1.0 ) ) / intracellular '

	########### proline utilization ###########

	# L-hydroxyproline dehydrogenase (NADP)
	r_0660 = 'intracellular * r_0660__Vmax_r_0660 * ( pow ( 1.0 / r_0660__kms_s_1091r_0660 , 1.0 ) * pow ( 1.0 / r_0660__kms_s_1379r_0660 , 1.0 ) * ( pow ( s_1091 , 1.0 ) * pow ( s_1379 , 1.0 ) - pow ( s_0118 , 1.0 ) * pow ( s_0763_b , 2.0 ) * pow ( s_1096 , 1.0 ) / r_0660__Keq_r_0660 ) / ( ( 1.0 + s_1091 / r_0660__kms_s_1091r_0660 ) * ( 1.0 + s_1379 / r_0660__kms_s_1379r_0660 ) + ( 1.0 + s_0118 / r_0660__kmp_s_0118r_0660 ) * ( 1.0 + s_0763_b / r_0660__kmp_s_0763_br_0660 ) * ( 1.0 + s_1096 / r_0660__kmp_s_1096r_0660 ) - 1.0 ) ) / intracellular '

	########### pyruvate dehydrogenase complex ###########

	# pyruvate dehydrogenase
	r_0940 = 'intracellular * r_0940__Vmax_r_0940 * ( pow ( 1.0 / r_0940__kms_s_0514r_0940 , 1.0 ) * pow ( 1.0 / r_0940__kms_s_1082r_0940 , 1.0 ) * pow ( 1.0 / r_0940__kms_s_1277r_0940 , 1.0 ) * ( pow ( s_0514 , 1.0 ) * pow ( s_1082 , 1.0 ) * pow ( s_1277 , 1.0 ) - pow ( s_0380 , 1.0 ) * pow ( s_0470 , 1.0 ) * pow ( s_1087 , 1.0 ) / r_0940__Keq_r_0940 ) / ( ( 1.0 + s_0514 / r_0940__kms_s_0514r_0940 ) * ( 1.0 + s_1082 / r_0940__kms_s_1082r_0940 ) * ( 1.0 + s_1277 / r_0940__kms_s_1277r_0940 ) + ( 1.0 + s_0380 / r_0940__kmp_s_0380r_0940 ) * ( 1.0 + s_0470 / r_0940__kmp_s_0470r_0940 ) * ( 1.0 + s_1087 / r_0940__kmp_s_1087r_0940 ) - 1.0 ) ) / intracellular '

	########### removal of superoxide radicals ###########

	# catalase
	r_0282 = 'intracellular * r_0282__Vmax_r_0282 * ( pow ( 1.0 / r_0282__kms_s_0801r_0282 , 2.0 ) * ( pow ( s_0801 , 2.0 ) - pow ( s_1160 , 1.0 ) * pow ( s_1434_b , 2.0 ) / r_0282__Keq_r_0282 ) / ( 1.0 + s_0801 / r_0282__kms_s_0801r_0282 + ( 1.0 + s_1160 / r_0282__kmp_s_1160r_0282 ) * ( 1.0 + s_1434_b / r_0282__kmp_s_1434_br_0282 ) - 1.0 ) ) / intracellular '

	########### riboflavin, FMN and FAD biosynthesis ###########

	# 2,5-diamino-6-ribitylamino-4(3H)-pyrimidinone 5'-phosphate deaminase
	r_0014 = 'intracellular * r_0014__Vmax_r_0014 * ( pow ( 1.0 / r_0014__kms_s_0146r_0014 , 1.0 ) * pow ( 1.0 / r_0014__kms_s_0763_br_0014 , 1.0 ) * pow ( 1.0 / r_0014__kms_s_1434_br_0014 , 1.0 ) * ( pow ( s_0146 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0319 , 1.0 ) * pow ( s_0430 , 1.0 ) / r_0014__Keq_r_0014 ) / ( ( 1.0 + s_0146 / r_0014__kms_s_0146r_0014 ) * ( 1.0 + s_0763_b / r_0014__kms_s_0763_br_0014 ) * ( 1.0 + s_1434_b / r_0014__kms_s_1434_br_0014 ) + ( 1.0 + s_0319 / r_0014__kmp_s_0319r_0014 ) * ( 1.0 + s_0430 / r_0014__kmp_s_0430r_0014 ) - 1.0 ) ) / intracellular '
	# 2,5-diamino-6-ribosylamino-4(3H)-pyrimidinone 5'-phosphate reductase (NADPH)
	r_0015 = 'intracellular * r_0015__Vmax_r_0015 * ( pow ( 1.0 / r_0015__kms_s_0145r_0015 , 1.0 ) * pow ( 1.0 / r_0015__kms_s_0763_br_0015 , 1.0 ) * pow ( 1.0 / r_0015__kms_s_1096r_0015 , 1.0 ) * ( pow ( s_0145 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) - pow ( s_0146 , 1.0 ) * pow ( s_1091 , 1.0 ) / r_0015__Keq_r_0015 ) / ( ( 1.0 + s_0145 / r_0015__kms_s_0145r_0015 ) * ( 1.0 + s_0763_b / r_0015__kms_s_0763_br_0015 ) * ( 1.0 + s_1096 / r_0015__kms_s_1096r_0015 ) + ( 1.0 + s_0146 / r_0015__kmp_s_0146r_0015 ) * ( 1.0 + s_1091 / r_0015__kmp_s_1091r_0015 ) - 1.0 ) ) / intracellular '
	# 3,4-dihydroxy-2-butanone-4-phosphate synthase
	r_0040 = 'intracellular * r_0040__Vmax_r_0040 * ( pow ( 1.0 / r_0040__kms_s_0557r_0040 , 1.0 ) * ( pow ( s_0557 , 1.0 ) - pow ( s_0163 , 1.0 ) * pow ( s_0689 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0040__Keq_r_0040 ) / ( 1.0 + s_0557 / r_0040__kms_s_0557r_0040 + ( 1.0 + s_0163 / r_0040__kmp_s_0163r_0040 ) * ( 1.0 + s_0689 / r_0040__kmp_s_0689r_0040 ) * ( 1.0 + s_0763_b / r_0040__kmp_s_0763_br_0040 ) - 1.0 ) ) / intracellular '
	# GTP cyclohydrolase II
	r_0562 = 'intracellular * r_0562__Vmax_r_0562 * ( pow ( 1.0 / r_0562__kms_s_0755r_0562 , 1.0 ) * pow ( 1.0 / r_0562__kms_s_1434_br_0562 , 3.0 ) * ( pow ( s_0755 , 1.0 ) * pow ( s_1434_b , 3.0 ) - pow ( s_0145 , 1.0 ) * pow ( s_0605 , 1.0 ) * pow ( s_0689 , 1.0 ) * pow ( s_0763_b , 2.0 ) / r_0562__Keq_r_0562 ) / ( ( 1.0 + s_0755 / r_0562__kms_s_0755r_0562 ) * ( 1.0 + s_1434_b / r_0562__kms_s_1434_br_0562 ) + ( 1.0 + s_0145 / r_0562__kmp_s_0145r_0562 ) * ( 1.0 + s_0605 / r_0562__kmp_s_0605r_0562 ) * ( 1.0 + s_0689 / r_0562__kmp_s_0689r_0562 ) * ( 1.0 + s_0763_b / r_0562__kmp_s_0763_br_0562 ) - 1.0 ) ) / intracellular '
	# riboflavin synthase
	r_0948 = 'intracellular * r_0948__Vmax_r_0948 * ( pow ( 1.0 / r_0948__kms_s_0163r_0948 , 1.0 ) * pow ( 1.0 / r_0948__kms_s_0320r_0948 , 1.0 ) * ( pow ( s_0163 , 1.0 ) * pow ( s_0320 , 1.0 ) - pow ( s_0335 , 1.0 ) * pow ( s_1207 , 1.0 ) * pow ( s_1434_b , 2.0 ) / r_0948__Keq_r_0948 ) / ( ( 1.0 + s_0163 / r_0948__kms_s_0163r_0948 ) * ( 1.0 + s_0320 / r_0948__kms_s_0320r_0948 ) + ( 1.0 + s_0335 / r_0948__kmp_s_0335r_0948 ) * ( 1.0 + s_1207 / r_0948__kmp_s_1207r_0948 ) * ( 1.0 + s_1434_b / r_0948__kmp_s_1434_br_0948 ) - 1.0 ) ) / intracellular '
	# riboflavin synthase_2
	r_0949 = 'intracellular * r_0949__Vmax_r_0949 * ( pow ( 1.0 / r_0949__kms_s_0335r_0949 , 2.0 ) * ( pow ( s_0335 , 2.0 ) - pow ( s_0320 , 1.0 ) * pow ( s_1283 , 1.0 ) / r_0949__Keq_r_0949 ) / ( 1.0 + s_0335 / r_0949__kms_s_0335r_0949 + ( 1.0 + s_0320 / r_0949__kmp_s_0320r_0949 ) * ( 1.0 + s_1283 / r_0949__kmp_s_1283r_0949 ) - 1.0 ) ) / intracellular '

	########### salvage pathways of pyrimidine ribonucleotides ###########

	# nucleoside-diphosphate kinase (ATP:CDP)
	r_0771 = 'intracellular * r_0771__Vmax_r_0771 * ( pow ( 1.0 / r_0771__kms_s_0400r_0771 , 1.0 ) * pow ( 1.0 / r_0771__kms_s_0521r_0771 , 1.0 ) * ( pow ( s_0400 , 1.0 ) * pow ( s_0521 , 1.0 ) - pow ( s_0446 , 1.0 ) * pow ( s_0481 , 1.0 ) / r_0771__Keq_r_0771 ) / ( ( 1.0 + s_0400 / r_0771__kms_s_0400r_0771 ) * ( 1.0 + s_0521 / r_0771__kms_s_0521r_0771 ) + ( 1.0 + s_0446 / r_0771__kmp_s_0446r_0771 ) * ( 1.0 + s_0481 / r_0771__kmp_s_0481r_0771 ) - 1.0 ) ) / intracellular '
	# nucleoside-diphosphate kinase (ATP:UDP)
	r_0779 = 'intracellular * r_0779__Vmax_r_0779 * ( pow ( 1.0 / r_0779__kms_s_0446r_0779 , 1.0 ) * pow ( 1.0 / r_0779__kms_s_1411r_0779 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_1411 , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_1430 , 1.0 ) / r_0779__Keq_r_0779 ) / ( ( 1.0 + s_0446 / r_0779__kms_s_0446r_0779 ) * ( 1.0 + s_1411 / r_0779__kms_s_1411r_0779 ) + ( 1.0 + s_0400 / r_0779__kmp_s_0400r_0779 ) * ( 1.0 + s_1430 / r_0779__kmp_s_1430r_0779 ) - 1.0 ) ) / intracellular '

	########### sphingolipid metabolism ###########

	# 3-dehydrosphinganine reductase
	r_0044 = 'intracellular * r_0044__Vmax_r_0044 * ( pow ( 1.0 / r_0044__kms_s_0218r_0044 , 1.0 ) * pow ( 1.0 / r_0044__kms_s_0763_br_0044 , 2.0 ) * pow ( 1.0 / r_0044__kms_s_1096r_0044 , 1.0 ) * ( pow ( s_0218 , 1.0 ) * pow ( s_0763_b , 2.0 ) * pow ( s_1096 , 1.0 ) - pow ( s_1091 , 1.0 ) * pow ( s_1325 , 1.0 ) / r_0044__Keq_r_0044 ) / ( ( 1.0 + s_0218 / r_0044__kms_s_0218r_0044 ) * ( 1.0 + s_0763_b / r_0044__kms_s_0763_br_0044 ) * ( 1.0 + s_1096 / r_0044__kms_s_1096r_0044 ) + ( 1.0 + s_1091 / r_0044__kmp_s_1091r_0044 ) * ( 1.0 + s_1325 / r_0044__kmp_s_1325r_0044 ) - 1.0 ) ) / intracellular '
	# ceramide-1 hydroxylase (24C)
	r_0287 = 'intracellular * r_0287__Vmax_r_0287 * ( pow ( 1.0 / r_0287__kms_s_0763_br_0287 , 1.0 ) * pow ( 1.0 / r_0287__kms_s_1080r_0287 , 1.0 ) * pow ( 1.0 / r_0287__kms_s_1096r_0287 , 1.0 ) * pow ( 1.0 / r_0287__kms_s_1160r_0287 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_1080 , 1.0 ) * pow ( s_1096 , 1.0 ) * pow ( s_1160 , 1.0 ) - pow ( s_1060 , 1.0 ) * pow ( s_1091 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0287__Keq_r_0287 ) / ( ( 1.0 + s_0763_b / r_0287__kms_s_0763_br_0287 ) * ( 1.0 + s_1080 / r_0287__kms_s_1080r_0287 ) * ( 1.0 + s_1096 / r_0287__kms_s_1096r_0287 ) * ( 1.0 + s_1160 / r_0287__kms_s_1160r_0287 ) + ( 1.0 + s_1060 / r_0287__kmp_s_1060r_0287 ) * ( 1.0 + s_1091 / r_0287__kmp_s_1091r_0287 ) * ( 1.0 + s_1434_b / r_0287__kmp_s_1434_br_0287 ) - 1.0 ) ) / intracellular '
	# ceramide-1 synthase (24C)
	r_0290 = 'intracellular * r_0290__Vmax_r_0290 * ( pow ( 1.0 / r_0290__kms_s_1325r_0290 , 1.0 ) * pow ( 1.0 / r_0290__kms_s_1355r_0290 , 1.0 ) * ( pow ( s_1325 , 1.0 ) * pow ( s_1355 , 1.0 ) - pow ( s_0514 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1080 , 1.0 ) / r_0290__Keq_r_0290 ) / ( ( 1.0 + s_1325 / r_0290__kms_s_1325r_0290 ) * ( 1.0 + s_1355 / r_0290__kms_s_1355r_0290 ) + ( 1.0 + s_0514 / r_0290__kmp_s_0514r_0290 ) * ( 1.0 + s_0763_b / r_0290__kmp_s_0763_br_0290 ) * ( 1.0 + s_1080 / r_0290__kmp_s_1080r_0290 ) - 1.0 ) ) / intracellular '
	# inositolphosphotransferase
	r_0618 = 'intracellular * r_0618__Vmax_r_0618 * ( pow ( 1.0 / r_0618__kms_s_0128r_0618 , 1.0 ) * pow ( 1.0 / r_0618__kms_s_1013r_0618 , 1.0 ) * ( pow ( s_0128 , 1.0 ) * pow ( s_1013 , 1.0 ) - pow ( s_0824 , 1.0 ) / r_0618__Keq_r_0618 ) / ( ( 1.0 + s_0128 / r_0618__kms_s_0128r_0618 ) * ( 1.0 + s_1013 / r_0618__kms_s_1013r_0618 ) + 1.0 + s_0824 / r_0618__kmp_s_0824r_0618 - 1.0 ) ) / intracellular '
	# IPC synthase
	r_0621 = 'intracellular * r_0621__Vmax_r_0621 * ( pow ( 1.0 / r_0621__kms_s_0128r_0621 , 1.0 ) * pow ( 1.0 / r_0621__kms_s_1060r_0621 , 1.0 ) * ( pow ( s_0128 , 1.0 ) * pow ( s_1060 , 1.0 ) - pow ( s_0828 , 1.0 ) / r_0621__Keq_r_0621 ) / ( ( 1.0 + s_0128 / r_0621__kms_s_0128r_0621 ) * ( 1.0 + s_1060 / r_0621__kms_s_1060r_0621 ) + 1.0 + s_0828 / r_0621__kmp_s_0828r_0621 - 1.0 ) ) / intracellular '
	# MIPC synthase
	r_0723 = 'intracellular * r_0723__Vmax_r_0723 * ( pow ( 1.0 / r_0723__kms_s_0710r_0723 , 1.0 ) * pow ( 1.0 / r_0723__kms_s_0828r_0723 , 1.0 ) * ( pow ( s_0710 , 1.0 ) * pow ( s_0828 , 1.0 ) - pow ( s_1013 , 1.0 ) / r_0723__Keq_r_0723 ) / ( ( 1.0 + s_0710 / r_0723__kms_s_0710r_0723 ) * ( 1.0 + s_0828 / r_0723__kms_s_0828r_0723 ) + 1.0 + s_1013 / r_0723__kmp_s_1013r_0723 - 1.0 ) ) / intracellular '
	# serine C-palmitoyltransferase
	r_0972 = 'intracellular * r_0972__Vmax_r_0972 * ( pow ( 1.0 / r_0972__kms_s_0943r_0972 , 1.0 ) * pow ( 1.0 / r_0972__kms_s_1187r_0972 , 1.0 ) * ( pow ( s_0943 , 1.0 ) * pow ( s_1187 , 1.0 ) - pow ( s_0218 , 1.0 ) * pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) / r_0972__Keq_r_0972 ) / ( ( 1.0 + s_0943 / r_0972__kms_s_0943r_0972 ) * ( 1.0 + s_1187 / r_0972__kms_s_1187r_0972 ) + ( 1.0 + s_0218 / r_0972__kmp_s_0218r_0972 ) * ( 1.0 + s_0470 / r_0972__kmp_s_0470r_0972 ) * ( 1.0 + s_0514 / r_0972__kmp_s_0514r_0972 ) - 1.0 ) ) / intracellular '

	########### superpathway of TCA cycle and glyoxylate cycle ###########

	# citrate synthase
	r_0328 = 'intracellular * r_0328__Vmax_r_0328 * ( pow ( 1.0 / r_0328__kms_s_0380r_0328 , 1.0 ) * pow ( 1.0 / r_0328__kms_s_1156r_0328 , 1.0 ) * pow ( 1.0 / r_0328__kms_s_1434_br_0328 , 1.0 ) * ( pow ( s_0380 , 1.0 ) * pow ( s_1156 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0507 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0328__Keq_r_0328 ) / ( ( 1.0 + s_0380 / r_0328__kms_s_0380r_0328 ) * ( 1.0 + s_1156 / r_0328__kms_s_1156r_0328 ) * ( 1.0 + s_1434_b / r_0328__kms_s_1434_br_0328 ) + ( 1.0 + s_0507 / r_0328__kmp_s_0507r_0328 ) * ( 1.0 + s_0514 / r_0328__kmp_s_0514r_0328 ) * ( 1.0 + s_0763_b / r_0328__kmp_s_0763_br_0328 ) - 1.0 ) ) / intracellular '
	# isocitrate lyase
	r_0633 = 'intracellular * r_0633__Vmax_r_0633 * ( pow ( 1.0 / r_0633__kms_s_0847r_0633 , 1.0 ) * ( pow ( s_0847 , 1.0 ) - pow ( s_0749 , 1.0 ) * pow ( s_1338 , 1.0 ) / r_0633__Keq_r_0633 ) / ( 1.0 + s_0847 / r_0633__kms_s_0847r_0633 + ( 1.0 + s_0749 / r_0633__kmp_s_0749r_0633 ) * ( 1.0 + s_1338 / r_0633__kmp_s_1338r_0633 ) - 1.0 ) ) / intracellular '
	# malate dehydrogenase
	r_0688 = 'intracellular * r_0688__Vmax_r_0688 * ( pow ( 1.0 / r_0688__kms_s_0763_br_0688 , 1.0 ) * pow ( 1.0 / r_0688__kms_s_1087r_0688 , 1.0 ) * pow ( 1.0 / r_0688__kms_s_1156r_0688 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_1087 , 1.0 ) * pow ( s_1156 , 1.0 ) - pow ( s_0069 , 1.0 ) * pow ( s_1082 , 1.0 ) / r_0688__Keq_r_0688 ) / ( ( 1.0 + s_0763_b / r_0688__kms_s_0763_br_0688 ) * ( 1.0 + s_1087 / r_0688__kms_s_1087r_0688 ) * ( 1.0 + s_1156 / r_0688__kms_s_1156r_0688 ) + ( 1.0 + s_0069 / r_0688__kmp_s_0069r_0688 ) * ( 1.0 + s_1082 / r_0688__kmp_s_1082r_0688 ) - 1.0 ) ) / intracellular '

	########### superpathway of acetoin and butanediol biosynthesis ###########

	# pyruvate decarboxylase
	r_0938 = 'intracellular * r_0938__Vmax_r_0938 * ( pow ( 1.0 / r_0938__kms_s_0763_br_0938 , 1.0 ) * pow ( 1.0 / r_0938__kms_s_1277r_0938 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_1277 , 1.0 ) - pow ( s_0366 , 1.0 ) * pow ( s_0470 , 1.0 ) / r_0938__Keq_r_0938 ) / ( ( 1.0 + s_0763_b / r_0938__kms_s_0763_br_0938 ) * ( 1.0 + s_1277 / r_0938__kms_s_1277r_0938 ) + ( 1.0 + s_0366 / r_0938__kmp_s_0366r_0938 ) * ( 1.0 + s_0470 / r_0938__kmp_s_0470r_0938 ) - 1.0 ) ) / intracellular '

	########### superpathway of fatty acid biosynthesis, saturated ###########

	# acetyl-Coa carboxylase
	r_0123 = 'intracellular * r_0123__Vmax_r_0123 * ( pow ( 1.0 / r_0123__kms_s_0380r_0123 , 1.0 ) * pow ( 1.0 / r_0123__kms_s_0446r_0123 , 1.0 ) * pow ( 1.0 / r_0123__kms_s_0458r_0123 , 1.0 ) * ( pow ( s_0380 , 1.0 ) * pow ( s_0446 , 1.0 ) * pow ( s_0458 , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0123__Keq_r_0123 ) / ( ( 1.0 + s_0380 / r_0123__kms_s_0380r_0123 ) * ( 1.0 + s_0446 / r_0123__kms_s_0446r_0123 ) * ( 1.0 + s_0458 / r_0123__kms_s_0458r_0123 ) + ( 1.0 + s_0400 / r_0123__kmp_s_0400r_0123 ) * ( 1.0 + s_0763_b / r_0123__kmp_s_0763_br_0123 ) * ( 1.0 + s_1005 / r_0123__kmp_s_1005r_0123 ) * ( 1.0 + s_1207 / r_0123__kmp_s_1207r_0123 ) - 1.0 ) ) / intracellular '
	# fatty acid synthase (n-C10:0)
	r_0417 = 'intracellular * r_0417__Vmax_r_0417 * ( pow ( 1.0 / r_0417__kms_s_0763_br_0417 , 3.0 ) * pow ( 1.0 / r_0417__kms_s_1005r_0417 , 1.0 ) * pow ( 1.0 / r_0417__kms_s_1096r_0417 , 2.0 ) * pow ( 1.0 / r_0417__kms_s_1132r_0417 , 1.0 ) * ( pow ( s_0763_b , 3.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1096 , 2.0 ) * pow ( s_1132 , 1.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_0574 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1434_b , 1.0 ) / r_0417__Keq_r_0417 ) / ( ( 1.0 + s_0763_b / r_0417__kms_s_0763_br_0417 ) * ( 1.0 + s_1005 / r_0417__kms_s_1005r_0417 ) * ( 1.0 + s_1096 / r_0417__kms_s_1096r_0417 ) * ( 1.0 + s_1132 / r_0417__kms_s_1132r_0417 ) + ( 1.0 + s_0470 / r_0417__kmp_s_0470r_0417 ) * ( 1.0 + s_0514 / r_0417__kmp_s_0514r_0417 ) * ( 1.0 + s_0574 / r_0417__kmp_s_0574r_0417 ) * ( 1.0 + s_1091 / r_0417__kmp_s_1091r_0417 ) * ( 1.0 + s_1434_b / r_0417__kmp_s_1434_br_0417 ) - 1.0 ) ) / intracellular '
	# fatty acid synthase (n-C12:0)
	r_0418 = 'intracellular * r_0418__Vmax_r_0418 * ( pow ( 1.0 / r_0418__kms_s_0574r_0418 , 1.0 ) * pow ( 1.0 / r_0418__kms_s_0763_br_0418 , 3.0 ) * pow ( 1.0 / r_0418__kms_s_1005r_0418 , 1.0 ) * pow ( 1.0 / r_0418__kms_s_1096r_0418 , 2.0 ) * ( pow ( s_0574 , 1.0 ) * pow ( s_0763_b , 3.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1096 , 2.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_0968 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1434_b , 1.0 ) / r_0418__Keq_r_0418 ) / ( ( 1.0 + s_0574 / r_0418__kms_s_0574r_0418 ) * ( 1.0 + s_0763_b / r_0418__kms_s_0763_br_0418 ) * ( 1.0 + s_1005 / r_0418__kms_s_1005r_0418 ) * ( 1.0 + s_1096 / r_0418__kms_s_1096r_0418 ) + ( 1.0 + s_0470 / r_0418__kmp_s_0470r_0418 ) * ( 1.0 + s_0514 / r_0418__kmp_s_0514r_0418 ) * ( 1.0 + s_0968 / r_0418__kmp_s_0968r_0418 ) * ( 1.0 + s_1091 / r_0418__kmp_s_1091r_0418 ) * ( 1.0 + s_1434_b / r_0418__kmp_s_1434_br_0418 ) - 1.0 ) ) / intracellular '
	# fatty acid synthase (n-C14:0)
	r_0419 = 'intracellular * r_0419__Vmax_r_0419 * ( pow ( 1.0 / r_0419__kms_s_0763_br_0419 , 3.0 ) * pow ( 1.0 / r_0419__kms_s_0968r_0419 , 1.0 ) * pow ( 1.0 / r_0419__kms_s_1005r_0419 , 1.0 ) * pow ( 1.0 / r_0419__kms_s_1096r_0419 , 2.0 ) * ( pow ( s_0763_b , 3.0 ) * pow ( s_0968 , 1.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1096 , 2.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_1028 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1434_b , 1.0 ) / r_0419__Keq_r_0419 ) / ( ( 1.0 + s_0763_b / r_0419__kms_s_0763_br_0419 ) * ( 1.0 + s_0968 / r_0419__kms_s_0968r_0419 ) * ( 1.0 + s_1005 / r_0419__kms_s_1005r_0419 ) * ( 1.0 + s_1096 / r_0419__kms_s_1096r_0419 ) + ( 1.0 + s_0470 / r_0419__kmp_s_0470r_0419 ) * ( 1.0 + s_0514 / r_0419__kmp_s_0514r_0419 ) * ( 1.0 + s_1028 / r_0419__kmp_s_1028r_0419 ) * ( 1.0 + s_1091 / r_0419__kmp_s_1091r_0419 ) * ( 1.0 + s_1434_b / r_0419__kmp_s_1434_br_0419 ) - 1.0 ) ) / intracellular '
	# fatty acid synthase (n-C16:0)
	r_0421 = 'intracellular * r_0421__Vmax_r_0421 * ( pow ( 1.0 / r_0421__kms_s_0763_br_0421 , 3.0 ) * pow ( 1.0 / r_0421__kms_s_1005r_0421 , 1.0 ) * pow ( 1.0 / r_0421__kms_s_1028r_0421 , 1.0 ) * pow ( 1.0 / r_0421__kms_s_1096r_0421 , 2.0 ) * ( pow ( s_0763_b , 3.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1028 , 1.0 ) * pow ( s_1096 , 2.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1170 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0421__Keq_r_0421 ) / ( ( 1.0 + s_0763_b / r_0421__kms_s_0763_br_0421 ) * ( 1.0 + s_1005 / r_0421__kms_s_1005r_0421 ) * ( 1.0 + s_1028 / r_0421__kms_s_1028r_0421 ) * ( 1.0 + s_1096 / r_0421__kms_s_1096r_0421 ) + ( 1.0 + s_0470 / r_0421__kmp_s_0470r_0421 ) * ( 1.0 + s_0514 / r_0421__kmp_s_0514r_0421 ) * ( 1.0 + s_1091 / r_0421__kmp_s_1091r_0421 ) * ( 1.0 + s_1170 / r_0421__kmp_s_1170r_0421 ) * ( 1.0 + s_1434_b / r_0421__kmp_s_1434_br_0421 ) - 1.0 ) ) / intracellular '
	# fatty acid synthase (n-C18:0)
	r_0423 = 'intracellular * r_0423__Vmax_r_0423 * ( pow ( 1.0 / r_0423__kms_s_0763_br_0423 , 3.0 ) * pow ( 1.0 / r_0423__kms_s_1005r_0423 , 1.0 ) * pow ( 1.0 / r_0423__kms_s_1096r_0423 , 2.0 ) * pow ( 1.0 / r_0423__kms_s_1170r_0423 , 1.0 ) * ( pow ( s_0763_b , 3.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1096 , 2.0 ) * pow ( s_1170 , 1.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1329 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0423__Keq_r_0423 ) / ( ( 1.0 + s_0763_b / r_0423__kms_s_0763_br_0423 ) * ( 1.0 + s_1005 / r_0423__kms_s_1005r_0423 ) * ( 1.0 + s_1096 / r_0423__kms_s_1096r_0423 ) * ( 1.0 + s_1170 / r_0423__kms_s_1170r_0423 ) + ( 1.0 + s_0470 / r_0423__kmp_s_0470r_0423 ) * ( 1.0 + s_0514 / r_0423__kmp_s_0514r_0423 ) * ( 1.0 + s_1091 / r_0423__kmp_s_1091r_0423 ) * ( 1.0 + s_1329 / r_0423__kmp_s_1329r_0423 ) * ( 1.0 + s_1434_b / r_0423__kmp_s_1434_br_0423 ) - 1.0 ) ) / intracellular '
	# fatty acyl-CoA synthase (n-C10:0CoA)
	r_0429 = 'intracellular * r_0429__Vmax_r_0429 * ( pow ( 1.0 / r_0429__kms_s_0763_br_0429 , 3.0 ) * pow ( 1.0 / r_0429__kms_s_1005r_0429 , 1.0 ) * pow ( 1.0 / r_0429__kms_s_1096r_0429 , 2.0 ) * pow ( 1.0 / r_0429__kms_s_1140r_0429 , 1.0 ) * ( pow ( s_0763_b , 3.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1096 , 2.0 ) * pow ( s_1140 , 1.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_0582 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1434_b , 1.0 ) / r_0429__Keq_r_0429 ) / ( ( 1.0 + s_0763_b / r_0429__kms_s_0763_br_0429 ) * ( 1.0 + s_1005 / r_0429__kms_s_1005r_0429 ) * ( 1.0 + s_1096 / r_0429__kms_s_1096r_0429 ) * ( 1.0 + s_1140 / r_0429__kms_s_1140r_0429 ) + ( 1.0 + s_0470 / r_0429__kmp_s_0470r_0429 ) * ( 1.0 + s_0514 / r_0429__kmp_s_0514r_0429 ) * ( 1.0 + s_0582 / r_0429__kmp_s_0582r_0429 ) * ( 1.0 + s_1091 / r_0429__kmp_s_1091r_0429 ) * ( 1.0 + s_1434_b / r_0429__kmp_s_1434_br_0429 ) - 1.0 ) ) / intracellular '
	# fatty acyl-CoA synthase (n-C8:0CoA), lumped reaction
	r_0430 = 'intracellular * r_0430__Vmax_r_0430 * ( pow ( 1.0 / r_0430__kms_s_0380r_0430 , 1.0 ) * pow ( 1.0 / r_0430__kms_s_0763_br_0430 , 9.0 ) * pow ( 1.0 / r_0430__kms_s_1005r_0430 , 3.0 ) * pow ( 1.0 / r_0430__kms_s_1096r_0430 , 6.0 ) * ( pow ( s_0380 , 1.0 ) * pow ( s_0763_b , 9.0 ) * pow ( s_1005 , 3.0 ) * pow ( s_1096 , 6.0 ) - pow ( s_0470 , 3.0 ) * pow ( s_0514 , 3.0 ) * pow ( s_1091 , 6.0 ) * pow ( s_1140 , 1.0 ) * pow ( s_1434_b , 3.0 ) / r_0430__Keq_r_0430 ) / ( ( 1.0 + s_0380 / r_0430__kms_s_0380r_0430 ) * ( 1.0 + s_0763_b / r_0430__kms_s_0763_br_0430 ) * ( 1.0 + s_1005 / r_0430__kms_s_1005r_0430 ) * ( 1.0 + s_1096 / r_0430__kms_s_1096r_0430 ) + ( 1.0 + s_0470 / r_0430__kmp_s_0470r_0430 ) * ( 1.0 + s_0514 / r_0430__kmp_s_0514r_0430 ) * ( 1.0 + s_1091 / r_0430__kmp_s_1091r_0430 ) * ( 1.0 + s_1140 / r_0430__kmp_s_1140r_0430 ) * ( 1.0 + s_1434_b / r_0430__kmp_s_1434_br_0430 ) - 1.0 ) ) / intracellular '
	# fatty-acyl-CoA synthase (n-C12:0CoA)
	r_0464 = 'intracellular * r_0464__Vmax_r_0464 * ( pow ( 1.0 / r_0464__kms_s_0582r_0464 , 1.0 ) * pow ( 1.0 / r_0464__kms_s_0763_br_0464 , 3.0 ) * pow ( 1.0 / r_0464__kms_s_1005r_0464 , 1.0 ) * pow ( 1.0 / r_0464__kms_s_1096r_0464 , 2.0 ) * ( pow ( s_0582 , 1.0 ) * pow ( s_0763_b , 3.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1096 , 2.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_0977 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1434_b , 1.0 ) / r_0464__Keq_r_0464 ) / ( ( 1.0 + s_0582 / r_0464__kms_s_0582r_0464 ) * ( 1.0 + s_0763_b / r_0464__kms_s_0763_br_0464 ) * ( 1.0 + s_1005 / r_0464__kms_s_1005r_0464 ) * ( 1.0 + s_1096 / r_0464__kms_s_1096r_0464 ) + ( 1.0 + s_0470 / r_0464__kmp_s_0470r_0464 ) * ( 1.0 + s_0514 / r_0464__kmp_s_0514r_0464 ) * ( 1.0 + s_0977 / r_0464__kmp_s_0977r_0464 ) * ( 1.0 + s_1091 / r_0464__kmp_s_1091r_0464 ) * ( 1.0 + s_1434_b / r_0464__kmp_s_1434_br_0464 ) - 1.0 ) ) / intracellular '
	# fatty-acyl-CoA synthase (n-C14:0CoA)
	r_0465 = 'intracellular * r_0465__Vmax_r_0465 * ( pow ( 1.0 / r_0465__kms_s_0763_br_0465 , 3.0 ) * pow ( 1.0 / r_0465__kms_s_0977r_0465 , 1.0 ) * pow ( 1.0 / r_0465__kms_s_1005r_0465 , 1.0 ) * pow ( 1.0 / r_0465__kms_s_1096r_0465 , 2.0 ) * ( pow ( s_0763_b , 3.0 ) * pow ( s_0977 , 1.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1096 , 2.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_1044 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1434_b , 1.0 ) / r_0465__Keq_r_0465 ) / ( ( 1.0 + s_0763_b / r_0465__kms_s_0763_br_0465 ) * ( 1.0 + s_0977 / r_0465__kms_s_0977r_0465 ) * ( 1.0 + s_1005 / r_0465__kms_s_1005r_0465 ) * ( 1.0 + s_1096 / r_0465__kms_s_1096r_0465 ) + ( 1.0 + s_0470 / r_0465__kmp_s_0470r_0465 ) * ( 1.0 + s_0514 / r_0465__kmp_s_0514r_0465 ) * ( 1.0 + s_1044 / r_0465__kmp_s_1044r_0465 ) * ( 1.0 + s_1091 / r_0465__kmp_s_1091r_0465 ) * ( 1.0 + s_1434_b / r_0465__kmp_s_1434_br_0465 ) - 1.0 ) ) / intracellular '
	# fatty-acyl-CoA synthase (n-C16:0CoA)
	r_0466 = 'intracellular * r_0466__Vmax_r_0466 * ( pow ( 1.0 / r_0466__kms_s_0763_br_0466 , 3.0 ) * pow ( 1.0 / r_0466__kms_s_1005r_0466 , 1.0 ) * pow ( 1.0 / r_0466__kms_s_1044r_0466 , 1.0 ) * pow ( 1.0 / r_0466__kms_s_1096r_0466 , 2.0 ) * ( pow ( s_0763_b , 3.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1044 , 1.0 ) * pow ( s_1096 , 2.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1187 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0466__Keq_r_0466 ) / ( ( 1.0 + s_0763_b / r_0466__kms_s_0763_br_0466 ) * ( 1.0 + s_1005 / r_0466__kms_s_1005r_0466 ) * ( 1.0 + s_1044 / r_0466__kms_s_1044r_0466 ) * ( 1.0 + s_1096 / r_0466__kms_s_1096r_0466 ) + ( 1.0 + s_0470 / r_0466__kmp_s_0470r_0466 ) * ( 1.0 + s_0514 / r_0466__kmp_s_0514r_0466 ) * ( 1.0 + s_1091 / r_0466__kmp_s_1091r_0466 ) * ( 1.0 + s_1187 / r_0466__kmp_s_1187r_0466 ) * ( 1.0 + s_1434_b / r_0466__kmp_s_1434_br_0466 ) - 1.0 ) ) / intracellular '
	# fatty-acyl-CoA synthase (n-C18:0CoA)
	r_0467 = 'intracellular * r_0467__Vmax_r_0467 * ( pow ( 1.0 / r_0467__kms_s_0763_br_0467 , 3.0 ) * pow ( 1.0 / r_0467__kms_s_1005r_0467 , 1.0 ) * pow ( 1.0 / r_0467__kms_s_1096r_0467 , 2.0 ) * pow ( 1.0 / r_0467__kms_s_1187r_0467 , 1.0 ) * ( pow ( s_0763_b , 3.0 ) * pow ( s_1005 , 1.0 ) * pow ( s_1096 , 2.0 ) * pow ( s_1187 , 1.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_1091 , 2.0 ) * pow ( s_1334 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0467__Keq_r_0467 ) / ( ( 1.0 + s_0763_b / r_0467__kms_s_0763_br_0467 ) * ( 1.0 + s_1005 / r_0467__kms_s_1005r_0467 ) * ( 1.0 + s_1096 / r_0467__kms_s_1096r_0467 ) * ( 1.0 + s_1187 / r_0467__kms_s_1187r_0467 ) + ( 1.0 + s_0470 / r_0467__kmp_s_0470r_0467 ) * ( 1.0 + s_0514 / r_0467__kmp_s_0514r_0467 ) * ( 1.0 + s_1091 / r_0467__kmp_s_1091r_0467 ) * ( 1.0 + s_1334 / r_0467__kmp_s_1334r_0467 ) * ( 1.0 + s_1434_b / r_0467__kmp_s_1434_br_0467 ) - 1.0 ) ) / intracellular '

	########### superpathway of glutamate biosynthesis ###########

	# glutamate dehydrogenase (NADP)
	r_0509 = 'intracellular * r_0509__Vmax_r_0509 * ( pow ( 1.0 / r_0509__kms_s_0185r_0509 , 1.0 ) * pow ( 1.0 / r_0509__kms_s_0430r_0509 , 1.0 ) * pow ( 1.0 / r_0509__kms_s_0763_br_0509 , 1.0 ) * pow ( 1.0 / r_0509__kms_s_1096r_0509 , 1.0 ) * ( pow ( s_0185 , 1.0 ) * pow ( s_0430 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) - pow ( s_0899 , 1.0 ) * pow ( s_1091 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0509__Keq_r_0509 ) / ( ( 1.0 + s_0185 / r_0509__kms_s_0185r_0509 ) * ( 1.0 + s_0430 / r_0509__kms_s_0430r_0509 ) * ( 1.0 + s_0763_b / r_0509__kms_s_0763_br_0509 ) * ( 1.0 + s_1096 / r_0509__kms_s_1096r_0509 ) + ( 1.0 + s_0899 / r_0509__kmp_s_0899r_0509 ) * ( 1.0 + s_1091 / r_0509__kmp_s_1091r_0509 ) * ( 1.0 + s_1434_b / r_0509__kmp_s_1434_br_0509 ) - 1.0 ) ) / intracellular '
	# glutamate synthase (NADH2)
	r_0510 = 'intracellular * r_0510__Vmax_r_0510 * ( pow ( 1.0 / r_0510__kms_s_0185r_0510 , 1.0 ) * pow ( 1.0 / r_0510__kms_s_0763_br_0510 , 1.0 ) * pow ( 1.0 / r_0510__kms_s_0907r_0510 , 1.0 ) * pow ( 1.0 / r_0510__kms_s_1087r_0510 , 1.0 ) * ( pow ( s_0185 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_0907 , 1.0 ) * pow ( s_1087 , 1.0 ) - pow ( s_0899 , 2.0 ) * pow ( s_1082 , 1.0 ) / r_0510__Keq_r_0510 ) / ( ( 1.0 + s_0185 / r_0510__kms_s_0185r_0510 ) * ( 1.0 + s_0763_b / r_0510__kms_s_0763_br_0510 ) * ( 1.0 + s_0907 / r_0510__kms_s_0907r_0510 ) * ( 1.0 + s_1087 / r_0510__kms_s_1087r_0510 ) + ( 1.0 + s_0899 / r_0510__kmp_s_0899r_0510 ) * ( 1.0 + s_1082 / r_0510__kmp_s_1082r_0510 ) - 1.0 ) ) / intracellular '
	# glutamine synthetase
	r_0515 = 'intracellular * r_0515__Vmax_r_0515 * ( pow ( 1.0 / r_0515__kms_s_0430r_0515 , 1.0 ) * pow ( 1.0 / r_0515__kms_s_0446r_0515 , 1.0 ) * pow ( 1.0 / r_0515__kms_s_0899r_0515 , 1.0 ) * ( pow ( s_0430 , 1.0 ) * pow ( s_0446 , 1.0 ) * pow ( s_0899 , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_0907 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0515__Keq_r_0515 ) / ( ( 1.0 + s_0430 / r_0515__kms_s_0430r_0515 ) * ( 1.0 + s_0446 / r_0515__kms_s_0446r_0515 ) * ( 1.0 + s_0899 / r_0515__kms_s_0899r_0515 ) + ( 1.0 + s_0400 / r_0515__kmp_s_0400r_0515 ) * ( 1.0 + s_0763_b / r_0515__kmp_s_0763_br_0515 ) * ( 1.0 + s_0907 / r_0515__kmp_s_0907r_0515 ) * ( 1.0 + s_1207 / r_0515__kmp_s_1207r_0515 ) - 1.0 ) ) / intracellular '
	# isocitrate dehydrogenase (NADP)
	r_0630 = 'intracellular * r_0630__Vmax_r_0630 * ( pow ( 1.0 / r_0630__kms_s_0847r_0630 , 1.0 ) * pow ( 1.0 / r_0630__kms_s_1091r_0630 , 1.0 ) * ( pow ( s_0847 , 1.0 ) * pow ( s_1091 , 1.0 ) - pow ( s_0185 , 1.0 ) * pow ( s_0470 , 1.0 ) * pow ( s_1096 , 1.0 ) / r_0630__Keq_r_0630 ) / ( ( 1.0 + s_0847 / r_0630__kms_s_0847r_0630 ) * ( 1.0 + s_1091 / r_0630__kms_s_1091r_0630 ) + ( 1.0 + s_0185 / r_0630__kmp_s_0185r_0630 ) * ( 1.0 + s_0470 / r_0630__kmp_s_0470r_0630 ) * ( 1.0 + s_1096 / r_0630__kmp_s_1096r_0630 ) - 1.0 ) ) / intracellular '

	########### superpathway of histidine, purine, and pyrimidine biosynthesis ###########

	# 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino)imidazole-4-carboxamide isomerase
	r_0008 = 'intracellular * r_0008__Vmax_r_0008 * ( pow ( 1.0 / r_0008__kms_s_0079r_0008 , 1.0 ) * ( pow ( s_0079 , 1.0 ) - pow ( s_0315 , 1.0 ) / r_0008__Keq_r_0008 ) / ( 1.0 + s_0079 / r_0008__kms_s_0079r_0008 + 1.0 + s_0315 / r_0008__kmp_s_0315r_0008 - 1.0 ) ) / intracellular '
	# ATP phosphoribosyltransferase
	r_0245 = 'intracellular * r_0245__Vmax_r_0245 * ( pow ( 1.0 / r_0245__kms_s_0331r_0245 , 1.0 ) * pow ( 1.0 / r_0245__kms_s_0446r_0245 , 1.0 ) * ( pow ( s_0331 , 1.0 ) * pow ( s_0446 , 1.0 ) - pow ( s_0334 , 1.0 ) * pow ( s_0605 , 1.0 ) / r_0245__Keq_r_0245 ) / ( ( 1.0 + s_0331 / r_0245__kms_s_0331r_0245 ) * ( 1.0 + s_0446 / r_0245__kms_s_0446r_0245 ) + ( 1.0 + s_0334 / r_0245__kmp_s_0334r_0245 ) * ( 1.0 + s_0605 / r_0245__kmp_s_0605r_0245 ) - 1.0 ) ) / intracellular '
	# GMP synthase
	r_0551 = 'intracellular * r_0551__Vmax_r_0551 * ( pow ( 1.0 / r_0551__kms_s_0306r_0551 , 1.0 ) * pow ( 1.0 / r_0551__kms_s_0446r_0551 , 1.0 ) * pow ( 1.0 / r_0551__kms_s_0907r_0551 , 1.0 ) * pow ( 1.0 / r_0551__kms_s_1434_br_0551 , 1.0 ) * ( pow ( s_0306 , 1.0 ) * pow ( s_0446 , 1.0 ) * pow ( s_0907 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0434 , 1.0 ) * pow ( s_0605 , 1.0 ) * pow ( s_0752 , 1.0 ) * pow ( s_0763_b , 2.0 ) * pow ( s_0899 , 1.0 ) / r_0551__Keq_r_0551 ) / ( ( 1.0 + s_0306 / r_0551__kms_s_0306r_0551 ) * ( 1.0 + s_0446 / r_0551__kms_s_0446r_0551 ) * ( 1.0 + s_0907 / r_0551__kms_s_0907r_0551 ) * ( 1.0 + s_1434_b / r_0551__kms_s_1434_br_0551 ) + ( 1.0 + s_0434 / r_0551__kmp_s_0434r_0551 ) * ( 1.0 + s_0605 / r_0551__kmp_s_0605r_0551 ) * ( 1.0 + s_0752 / r_0551__kmp_s_0752r_0551 ) * ( 1.0 + s_0763_b / r_0551__kmp_s_0763_br_0551 ) * ( 1.0 + s_0899 / r_0551__kmp_s_0899r_0551 ) - 1.0 ) ) / intracellular '
	# histidinol dehydrogenase
	r_0575 = 'intracellular * r_0575__Vmax_r_0575 * ( pow ( 1.0 / r_0575__kms_s_0915r_0575 , 1.0 ) * pow ( 1.0 / r_0575__kms_s_1082r_0575 , 2.0 ) * pow ( 1.0 / r_0575__kms_s_1434_br_0575 , 1.0 ) * ( pow ( s_0915 , 1.0 ) * pow ( s_1082 , 2.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0763_b , 3.0 ) * pow ( s_0911 , 1.0 ) * pow ( s_1087 , 2.0 ) / r_0575__Keq_r_0575 ) / ( ( 1.0 + s_0915 / r_0575__kms_s_0915r_0575 ) * ( 1.0 + s_1082 / r_0575__kms_s_1082r_0575 ) * ( 1.0 + s_1434_b / r_0575__kms_s_1434_br_0575 ) + ( 1.0 + s_0763_b / r_0575__kmp_s_0763_br_0575 ) * ( 1.0 + s_0911 / r_0575__kmp_s_0911r_0575 ) * ( 1.0 + s_1087 / r_0575__kmp_s_1087r_0575 ) - 1.0 ) ) / intracellular '
	# histidinol-phosphatase
	r_0576 = 'intracellular * r_0576__Vmax_r_0576 * ( pow ( 1.0 / r_0576__kms_s_0916r_0576 , 1.0 ) * pow ( 1.0 / r_0576__kms_s_1434_br_0576 , 1.0 ) * ( pow ( s_0916 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0915 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0576__Keq_r_0576 ) / ( ( 1.0 + s_0916 / r_0576__kms_s_0916r_0576 ) * ( 1.0 + s_1434_b / r_0576__kms_s_1434_br_0576 ) + ( 1.0 + s_0915 / r_0576__kmp_s_0915r_0576 ) * ( 1.0 + s_1207 / r_0576__kmp_s_1207r_0576 ) - 1.0 ) ) / intracellular '
	# histidinol-phosphate transaminase
	r_0577 = 'intracellular * r_0577__Vmax_r_0577 * ( pow ( 1.0 / r_0577__kms_s_0212r_0577 , 1.0 ) * pow ( 1.0 / r_0577__kms_s_0899r_0577 , 1.0 ) * ( pow ( s_0212 , 1.0 ) * pow ( s_0899 , 1.0 ) - pow ( s_0185 , 1.0 ) * pow ( s_0916 , 1.0 ) / r_0577__Keq_r_0577 ) / ( ( 1.0 + s_0212 / r_0577__kms_s_0212r_0577 ) * ( 1.0 + s_0899 / r_0577__kms_s_0899r_0577 ) + ( 1.0 + s_0185 / r_0577__kmp_s_0185r_0577 ) * ( 1.0 + s_0916 / r_0577__kmp_s_0916r_0577 ) - 1.0 ) ) / intracellular '
	# Imidazole-glycerol-3-phosphate synthase
	r_0604 = 'intracellular * r_0604__Vmax_r_0604 * ( pow ( 1.0 / r_0604__kms_s_0315r_0604 , 1.0 ) * pow ( 1.0 / r_0604__kms_s_0907r_0604 , 1.0 ) * ( pow ( s_0315 , 1.0 ) * pow ( s_0907 , 1.0 ) - pow ( s_0317 , 1.0 ) * pow ( s_0532 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_0899 , 1.0 ) / r_0604__Keq_r_0604 ) / ( ( 1.0 + s_0315 / r_0604__kms_s_0315r_0604 ) * ( 1.0 + s_0907 / r_0604__kms_s_0907r_0604 ) + ( 1.0 + s_0317 / r_0604__kmp_s_0317r_0604 ) * ( 1.0 + s_0532 / r_0604__kmp_s_0532r_0604 ) * ( 1.0 + s_0763_b / r_0604__kmp_s_0763_br_0604 ) * ( 1.0 + s_0899 / r_0604__kmp_s_0899r_0604 ) - 1.0 ) ) / intracellular '
	# imidazoleglycerol-phosphate dehydratase
	r_0605 = 'intracellular * r_0605__Vmax_r_0605 * ( pow ( 1.0 / r_0605__kms_s_0532r_0605 , 1.0 ) * ( pow ( s_0532 , 1.0 ) - pow ( s_0212 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0605__Keq_r_0605 ) / ( 1.0 + s_0532 / r_0605__kms_s_0532r_0605 + ( 1.0 + s_0212 / r_0605__kmp_s_0212r_0605 ) * ( 1.0 + s_1434_b / r_0605__kmp_s_1434_br_0605 ) - 1.0 ) ) / intracellular '
	# phosphoribosyl-AMP cyclohydrolase
	r_0881 = 'intracellular * r_0881__Vmax_r_0881 * ( pow ( 1.0 / r_0881__kms_s_0080r_0881 , 1.0 ) * pow ( 1.0 / r_0881__kms_s_1434_br_0881 , 1.0 ) * ( pow ( s_0080 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0079 , 1.0 ) / r_0881__Keq_r_0881 ) / ( ( 1.0 + s_0080 / r_0881__kms_s_0080r_0881 ) * ( 1.0 + s_1434_b / r_0881__kms_s_1434_br_0881 ) + 1.0 + s_0079 / r_0881__kmp_s_0079r_0881 - 1.0 ) ) / intracellular '
	# phosphoribosyl-ATP pyrophosphatase
	r_0882 = 'intracellular * r_0882__Vmax_r_0882 * ( pow ( 1.0 / r_0882__kms_s_0334r_0882 , 1.0 ) * pow ( 1.0 / r_0882__kms_s_1434_br_0882 , 1.0 ) * ( pow ( s_0334 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0080 , 1.0 ) * pow ( s_0605 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0882__Keq_r_0882 ) / ( ( 1.0 + s_0334 / r_0882__kms_s_0334r_0882 ) * ( 1.0 + s_1434_b / r_0882__kms_s_1434_br_0882 ) + ( 1.0 + s_0080 / r_0882__kmp_s_0080r_0882 ) * ( 1.0 + s_0605 / r_0882__kmp_s_0605r_0882 ) * ( 1.0 + s_0763_b / r_0882__kmp_s_0763_br_0882 ) - 1.0 ) ) / intracellular '
	# phosphoribosylpyrophosphate synthetase
	r_0891 = 'intracellular * r_0891__Vmax_r_0891 * ( pow ( 1.0 / r_0891__kms_s_0427r_0891 , 1.0 ) * pow ( 1.0 / r_0891__kms_s_0446r_0891 , 1.0 ) * ( pow ( s_0427 , 1.0 ) * pow ( s_0446 , 1.0 ) - pow ( s_0331 , 1.0 ) * pow ( s_0434 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0891__Keq_r_0891 ) / ( ( 1.0 + s_0427 / r_0891__kms_s_0427r_0891 ) * ( 1.0 + s_0446 / r_0891__kms_s_0446r_0891 ) + ( 1.0 + s_0331 / r_0891__kmp_s_0331r_0891 ) * ( 1.0 + s_0434 / r_0891__kmp_s_0434r_0891 ) * ( 1.0 + s_0763_b / r_0891__kmp_s_0763_br_0891 ) - 1.0 ) ) / intracellular '

	########### superpathway of phenylalanine, tyrosine and tryptophan biosynthesis ###########

	# 2-deoxy-D-arabino-heptulosonate 7-phosphate synthetase
	r_0021 = 'intracellular * r_0021__Vmax_r_0021 * ( pow ( 1.0 / r_0021__kms_s_0533r_0021 , 1.0 ) * pow ( 1.0 / r_0021__kms_s_1243r_0021 , 1.0 ) * pow ( 1.0 / r_0021__kms_s_1434_br_0021 , 1.0 ) * ( pow ( s_0533 , 1.0 ) * pow ( s_1243 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0356 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0021__Keq_r_0021 ) / ( ( 1.0 + s_0533 / r_0021__kms_s_0533r_0021 ) * ( 1.0 + s_1243 / r_0021__kms_s_1243r_0021 ) * ( 1.0 + s_1434_b / r_0021__kms_s_1434_br_0021 ) + ( 1.0 + s_0356 / r_0021__kmp_s_0356r_0021 ) * ( 1.0 + s_1207 / r_0021__kmp_s_1207r_0021 ) - 1.0 ) ) / intracellular '
	# 3-dehydroquinate dehydratase
	r_0042 = 'intracellular * r_0042__Vmax_r_0042 * ( pow ( 1.0 / r_0042__kms_s_0216r_0042 , 1.0 ) * ( pow ( s_0216 , 1.0 ) - pow ( s_0217 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0042__Keq_r_0042 ) / ( 1.0 + s_0216 / r_0042__kms_s_0216r_0042 + ( 1.0 + s_0217 / r_0042__kmp_s_0217r_0042 ) * ( 1.0 + s_1434_b / r_0042__kmp_s_1434_br_0042 ) - 1.0 ) ) / intracellular '
	# 3-dehydroquinate synthase
	r_0043 = 'intracellular * r_0043__Vmax_r_0043 * ( pow ( 1.0 / r_0043__kms_s_0356r_0043 , 1.0 ) * ( pow ( s_0356 , 1.0 ) - pow ( s_0216 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0043__Keq_r_0043 ) / ( 1.0 + s_0356 / r_0043__kms_s_0356r_0043 + ( 1.0 + s_0216 / r_0043__kmp_s_0216r_0043 ) * ( 1.0 + s_1207 / r_0043__kmp_s_1207r_0043 ) - 1.0 ) ) / intracellular '
	# 3-phosphoshikimate 1-carboxyvinyltransferase
	r_0068 = 'intracellular * r_0068__Vmax_r_0068 * ( pow ( 1.0 / r_0068__kms_s_0267r_0068 , 1.0 ) * pow ( 1.0 / r_0068__kms_s_1243r_0068 , 1.0 ) * ( pow ( s_0267 , 1.0 ) * pow ( s_1243 , 1.0 ) - pow ( s_0330 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0068__Keq_r_0068 ) / ( ( 1.0 + s_0267 / r_0068__kms_s_0267r_0068 ) * ( 1.0 + s_1243 / r_0068__kms_s_1243r_0068 ) + ( 1.0 + s_0330 / r_0068__kmp_s_0330r_0068 ) * ( 1.0 + s_1207 / r_0068__kmp_s_1207r_0068 ) - 1.0 ) ) / intracellular '
	# chorismate synthase
	r_0306 = 'intracellular * r_0306__Vmax_r_0306 * ( pow ( 1.0 / r_0306__kms_s_0330r_0306 , 1.0 ) * ( pow ( s_0330 , 1.0 ) - pow ( s_0500 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0306__Keq_r_0306 ) / ( 1.0 + s_0330 / r_0306__kms_s_0330r_0306 + ( 1.0 + s_0500 / r_0306__kmp_s_0500r_0306 ) * ( 1.0 + s_1207 / r_0306__kmp_s_1207r_0306 ) - 1.0 ) ) / intracellular '
	# shikimate dehydrogenase
	r_0976 = 'intracellular * r_0976__Vmax_r_0976 * ( pow ( 1.0 / r_0976__kms_s_0217r_0976 , 1.0 ) * pow ( 1.0 / r_0976__kms_s_0763_br_0976 , 1.0 ) * pow ( 1.0 / r_0976__kms_s_1096r_0976 , 1.0 ) * ( pow ( s_0217 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) - pow ( s_1091 , 1.0 ) * pow ( s_1306 , 1.0 ) / r_0976__Keq_r_0976 ) / ( ( 1.0 + s_0217 / r_0976__kms_s_0217r_0976 ) * ( 1.0 + s_0763_b / r_0976__kms_s_0763_br_0976 ) * ( 1.0 + s_1096 / r_0976__kms_s_1096r_0976 ) + ( 1.0 + s_1091 / r_0976__kmp_s_1091r_0976 ) * ( 1.0 + s_1306 / r_0976__kmp_s_1306r_0976 ) - 1.0 ) ) / intracellular '
	# shikimate kinase
	r_0977 = 'intracellular * r_0977__Vmax_r_0977 * ( pow ( 1.0 / r_0977__kms_s_0446r_0977 , 1.0 ) * pow ( 1.0 / r_0977__kms_s_1306r_0977 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_1306 , 1.0 ) - pow ( s_0267 , 1.0 ) * pow ( s_0400 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0977__Keq_r_0977 ) / ( ( 1.0 + s_0446 / r_0977__kms_s_0446r_0977 ) * ( 1.0 + s_1306 / r_0977__kms_s_1306r_0977 ) + ( 1.0 + s_0267 / r_0977__kmp_s_0267r_0977 ) * ( 1.0 + s_0400 / r_0977__kmp_s_0400r_0977 ) * ( 1.0 + s_0763_b / r_0977__kmp_s_0763_br_0977 ) - 1.0 ) ) / intracellular '

	########### superpathway of phosphatidate biosynthesis ###########

	# glycerol-3-phosphate dehydrogenase (NAD)
	r_0530 = 'intracellular * r_0530__Vmax_r_0530 * ( pow ( 1.0 / r_0530__kms_s_0735r_0530 , 1.0 ) * pow ( 1.0 / r_0530__kms_s_0763_br_0530 , 1.0 ) * pow ( 1.0 / r_0530__kms_s_1087r_0530 , 1.0 ) * ( pow ( s_0735 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1087 , 1.0 ) - pow ( s_1082 , 1.0 ) * pow ( s_1315 , 1.0 ) / r_0530__Keq_r_0530 ) / ( ( 1.0 + s_0735 / r_0530__kms_s_0735r_0530 ) * ( 1.0 + s_0763_b / r_0530__kms_s_0763_br_0530 ) * ( 1.0 + s_1087 / r_0530__kms_s_1087r_0530 ) + ( 1.0 + s_1082 / r_0530__kmp_s_1082r_0530 ) * ( 1.0 + s_1315 / r_0530__kmp_s_1315r_0530 ) - 1.0 ) ) / intracellular '

	########### superpathway of phospholipid biosynthesis ###########

	# phosphatidylethanolamine methyltransferase
	r_0831 = 'intracellular * r_0831__Vmax_r_0831 * ( pow ( 1.0 / r_0831__kms_s_1233r_0831 , 1.0 ) * pow ( 1.0 / r_0831__kms_s_1293r_0831 , 1.0 ) * ( pow ( s_1233 , 1.0 ) * pow ( s_1293 , 1.0 ) - pow ( s_0763_b , 1.0 ) * pow ( s_1226 , 1.0 ) * pow ( s_1290 , 1.0 ) / r_0831__Keq_r_0831 ) / ( ( 1.0 + s_1233 / r_0831__kms_s_1233r_0831 ) * ( 1.0 + s_1293 / r_0831__kms_s_1293r_0831 ) + ( 1.0 + s_0763_b / r_0831__kmp_s_0763_br_0831 ) * ( 1.0 + s_1226 / r_0831__kmp_s_1226r_0831 ) * ( 1.0 + s_1290 / r_0831__kmp_s_1290r_0831 ) - 1.0 ) ) / intracellular '
	# phosphatidylserine decarboxylase
	r_0850 = 'intracellular * r_0850__Vmax_r_0850 * ( pow ( 1.0 / r_0850__kms_s_1219r_0850 , 1.0 ) * ( pow ( s_1219 , 1.0 ) - pow ( s_0470 , 1.0 ) * pow ( s_1233 , 1.0 ) / r_0850__Keq_r_0850 ) / ( 1.0 + s_1219 / r_0850__kms_s_1219r_0850 + ( 1.0 + s_0470 / r_0850__kmp_s_0470r_0850 ) * ( 1.0 + s_1233 / r_0850__kmp_s_1233r_0850 ) - 1.0 ) ) / intracellular '
	# phosphatidylserine synthase
	r_0853 = 'intracellular * r_0853__Vmax_r_0853 * ( pow ( 1.0 / r_0853__kms_s_0485r_0853 , 1.0 ) * pow ( 1.0 / r_0853__kms_s_0943r_0853 , 1.0 ) * ( pow ( s_0485 , 1.0 ) * pow ( s_0943 , 1.0 ) - pow ( s_0511 , 1.0 ) * pow ( s_0763_b , 2.0 ) * pow ( s_1219 , 1.0 ) / r_0853__Keq_r_0853 ) / ( ( 1.0 + s_0485 / r_0853__kms_s_0485r_0853 ) * ( 1.0 + s_0943 / r_0853__kms_s_0943r_0853 ) + ( 1.0 + s_0511 / r_0853__kmp_s_0511r_0853 ) * ( 1.0 + s_0763_b / r_0853__kmp_s_0763_br_0853 ) * ( 1.0 + s_1219 / r_0853__kmp_s_1219r_0853 ) - 1.0 ) ) / intracellular '
	# phospholipid methyltransferase
	r_0873 = 'intracellular * r_0873__Vmax_r_0873 * ( pow ( 1.0 / r_0873__kms_s_1225r_0873 , 1.0 ) * pow ( 1.0 / r_0873__kms_s_1293r_0873 , 1.0 ) * ( pow ( s_1225 , 1.0 ) * pow ( s_1293 , 1.0 ) - pow ( s_1228 , 1.0 ) * pow ( s_1290 , 1.0 ) / r_0873__Keq_r_0873 ) / ( ( 1.0 + s_1225 / r_0873__kms_s_1225r_0873 ) * ( 1.0 + s_1293 / r_0873__kms_s_1293r_0873 ) + ( 1.0 + s_1228 / r_0873__kmp_s_1228r_0873 ) * ( 1.0 + s_1290 / r_0873__kmp_s_1290r_0873 ) - 1.0 ) ) / intracellular '
	# phospholipid methyltransferase_2
	r_0874 = 'intracellular * r_0874__Vmax_r_0874 * ( pow ( 1.0 / r_0874__kms_s_1226r_0874 , 1.0 ) * pow ( 1.0 / r_0874__kms_s_1293r_0874 , 1.0 ) * ( pow ( s_1226 , 1.0 ) * pow ( s_1293 , 1.0 ) - pow ( s_0763_b , 1.0 ) * pow ( s_1225 , 1.0 ) * pow ( s_1290 , 1.0 ) / r_0874__Keq_r_0874 ) / ( ( 1.0 + s_1226 / r_0874__kms_s_1226r_0874 ) * ( 1.0 + s_1293 / r_0874__kms_s_1293r_0874 ) + ( 1.0 + s_0763_b / r_0874__kmp_s_0763_br_0874 ) * ( 1.0 + s_1225 / r_0874__kmp_s_1225r_0874 ) * ( 1.0 + s_1290 / r_0874__kmp_s_1290r_0874 ) - 1.0 ) ) / intracellular '

	########### superpathway of purine biosynthesis and salvage pathways ###########

	# adenosine kinase
	r_0157 = 'intracellular * r_0157__Vmax_r_0157 * ( pow ( 1.0 / r_0157__kms_s_0393r_0157 , 1.0 ) * pow ( 1.0 / r_0157__kms_s_0446r_0157 , 1.0 ) * ( pow ( s_0393 , 1.0 ) * pow ( s_0446 , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_0434 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0157__Keq_r_0157 ) / ( ( 1.0 + s_0393 / r_0157__kms_s_0393r_0157 ) * ( 1.0 + s_0446 / r_0157__kms_s_0446r_0157 ) + ( 1.0 + s_0400 / r_0157__kmp_s_0400r_0157 ) * ( 1.0 + s_0434 / r_0157__kmp_s_0434r_0157 ) * ( 1.0 + s_0763_b / r_0157__kmp_s_0763_br_0157 ) - 1.0 ) ) / intracellular '
	# adenylate kinase
	r_0163 = 'intracellular * r_0163__Vmax_r_0163 * ( pow ( 1.0 / r_0163__kms_s_0400r_0163 , 2.0 ) * ( pow ( s_0400 , 2.0 ) - pow ( s_0434 , 1.0 ) * pow ( s_0446 , 1.0 ) / r_0163__Keq_r_0163 ) / ( 1.0 + s_0400 / r_0163__kms_s_0400r_0163 + ( 1.0 + s_0434 / r_0163__kmp_s_0434r_0163 ) * ( 1.0 + s_0446 / r_0163__kmp_s_0446r_0163 ) - 1.0 ) ) / intracellular '
	# adenylate kinase (GTP)
	r_0165 = 'intracellular * r_0165__Vmax_r_0165 * ( pow ( 1.0 / r_0165__kms_s_0400r_0165 , 1.0 ) * pow ( 1.0 / r_0165__kms_s_0706r_0165 , 1.0 ) * ( pow ( s_0400 , 1.0 ) * pow ( s_0706 , 1.0 ) - pow ( s_0434 , 1.0 ) * pow ( s_0755 , 1.0 ) / r_0165__Keq_r_0165 ) / ( ( 1.0 + s_0400 / r_0165__kms_s_0400r_0165 ) * ( 1.0 + s_0706 / r_0165__kms_s_0706r_0165 ) + ( 1.0 + s_0434 / r_0165__kmp_s_0434r_0165 ) * ( 1.0 + s_0755 / r_0165__kmp_s_0755r_0165 ) - 1.0 ) ) / intracellular '
	# adenylosuccinate lyase
	r_0169 = 'intracellular * r_0169__Vmax_r_0169 * ( pow ( 1.0 / r_0169__kms_s_0009r_0169 , 1.0 ) * ( pow ( s_0009 , 1.0 ) - pow ( s_0317 , 1.0 ) * pow ( s_0692 , 1.0 ) / r_0169__Keq_r_0169 ) / ( 1.0 + s_0009 / r_0169__kms_s_0009r_0169 + ( 1.0 + s_0317 / r_0169__kmp_s_0317r_0169 ) * ( 1.0 + s_0692 / r_0169__kmp_s_0692r_0169 ) - 1.0 ) ) / intracellular '
	# adenylosuccinate synthase
	r_0170 = 'intracellular * r_0170__Vmax_r_0170 * ( pow ( 1.0 / r_0170__kms_s_0755r_0170 , 1.0 ) * pow ( 1.0 / r_0170__kms_s_0816r_0170 , 1.0 ) * pow ( 1.0 / r_0170__kms_s_0881r_0170 , 1.0 ) * ( pow ( s_0755 , 1.0 ) * pow ( s_0816 , 1.0 ) * pow ( s_0881 , 1.0 ) - pow ( s_0706 , 1.0 ) * pow ( s_0763_b , 2.0 ) * pow ( s_1053 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0170__Keq_r_0170 ) / ( ( 1.0 + s_0755 / r_0170__kms_s_0755r_0170 ) * ( 1.0 + s_0816 / r_0170__kms_s_0816r_0170 ) * ( 1.0 + s_0881 / r_0170__kms_s_0881r_0170 ) + ( 1.0 + s_0706 / r_0170__kmp_s_0706r_0170 ) * ( 1.0 + s_0763_b / r_0170__kmp_s_0763_br_0170 ) * ( 1.0 + s_1053 / r_0170__kmp_s_1053r_0170 ) * ( 1.0 + s_1207 / r_0170__kmp_s_1207r_0170 ) - 1.0 ) ) / intracellular '
	# adenylsuccinate lyase
	r_0171 = 'intracellular * r_0171__Vmax_r_0171 * ( pow ( 1.0 / r_0171__kms_s_1053r_0171 , 1.0 ) * ( pow ( s_1053 , 1.0 ) - pow ( s_0434 , 1.0 ) * pow ( s_0692 , 1.0 ) / r_0171__Keq_r_0171 ) / ( 1.0 + s_1053 / r_0171__kms_s_1053r_0171 + ( 1.0 + s_0434 / r_0171__kmp_s_0434r_0171 ) * ( 1.0 + s_0692 / r_0171__kmp_s_0692r_0171 ) - 1.0 ) ) / intracellular '
	# deoxyguanylate kinase (dGMP:ATP)
	r_0362 = 'intracellular * r_0362__Vmax_r_0362 * ( pow ( 1.0 / r_0362__kms_s_0400r_0362 , 1.0 ) * pow ( 1.0 / r_0362__kms_s_0591r_0362 , 1.0 ) * ( pow ( s_0400 , 1.0 ) * pow ( s_0591 , 1.0 ) - pow ( s_0446 , 1.0 ) * pow ( s_0593 , 1.0 ) / r_0362__Keq_r_0362 ) / ( ( 1.0 + s_0400 / r_0362__kms_s_0400r_0362 ) * ( 1.0 + s_0591 / r_0362__kms_s_0591r_0362 ) + ( 1.0 + s_0446 / r_0362__kmp_s_0446r_0362 ) * ( 1.0 + s_0593 / r_0362__kmp_s_0593r_0362 ) - 1.0 ) ) / intracellular '
	# glutamine phosphoribosyldiphosphate amidotransferase
	r_0514 = 'intracellular * r_0514__Vmax_r_0514 * ( pow ( 1.0 / r_0514__kms_s_0331r_0514 , 1.0 ) * pow ( 1.0 / r_0514__kms_s_0907r_0514 , 1.0 ) * pow ( 1.0 / r_0514__kms_s_1434_br_0514 , 1.0 ) * ( pow ( s_0331 , 1.0 ) * pow ( s_0907 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0333 , 1.0 ) * pow ( s_0605 , 1.0 ) * pow ( s_0899 , 1.0 ) / r_0514__Keq_r_0514 ) / ( ( 1.0 + s_0331 / r_0514__kms_s_0331r_0514 ) * ( 1.0 + s_0907 / r_0514__kms_s_0907r_0514 ) * ( 1.0 + s_1434_b / r_0514__kms_s_1434_br_0514 ) + ( 1.0 + s_0333 / r_0514__kmp_s_0333r_0514 ) * ( 1.0 + s_0605 / r_0514__kmp_s_0605r_0514 ) * ( 1.0 + s_0899 / r_0514__kmp_s_0899r_0514 ) - 1.0 ) ) / intracellular '
	# guanylate kinase (GMP:ATP)
	r_0567 = 'intracellular * r_0567__Vmax_r_0567 * ( pow ( 1.0 / r_0567__kms_s_0446r_0567 , 1.0 ) * pow ( 1.0 / r_0567__kms_s_0752r_0567 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_0752 , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_0706 , 1.0 ) / r_0567__Keq_r_0567 ) / ( ( 1.0 + s_0446 / r_0567__kms_s_0446r_0567 ) * ( 1.0 + s_0752 / r_0567__kms_s_0752r_0567 ) + ( 1.0 + s_0400 / r_0567__kmp_s_0400r_0567 ) * ( 1.0 + s_0706 / r_0567__kmp_s_0706r_0567 ) - 1.0 ) ) / intracellular '
	# guanylate kinase (GMP:dATP)
	r_0568 = 'intracellular * r_0568__Vmax_r_0568 * ( pow ( 1.0 / r_0568__kms_s_0566r_0568 , 1.0 ) * pow ( 1.0 / r_0568__kms_s_0752r_0568 , 1.0 ) * ( pow ( s_0566 , 1.0 ) * pow ( s_0752 , 1.0 ) - pow ( s_0562 , 1.0 ) * pow ( s_0706 , 1.0 ) / r_0568__Keq_r_0568 ) / ( ( 1.0 + s_0566 / r_0568__kms_s_0566r_0568 ) * ( 1.0 + s_0752 / r_0568__kms_s_0752r_0568 ) + ( 1.0 + s_0562 / r_0568__kmp_s_0562r_0568 ) * ( 1.0 + s_0706 / r_0568__kmp_s_0706r_0568 ) - 1.0 ) ) / intracellular '
	# IMP cyclohydrolase
	r_0606 = 'intracellular * r_0606__Vmax_r_0606 * ( pow ( 1.0 / r_0606__kms_s_0325r_0606 , 1.0 ) * ( pow ( s_0325 , 1.0 ) - pow ( s_0816 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0606__Keq_r_0606 ) / ( 1.0 + s_0325 / r_0606__kms_s_0325r_0606 + ( 1.0 + s_0816 / r_0606__kmp_s_0816r_0606 ) * ( 1.0 + s_1434_b / r_0606__kmp_s_1434_br_0606 ) - 1.0 ) ) / intracellular '
	# IMP dehydrogenase
	r_0607 = 'intracellular * r_0607__Vmax_r_0607 * ( pow ( 1.0 / r_0607__kms_s_0816r_0607 , 1.0 ) * pow ( 1.0 / r_0607__kms_s_1082r_0607 , 1.0 ) * pow ( 1.0 / r_0607__kms_s_1434_br_0607 , 1.0 ) * ( pow ( s_0816 , 1.0 ) * pow ( s_1082 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0306 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1087 , 1.0 ) / r_0607__Keq_r_0607 ) / ( ( 1.0 + s_0816 / r_0607__kms_s_0816r_0607 ) * ( 1.0 + s_1082 / r_0607__kms_s_1082r_0607 ) * ( 1.0 + s_1434_b / r_0607__kms_s_1434_br_0607 ) + ( 1.0 + s_0306 / r_0607__kmp_s_0306r_0607 ) * ( 1.0 + s_0763_b / r_0607__kmp_s_0763_br_0607 ) * ( 1.0 + s_1087 / r_0607__kmp_s_1087r_0607 ) - 1.0 ) ) / intracellular '
	# phosphoribosylaminoimidazole carboxylase
	r_0883 = 'intracellular * r_0883__Vmax_r_0883 * ( pow ( 1.0 / r_0883__kms_s_0316r_0883 , 1.0 ) * pow ( 1.0 / r_0883__kms_s_0470r_0883 , 1.0 ) * ( pow ( s_0316 , 1.0 ) * pow ( s_0470 , 1.0 ) - pow ( s_0318 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0883__Keq_r_0883 ) / ( ( 1.0 + s_0316 / r_0883__kms_s_0316r_0883 ) * ( 1.0 + s_0470 / r_0883__kms_s_0470r_0883 ) + ( 1.0 + s_0318 / r_0883__kmp_s_0318r_0883 ) * ( 1.0 + s_0763_b / r_0883__kmp_s_0763_br_0883 ) - 1.0 ) ) / intracellular '
	# phosphoribosylaminoimidazolecarboxamide formyltransferase
	r_0885 = 'intracellular * r_0885__Vmax_r_0885 * ( pow ( 1.0 / r_0885__kms_s_0122r_0885 , 1.0 ) * pow ( 1.0 / r_0885__kms_s_0317r_0885 , 1.0 ) * ( pow ( s_0122 , 1.0 ) * pow ( s_0317 , 1.0 ) - pow ( s_0309 , 1.0 ) * pow ( s_0325 , 1.0 ) / r_0885__Keq_r_0885 ) / ( ( 1.0 + s_0122 / r_0885__kms_s_0122r_0885 ) * ( 1.0 + s_0317 / r_0885__kms_s_0317r_0885 ) + ( 1.0 + s_0309 / r_0885__kmp_s_0309r_0885 ) * ( 1.0 + s_0325 / r_0885__kmp_s_0325r_0885 ) - 1.0 ) ) / intracellular '
	# phosphoribosylaminoimidazolesuccinocarboxamide synthase
	r_0886 = 'intracellular * r_0886__Vmax_r_0886 * ( pow ( 1.0 / r_0886__kms_s_0318r_0886 , 1.0 ) * pow ( 1.0 / r_0886__kms_s_0446r_0886 , 1.0 ) * pow ( 1.0 / r_0886__kms_s_0881r_0886 , 1.0 ) * ( pow ( s_0318 , 1.0 ) * pow ( s_0446 , 1.0 ) * pow ( s_0881 , 1.0 ) - pow ( s_0009 , 1.0 ) * pow ( s_0400 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0886__Keq_r_0886 ) / ( ( 1.0 + s_0318 / r_0886__kms_s_0318r_0886 ) * ( 1.0 + s_0446 / r_0886__kms_s_0446r_0886 ) * ( 1.0 + s_0881 / r_0886__kms_s_0881r_0886 ) + ( 1.0 + s_0009 / r_0886__kmp_s_0009r_0886 ) * ( 1.0 + s_0400 / r_0886__kmp_s_0400r_0886 ) * ( 1.0 + s_0763_b / r_0886__kmp_s_0763_br_0886 ) * ( 1.0 + s_1207 / r_0886__kmp_s_1207r_0886 ) - 1.0 ) ) / intracellular '
	# phosphoribosylformylglycinamidine synthase
	r_0888 = 'intracellular * r_0888__Vmax_r_0888 * ( pow ( 1.0 / r_0888__kms_s_0446r_0888 , 1.0 ) * pow ( 1.0 / r_0888__kms_s_0907r_0888 , 1.0 ) * pow ( 1.0 / r_0888__kms_s_1052r_0888 , 1.0 ) * pow ( 1.0 / r_0888__kms_s_1434_br_0888 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_0907 , 1.0 ) * pow ( s_1052 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0158 , 1.0 ) * pow ( s_0400 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_0899 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0888__Keq_r_0888 ) / ( ( 1.0 + s_0446 / r_0888__kms_s_0446r_0888 ) * ( 1.0 + s_0907 / r_0888__kms_s_0907r_0888 ) * ( 1.0 + s_1052 / r_0888__kms_s_1052r_0888 ) * ( 1.0 + s_1434_b / r_0888__kms_s_1434_br_0888 ) + ( 1.0 + s_0158 / r_0888__kmp_s_0158r_0888 ) * ( 1.0 + s_0400 / r_0888__kmp_s_0400r_0888 ) * ( 1.0 + s_0763_b / r_0888__kmp_s_0763_br_0888 ) * ( 1.0 + s_0899 / r_0888__kmp_s_0899r_0888 ) * ( 1.0 + s_1207 / r_0888__kmp_s_1207r_0888 ) - 1.0 ) ) / intracellular '
	# phosphoribosylglycinamide formyltransferase
	r_0889 = 'intracellular * r_0889__Vmax_r_0889 * ( pow ( 1.0 / r_0889__kms_s_0122r_0889 , 1.0 ) * pow ( 1.0 / r_0889__kms_s_1048r_0889 , 1.0 ) * ( pow ( s_0122 , 1.0 ) * pow ( s_1048 , 1.0 ) - pow ( s_0309 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1052 , 1.0 ) / r_0889__Keq_r_0889 ) / ( ( 1.0 + s_0122 / r_0889__kms_s_0122r_0889 ) * ( 1.0 + s_1048 / r_0889__kms_s_1048r_0889 ) + ( 1.0 + s_0309 / r_0889__kmp_s_0309r_0889 ) * ( 1.0 + s_0763_b / r_0889__kmp_s_0763_br_0889 ) * ( 1.0 + s_1052 / r_0889__kmp_s_1052r_0889 ) - 1.0 ) ) / intracellular '

	########### superpathway of serine and glycine biosynthesis ###########

	# alanine glyoxylate aminotransferase
	r_0174 = 'intracellular * r_0174__Vmax_r_0174 * ( pow ( 1.0 / r_0174__kms_s_0749r_0174 , 1.0 ) * pow ( 1.0 / r_0174__kms_s_0863r_0174 , 1.0 ) * ( pow ( s_0749 , 1.0 ) * pow ( s_0863 , 1.0 ) - pow ( s_0740 , 1.0 ) * pow ( s_1277 , 1.0 ) / r_0174__Keq_r_0174 ) / ( ( 1.0 + s_0749 / r_0174__kms_s_0749r_0174 ) * ( 1.0 + s_0863 / r_0174__kms_s_0863r_0174 ) + ( 1.0 + s_0740 / r_0174__kmp_s_0740r_0174 ) * ( 1.0 + s_1277 / r_0174__kmp_s_1277r_0174 ) - 1.0 ) ) / intracellular '
	# glycine hydroxymethyltransferase
	r_0539 = 'intracellular * r_0539__Vmax_r_0539 * ( pow ( 1.0 / r_0539__kms_s_0307r_0539 , 1.0 ) * pow ( 1.0 / r_0539__kms_s_0740r_0539 , 1.0 ) * pow ( 1.0 / r_0539__kms_s_1434_br_0539 , 1.0 ) * ( pow ( s_0307 , 1.0 ) * pow ( s_0740 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0309 , 1.0 ) * pow ( s_0943 , 1.0 ) / r_0539__Keq_r_0539 ) / ( ( 1.0 + s_0307 / r_0539__kms_s_0307r_0539 ) * ( 1.0 + s_0740 / r_0539__kms_s_0740r_0539 ) * ( 1.0 + s_1434_b / r_0539__kms_s_1434_br_0539 ) + ( 1.0 + s_0309 / r_0539__kmp_s_0309r_0539 ) * ( 1.0 + s_0943 / r_0539__kmp_s_0943r_0539 ) - 1.0 ) ) / intracellular '
	# threonine aldolase
	r_1026 = 'intracellular * r_1026__Vmax_r_1026 * ( pow ( 1.0 / r_1026__kms_s_0949r_1026 , 1.0 ) * ( pow ( s_0949 , 1.0 ) - pow ( s_0366 , 1.0 ) * pow ( s_0740 , 1.0 ) / r_1026__Keq_r_1026 ) / ( 1.0 + s_0949 / r_1026__kms_s_0949r_1026 + ( 1.0 + s_0366 / r_1026__kmp_s_0366r_1026 ) * ( 1.0 + s_0740 / r_1026__kmp_s_0740r_1026 ) - 1.0 ) ) / intracellular '

	########### superpathway of sulfur amino acid biosynthesis ###########

	# adenylyl-sulfate kinase
	r_0172 = 'intracellular * r_0172__Vmax_r_0172 * ( pow ( 1.0 / r_0172__kms_s_0304r_0172 , 1.0 ) * pow ( 1.0 / r_0172__kms_s_0446r_0172 , 1.0 ) * ( pow ( s_0304 , 1.0 ) * pow ( s_0446 , 1.0 ) - pow ( s_0206 , 1.0 ) * pow ( s_0400 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0172__Keq_r_0172 ) / ( ( 1.0 + s_0304 / r_0172__kms_s_0304r_0172 ) * ( 1.0 + s_0446 / r_0172__kms_s_0446r_0172 ) + ( 1.0 + s_0206 / r_0172__kmp_s_0206r_0172 ) * ( 1.0 + s_0400 / r_0172__kmp_s_0400r_0172 ) * ( 1.0 + s_0763_b / r_0172__kmp_s_0763_br_0172 ) - 1.0 ) ) / intracellular '
	# cystathionine beta-synthase
	r_0338 = 'intracellular * r_0338__Vmax_r_0338 * ( pow ( 1.0 / r_0338__kms_s_0917r_0338 , 1.0 ) * pow ( 1.0 / r_0338__kms_s_0943r_0338 , 1.0 ) * ( pow ( s_0917 , 1.0 ) * pow ( s_0943 , 1.0 ) - pow ( s_0888 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0338__Keq_r_0338 ) / ( ( 1.0 + s_0917 / r_0338__kms_s_0917r_0338 ) * ( 1.0 + s_0943 / r_0338__kms_s_0943r_0338 ) + ( 1.0 + s_0888 / r_0338__kmp_s_0888r_0338 ) * ( 1.0 + s_1434_b / r_0338__kmp_s_1434_br_0338 ) - 1.0 ) ) / intracellular '
	# cystathionine gamma-synthase
	r_0340 = 'intracellular * r_0340__Vmax_r_0340 * ( pow ( 1.0 / r_0340__kms_s_0889r_0340 , 1.0 ) * pow ( 1.0 / r_0340__kms_s_1117r_0340 , 1.0 ) * ( pow ( s_0889 , 1.0 ) * pow ( s_1117 , 1.0 ) - pow ( s_0369 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_0888 , 1.0 ) / r_0340__Keq_r_0340 ) / ( ( 1.0 + s_0889 / r_0340__kms_s_0889r_0340 ) * ( 1.0 + s_1117 / r_0340__kms_s_1117r_0340 ) + ( 1.0 + s_0369 / r_0340__kmp_s_0369r_0340 ) * ( 1.0 + s_0763_b / r_0340__kmp_s_0763_br_0340 ) * ( 1.0 + s_0888 / r_0340__kmp_s_0888r_0340 ) - 1.0 ) ) / intracellular '
	# homoserine O-trans-acetylase
	r_0589 = 'intracellular * r_0589__Vmax_r_0589 * ( pow ( 1.0 / r_0589__kms_s_0380r_0589 , 1.0 ) * pow ( 1.0 / r_0589__kms_s_0919r_0589 , 1.0 ) * ( pow ( s_0380 , 1.0 ) * pow ( s_0919 , 1.0 ) - pow ( s_0514 , 1.0 ) * pow ( s_1117 , 1.0 ) / r_0589__Keq_r_0589 ) / ( ( 1.0 + s_0380 / r_0589__kms_s_0380r_0589 ) * ( 1.0 + s_0919 / r_0589__kms_s_0919r_0589 ) + ( 1.0 + s_0514 / r_0589__kmp_s_0514r_0589 ) * ( 1.0 + s_1117 / r_0589__kmp_s_1117r_0589 ) - 1.0 ) ) / intracellular '
	# methionine synthase
	r_0702 = 'intracellular * r_0702__Vmax_r_0702 * ( pow ( 1.0 / r_0702__kms_s_0328r_0702 , 1.0 ) * pow ( 1.0 / r_0702__kms_s_0917r_0702 , 1.0 ) * ( pow ( s_0328 , 1.0 ) * pow ( s_0917 , 1.0 ) - pow ( s_0309 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_0933 , 1.0 ) / r_0702__Keq_r_0702 ) / ( ( 1.0 + s_0328 / r_0702__kms_s_0328r_0702 ) * ( 1.0 + s_0917 / r_0702__kms_s_0917r_0702 ) + ( 1.0 + s_0309 / r_0702__kmp_s_0309r_0702 ) * ( 1.0 + s_0763_b / r_0702__kmp_s_0763_br_0702 ) * ( 1.0 + s_0933 / r_0702__kmp_s_0933r_0702 ) - 1.0 ) ) / intracellular '
	# O-acetylhomoserine (thiol)-lyase
	r_0783 = 'intracellular * r_0783__Vmax_r_0783 * ( pow ( 1.0 / r_0783__kms_s_0805r_0783 , 1.0 ) * pow ( 1.0 / r_0783__kms_s_1117r_0783 , 1.0 ) * ( pow ( s_0805 , 1.0 ) * pow ( s_1117 , 1.0 ) - pow ( s_0369 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_0917 , 1.0 ) / r_0783__Keq_r_0783 ) / ( ( 1.0 + s_0805 / r_0783__kms_s_0805r_0783 ) * ( 1.0 + s_1117 / r_0783__kms_s_1117r_0783 ) + ( 1.0 + s_0369 / r_0783__kmp_s_0369r_0783 ) * ( 1.0 + s_0763_b / r_0783__kmp_s_0763_br_0783 ) * ( 1.0 + s_0917 / r_0783__kmp_s_0917r_0783 ) - 1.0 ) ) / intracellular '
	# phosphoadenylyl-sulfate reductase (thioredoxin)
	r_0856 = 'intracellular * r_0856__Vmax_r_0856 * ( pow ( 1.0 / r_0856__kms_s_0206r_0856 , 1.0 ) * pow ( 1.0 / r_0856__kms_s_1521r_0856 , 1.0 ) * ( pow ( s_0206 , 1.0 ) * pow ( s_1521 , 1.0 ) - pow ( s_0397 , 1.0 ) * pow ( s_0763_b , 2.0 ) * pow ( s_1349 , 1.0 ) * pow ( s_1517 , 1.0 ) / r_0856__Keq_r_0856 ) / ( ( 1.0 + s_0206 / r_0856__kms_s_0206r_0856 ) * ( 1.0 + s_1521 / r_0856__kms_s_1521r_0856 ) + ( 1.0 + s_0397 / r_0856__kmp_s_0397r_0856 ) * ( 1.0 + s_0763_b / r_0856__kmp_s_0763_br_0856 ) * ( 1.0 + s_1349 / r_0856__kmp_s_1349r_0856 ) * ( 1.0 + s_1517 / r_0856__kmp_s_1517r_0856 ) - 1.0 ) ) / intracellular '
	# sulfite reductase (NADPH2)
	r_1008 = 'intracellular * r_1008__Vmax_r_1008 * ( pow ( 1.0 / r_1008__kms_s_0763_br_1008 , 5.0 ) * pow ( 1.0 / r_1008__kms_s_1096r_1008 , 3.0 ) * pow ( 1.0 / r_1008__kms_s_1349r_1008 , 1.0 ) * ( pow ( s_0763_b , 5.0 ) * pow ( s_1096 , 3.0 ) * pow ( s_1349 , 1.0 ) - pow ( s_0805 , 1.0 ) * pow ( s_1091 , 3.0 ) * pow ( s_1434_b , 3.0 ) / r_1008__Keq_r_1008 ) / ( ( 1.0 + s_0763_b / r_1008__kms_s_0763_br_1008 ) * ( 1.0 + s_1096 / r_1008__kms_s_1096r_1008 ) * ( 1.0 + s_1349 / r_1008__kms_s_1349r_1008 ) + ( 1.0 + s_0805 / r_1008__kmp_s_0805r_1008 ) * ( 1.0 + s_1091 / r_1008__kmp_s_1091r_1008 ) * ( 1.0 + s_1434_b / r_1008__kmp_s_1434_br_1008 ) - 1.0 ) ) / intracellular '

	########### superpathway of threonine biosynthesis ###########

	# aspartate transaminase
	r_0235 = 'intracellular * r_0235__Vmax_r_0235 * ( pow ( 1.0 / r_0235__kms_s_0899r_0235 , 1.0 ) * pow ( 1.0 / r_0235__kms_s_1156r_0235 , 1.0 ) * ( pow ( s_0899 , 1.0 ) * pow ( s_1156 , 1.0 ) - pow ( s_0185 , 1.0 ) * pow ( s_0881 , 1.0 ) / r_0235__Keq_r_0235 ) / ( ( 1.0 + s_0899 / r_0235__kms_s_0899r_0235 ) * ( 1.0 + s_1156 / r_0235__kms_s_1156r_0235 ) + ( 1.0 + s_0185 / r_0235__kmp_s_0185r_0235 ) * ( 1.0 + s_0881 / r_0235__kmp_s_0881r_0235 ) - 1.0 ) ) / intracellular '
	# tyrosine transaminase
	r_1050 = 'intracellular * r_1050__Vmax_r_1050 * ( pow ( 1.0 / r_1050__kms_s_0209r_1050 , 1.0 ) * pow ( 1.0 / r_1050__kms_s_0899r_1050 , 1.0 ) * ( pow ( s_0209 , 1.0 ) * pow ( s_0899 , 1.0 ) - pow ( s_0185 , 1.0 ) * pow ( s_0955 , 1.0 ) / r_1050__Keq_r_1050 ) / ( ( 1.0 + s_0209 / r_1050__kms_s_0209r_1050 ) * ( 1.0 + s_0899 / r_1050__kms_s_0899r_1050 ) + ( 1.0 + s_0185 / r_1050__kmp_s_0185r_1050 ) * ( 1.0 + s_0955 / r_1050__kmp_s_0955r_1050 ) - 1.0 ) ) / intracellular '

	########### superpathway of ubiquinone biosynthesis ###########

	# dimethylallyltranstransferase
	r_0387 = 'intracellular * r_0387__Vmax_r_0387 * ( pow ( 1.0 / r_0387__kms_s_0850r_0387 , 1.0 ) * pow ( 1.0 / r_0387__kms_s_1257r_0387 , 1.0 ) * ( pow ( s_0850 , 1.0 ) * pow ( s_1257 , 1.0 ) - pow ( s_0605 , 1.0 ) * pow ( s_0712 , 1.0 ) / r_0387__Keq_r_0387 ) / ( ( 1.0 + s_0850 / r_0387__kms_s_0850r_0387 ) * ( 1.0 + s_1257 / r_0387__kms_s_1257r_0387 ) + ( 1.0 + s_0605 / r_0387__kmp_s_0605r_0387 ) * ( 1.0 + s_0712 / r_0387__kmp_s_0712r_0387 ) - 1.0 ) ) / intracellular '
	# geranyltranstransferase
	r_0496 = 'intracellular * r_0496__Vmax_r_0496 * ( pow ( 1.0 / r_0496__kms_s_0712r_0496 , 1.0 ) * pow ( 1.0 / r_0496__kms_s_0850r_0496 , 1.0 ) * ( pow ( s_0712 , 1.0 ) * pow ( s_0850 , 1.0 ) - pow ( s_0195 , 1.0 ) * pow ( s_0605 , 1.0 ) / r_0496__Keq_r_0496 ) / ( ( 1.0 + s_0712 / r_0496__kms_s_0712r_0496 ) * ( 1.0 + s_0850 / r_0496__kms_s_0850r_0496 ) + ( 1.0 + s_0195 / r_0496__kmp_s_0195r_0496 ) * ( 1.0 + s_0605 / r_0496__kmp_s_0605r_0496 ) - 1.0 ) ) / intracellular '

	########### thioredoxin system ###########

	# phosphoadenylyl-sulfate reductase (thioredoxin)
	r_0856 = 'intracellular * r_0856__Vmax_r_0856 * ( pow ( 1.0 / r_0856__kms_s_0206r_0856 , 1.0 ) * pow ( 1.0 / r_0856__kms_s_1521r_0856 , 1.0 ) * ( pow ( s_0206 , 1.0 ) * pow ( s_1521 , 1.0 ) - pow ( s_0397 , 1.0 ) * pow ( s_0763_b , 2.0 ) * pow ( s_1349 , 1.0 ) * pow ( s_1517 , 1.0 ) / r_0856__Keq_r_0856 ) / ( ( 1.0 + s_0206 / r_0856__kms_s_0206r_0856 ) * ( 1.0 + s_1521 / r_0856__kms_s_1521r_0856 ) + ( 1.0 + s_0397 / r_0856__kmp_s_0397r_0856 ) * ( 1.0 + s_0763_b / r_0856__kmp_s_0763_br_0856 ) * ( 1.0 + s_1349 / r_0856__kmp_s_1349r_0856 ) * ( 1.0 + s_1517 / r_0856__kmp_s_1517r_0856 ) - 1.0 ) ) / intracellular '
	# ribonucleoside-diphosphate reductase (GDP)
	r_0955 = 'intracellular * r_0955__Vmax_r_0955 * ( pow ( 1.0 / r_0955__kms_s_0706r_0955 , 1.0 ) * pow ( 1.0 / r_0955__kms_s_1521r_0955 , 1.0 ) * ( pow ( s_0706 , 1.0 ) * pow ( s_1521 , 1.0 ) - pow ( s_0591 , 1.0 ) * pow ( s_1434_b , 1.0 ) * pow ( s_1517 , 1.0 ) / r_0955__Keq_r_0955 ) / ( ( 1.0 + s_0706 / r_0955__kms_s_0706r_0955 ) * ( 1.0 + s_1521 / r_0955__kms_s_1521r_0955 ) + ( 1.0 + s_0591 / r_0955__kmp_s_0591r_0955 ) * ( 1.0 + s_1434_b / r_0955__kmp_s_1434_br_0955 ) * ( 1.0 + s_1517 / r_0955__kmp_s_1517r_0955 ) - 1.0 ) ) / intracellular '
	# ribonucleoside-diphosphate reductase (UDP)
	r_0957 = 'intracellular * r_0957__Vmax_r_0957 * ( pow ( 1.0 / r_0957__kms_s_1411r_0957 , 1.0 ) * pow ( 1.0 / r_0957__kms_s_1521r_0957 , 1.0 ) * ( pow ( s_1411 , 1.0 ) * pow ( s_1521 , 1.0 ) - pow ( s_0622 , 1.0 ) * pow ( s_1434_b , 1.0 ) * pow ( s_1517 , 1.0 ) / r_0957__Keq_r_0957 ) / ( ( 1.0 + s_1411 / r_0957__kms_s_1411r_0957 ) * ( 1.0 + s_1521 / r_0957__kms_s_1521r_0957 ) + ( 1.0 + s_0622 / r_0957__kmp_s_0622r_0957 ) * ( 1.0 + s_1434_b / r_0957__kmp_s_1434_br_0957 ) * ( 1.0 + s_1517 / r_0957__kmp_s_1517r_0957 ) - 1.0 ) ) / intracellular '
	# ribonucleoside-triphosphate reductase (ATP)
	r_0959 = 'intracellular * r_0959__Vmax_r_0959 * ( pow ( 1.0 / r_0959__kms_s_0446r_0959 , 1.0 ) * pow ( 1.0 / r_0959__kms_s_1521r_0959 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_1521 , 1.0 ) - pow ( s_0566 , 1.0 ) * pow ( s_1434_b , 1.0 ) * pow ( s_1517 , 1.0 ) / r_0959__Keq_r_0959 ) / ( ( 1.0 + s_0446 / r_0959__kms_s_0446r_0959 ) * ( 1.0 + s_1521 / r_0959__kms_s_1521r_0959 ) + ( 1.0 + s_0566 / r_0959__kmp_s_0566r_0959 ) * ( 1.0 + s_1434_b / r_0959__kmp_s_1434_br_0959 ) * ( 1.0 + s_1517 / r_0959__kmp_s_1517r_0959 ) - 1.0 ) ) / intracellular '
	# thioredoxin reductase (NADPH)
	r_1024 = 'intracellular * r_1024__Vmax_r_1024 * ( pow ( 1.0 / r_1024__kms_s_0763_br_1024 , 1.0 ) * pow ( 1.0 / r_1024__kms_s_1096r_1024 , 1.0 ) * pow ( 1.0 / r_1024__kms_s_1517r_1024 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) * pow ( s_1517 , 1.0 ) - pow ( s_1091 , 1.0 ) * pow ( s_1521 , 1.0 ) / r_1024__Keq_r_1024 ) / ( ( 1.0 + s_0763_b / r_1024__kms_s_0763_br_1024 ) * ( 1.0 + s_1096 / r_1024__kms_s_1096r_1024 ) * ( 1.0 + s_1517 / r_1024__kms_s_1517r_1024 ) + ( 1.0 + s_1091 / r_1024__kmp_s_1091r_1024 ) * ( 1.0 + s_1521 / r_1024__kmp_s_1521r_1024 ) - 1.0 ) ) / intracellular '

	########### threonine biosynthesis ###########

	# aspartate kinase
	r_0233 = 'intracellular * r_0233__Vmax_r_0233 * ( pow ( 1.0 / r_0233__kms_s_0446r_0233 , 1.0 ) * pow ( 1.0 / r_0233__kms_s_0881r_0233 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_0881 , 1.0 ) - pow ( s_0301 , 1.0 ) * pow ( s_0400 , 1.0 ) / r_0233__Keq_r_0233 ) / ( ( 1.0 + s_0446 / r_0233__kms_s_0446r_0233 ) * ( 1.0 + s_0881 / r_0233__kms_s_0881r_0233 ) + ( 1.0 + s_0301 / r_0233__kmp_s_0301r_0233 ) * ( 1.0 + s_0400 / r_0233__kmp_s_0400r_0233 ) - 1.0 ) ) / intracellular '
	# aspartate-semialdehyde dehydrogenase
	r_0238 = 'intracellular * r_0238__Vmax_r_0238 * ( pow ( 1.0 / r_0238__kms_s_0301r_0238 , 1.0 ) * pow ( 1.0 / r_0238__kms_s_0763_br_0238 , 1.0 ) * pow ( 1.0 / r_0238__kms_s_1096r_0238 , 1.0 ) * ( pow ( s_0301 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) - pow ( s_0886 , 1.0 ) * pow ( s_1091 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0238__Keq_r_0238 ) / ( ( 1.0 + s_0301 / r_0238__kms_s_0301r_0238 ) * ( 1.0 + s_0763_b / r_0238__kms_s_0763_br_0238 ) * ( 1.0 + s_1096 / r_0238__kms_s_1096r_0238 ) + ( 1.0 + s_0886 / r_0238__kmp_s_0886r_0238 ) * ( 1.0 + s_1091 / r_0238__kmp_s_1091r_0238 ) * ( 1.0 + s_1207 / r_0238__kmp_s_1207r_0238 ) - 1.0 ) ) / intracellular '
	# homoserine dehydrogenase (NADH)
	r_0586 = 'intracellular * r_0586__Vmax_r_0586 * ( pow ( 1.0 / r_0586__kms_s_0763_br_0586 , 1.0 ) * pow ( 1.0 / r_0586__kms_s_0886r_0586 , 1.0 ) * pow ( 1.0 / r_0586__kms_s_1087r_0586 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_0886 , 1.0 ) * pow ( s_1087 , 1.0 ) - pow ( s_0919 , 1.0 ) * pow ( s_1082 , 1.0 ) / r_0586__Keq_r_0586 ) / ( ( 1.0 + s_0763_b / r_0586__kms_s_0763_br_0586 ) * ( 1.0 + s_0886 / r_0586__kms_s_0886r_0586 ) * ( 1.0 + s_1087 / r_0586__kms_s_1087r_0586 ) + ( 1.0 + s_0919 / r_0586__kmp_s_0919r_0586 ) * ( 1.0 + s_1082 / r_0586__kmp_s_1082r_0586 ) - 1.0 ) ) / intracellular '
	# homoserine kinase
	r_0588 = 'intracellular * r_0588__Vmax_r_0588 * ( pow ( 1.0 / r_0588__kms_s_0446r_0588 , 1.0 ) * pow ( 1.0 / r_0588__kms_s_0919r_0588 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_0919 , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1122 , 1.0 ) / r_0588__Keq_r_0588 ) / ( ( 1.0 + s_0446 / r_0588__kms_s_0446r_0588 ) * ( 1.0 + s_0919 / r_0588__kms_s_0919r_0588 ) + ( 1.0 + s_0400 / r_0588__kmp_s_0400r_0588 ) * ( 1.0 + s_0763_b / r_0588__kmp_s_0763_br_0588 ) * ( 1.0 + s_1122 / r_0588__kmp_s_1122r_0588 ) - 1.0 ) ) / intracellular '
	# threonine synthase
	r_1027 = 'intracellular * r_1027__Vmax_r_1027 * ( pow ( 1.0 / r_1027__kms_s_1122r_1027 , 1.0 ) * pow ( 1.0 / r_1027__kms_s_1434_br_1027 , 1.0 ) * ( pow ( s_1122 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0949 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_1027__Keq_r_1027 ) / ( ( 1.0 + s_1122 / r_1027__kms_s_1122r_1027 ) * ( 1.0 + s_1434_b / r_1027__kms_s_1434_br_1027 ) + ( 1.0 + s_0949 / r_1027__kmp_s_0949r_1027 ) * ( 1.0 + s_1207 / r_1027__kmp_s_1207r_1027 ) - 1.0 ) ) / intracellular '

	########### threonine catabolism ###########

	# cystathionine g-lyase
	r_0339 = 'intracellular * r_0339__Vmax_r_0339 * ( pow ( 1.0 / r_0339__kms_s_0888r_0339 , 1.0 ) * pow ( 1.0 / r_0339__kms_s_1434_br_0339 , 1.0 ) * ( pow ( s_0888 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0183 , 1.0 ) * pow ( s_0430 , 1.0 ) * pow ( s_0889 , 1.0 ) / r_0339__Keq_r_0339 ) / ( ( 1.0 + s_0888 / r_0339__kms_s_0888r_0339 ) * ( 1.0 + s_1434_b / r_0339__kms_s_1434_br_0339 ) + ( 1.0 + s_0183 / r_0339__kmp_s_0183r_0339 ) * ( 1.0 + s_0430 / r_0339__kmp_s_0430r_0339 ) * ( 1.0 + s_0889 / r_0339__kmp_s_0889r_0339 ) - 1.0 ) ) / intracellular '
	# L-threonine deaminase
	r_0667 = 'intracellular * r_0667__Vmax_r_0667 * ( pow ( 1.0 / r_0667__kms_s_0949r_0667 , 1.0 ) * ( pow ( s_0949 , 1.0 ) - pow ( s_0183 , 1.0 ) * pow ( s_0430 , 1.0 ) / r_0667__Keq_r_0667 ) / ( 1.0 + s_0949 / r_0667__kms_s_0949r_0667 + ( 1.0 + s_0183 / r_0667__kmp_s_0183r_0667 ) * ( 1.0 + s_0430 / r_0667__kmp_s_0430r_0667 ) - 1.0 ) ) / intracellular '

	########### trehalose biosynthesis ###########

	# alpha,alpha-trehalose-phosphate synthase (UDP-forming)
	r_0213 = 'intracellular * r_0213__Vmax_r_0213 * ( pow ( 1.0 / r_0213__kms_s_0410r_0213 , 1.0 ) * pow ( 1.0 / r_0213__kms_s_1415r_0213 , 1.0 ) * ( pow ( s_0410 , 1.0 ) * pow ( s_1415 , 1.0 ) - pow ( s_0419 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1411 , 1.0 ) / r_0213__Keq_r_0213 ) / ( ( 1.0 + s_0410 / r_0213__kms_s_0410r_0213 ) * ( 1.0 + s_1415 / r_0213__kms_s_1415r_0213 ) + ( 1.0 + s_0419 / r_0213__kmp_s_0419r_0213 ) * ( 1.0 + s_0763_b / r_0213__kmp_s_0763_br_0213 ) * ( 1.0 + s_1411 / r_0213__kmp_s_1411r_0213 ) - 1.0 ) ) / intracellular '
	# trehalose-phosphatase
	r_1038 = 'intracellular * r_1038__Vmax_r_1038 * ( pow ( 1.0 / r_1038__kms_s_0419r_1038 , 1.0 ) * pow ( 1.0 / r_1038__kms_s_1434_br_1038 , 1.0 ) * ( pow ( s_0419 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0416 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_1038__Keq_r_1038 ) / ( ( 1.0 + s_0419 / r_1038__kms_s_0419r_1038 ) * ( 1.0 + s_1434_b / r_1038__kms_s_1434_br_1038 ) + ( 1.0 + s_0416 / r_1038__kmp_s_0416r_1038 ) * ( 1.0 + s_1207 / r_1038__kmp_s_1207r_1038 ) - 1.0 ) ) / intracellular '

	########### triglyceride biosynthesis ###########

	# diacylglycerol acyltransferase
	r_0370 = 'intracellular * r_0370__Vmax_r_0370 * ( pow ( 1.0 / r_0370__kms_s_0386r_0370 , 1.0 ) * pow ( 1.0 / r_0370__kms_s_0596r_0370 , 1.0 ) * ( pow ( s_0386 , 1.0 ) * pow ( s_0596 , 1.0 ) - pow ( s_0514 , 1.0 ) * pow ( s_0763_b , 4.0 ) * pow ( s_1399 , 1.0 ) / r_0370__Keq_r_0370 ) / ( ( 1.0 + s_0386 / r_0370__kms_s_0386r_0370 ) * ( 1.0 + s_0596 / r_0370__kms_s_0596r_0370 ) + ( 1.0 + s_0514 / r_0370__kmp_s_0514r_0370 ) * ( 1.0 + s_0763_b / r_0370__kmp_s_0763_br_0370 ) * ( 1.0 + s_1399 / r_0370__kmp_s_1399r_0370 ) - 1.0 ) ) / intracellular '
	# glycerol-3-phosphate/dihydroxyacetone phosphate acyltransferase
	r_0534 = 'intracellular * r_0534__Vmax_r_0534 * ( pow ( 1.0 / r_0534__kms_s_0386r_0534 , 1.0 ) * pow ( 1.0 / r_0534__kms_s_1315r_0534 , 1.0 ) * ( pow ( s_0386 , 1.0 ) * pow ( s_1315 , 1.0 ) - pow ( s_0083 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_0763_b , 2.0 ) / r_0534__Keq_r_0534 ) / ( ( 1.0 + s_0386 / r_0534__kms_s_0386r_0534 ) * ( 1.0 + s_1315 / r_0534__kms_s_1315r_0534 ) + ( 1.0 + s_0083 / r_0534__kmp_s_0083r_0534 ) * ( 1.0 + s_0514 / r_0534__kmp_s_0514r_0534 ) * ( 1.0 + s_0763_b / r_0534__kmp_s_0763_br_0534 ) - 1.0 ) ) / intracellular '

	########### tryptophan biosynthesis ###########

	# anthranilate phosphoribosyltransferase
	r_0220 = 'intracellular * r_0220__Vmax_r_0220 * ( pow ( 1.0 / r_0220__kms_s_0331r_0220 , 1.0 ) * pow ( 1.0 / r_0220__kms_s_0439r_0220 , 1.0 ) * ( pow ( s_0331 , 1.0 ) * pow ( s_0439 , 1.0 ) - pow ( s_0605 , 1.0 ) * pow ( s_1066 , 1.0 ) / r_0220__Keq_r_0220 ) / ( ( 1.0 + s_0331 / r_0220__kms_s_0331r_0220 ) * ( 1.0 + s_0439 / r_0220__kms_s_0439r_0220 ) + ( 1.0 + s_0605 / r_0220__kmp_s_0605r_0220 ) * ( 1.0 + s_1066 / r_0220__kmp_s_1066r_0220 ) - 1.0 ) ) / intracellular '
	# anthranilate synthase
	r_0221 = 'intracellular * r_0221__Vmax_r_0221 * ( pow ( 1.0 / r_0221__kms_s_0500r_0221 , 1.0 ) * pow ( 1.0 / r_0221__kms_s_0907r_0221 , 1.0 ) * ( pow ( s_0500 , 1.0 ) * pow ( s_0907 , 1.0 ) - pow ( s_0439 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_0899 , 1.0 ) * pow ( s_1277 , 1.0 ) / r_0221__Keq_r_0221 ) / ( ( 1.0 + s_0500 / r_0221__kms_s_0500r_0221 ) * ( 1.0 + s_0907 / r_0221__kms_s_0907r_0221 ) + ( 1.0 + s_0439 / r_0221__kmp_s_0439r_0221 ) * ( 1.0 + s_0763_b / r_0221__kmp_s_0763_br_0221 ) * ( 1.0 + s_0899 / r_0221__kmp_s_0899r_0221 ) * ( 1.0 + s_1277 / r_0221__kmp_s_1277r_0221 ) - 1.0 ) ) / intracellular '
	# indole-3-glycerol-phosphate synthase
	r_0608 = 'intracellular * r_0608__Vmax_r_0608 * ( pow ( 1.0 / r_0608__kms_s_0078r_0608 , 1.0 ) * pow ( 1.0 / r_0608__kms_s_0763_br_0608 , 1.0 ) * ( pow ( s_0078 , 1.0 ) * pow ( s_0763_b , 1.0 ) - pow ( s_0088 , 1.0 ) * pow ( s_0470 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0608__Keq_r_0608 ) / ( ( 1.0 + s_0078 / r_0608__kms_s_0078r_0608 ) * ( 1.0 + s_0763_b / r_0608__kms_s_0763_br_0608 ) + ( 1.0 + s_0088 / r_0608__kmp_s_0088r_0608 ) * ( 1.0 + s_0470 / r_0608__kmp_s_0470r_0608 ) * ( 1.0 + s_1434_b / r_0608__kmp_s_1434_br_0608 ) - 1.0 ) ) / intracellular '
	# phosphoribosylanthranilate isomerase
	r_0887 = 'intracellular * r_0887__Vmax_r_0887 * ( pow ( 1.0 / r_0887__kms_s_1066r_0887 , 1.0 ) * ( pow ( s_1066 , 1.0 ) - pow ( s_0078 , 1.0 ) / r_0887__Keq_r_0887 ) / ( 1.0 + s_1066 / r_0887__kms_s_1066r_0887 + 1.0 + s_0078 / r_0887__kmp_s_0078r_0887 - 1.0 ) ) / intracellular '
	# tryptophan synthase (indoleglycerol phosphate)
	r_1042 = 'intracellular * r_1042__Vmax_r_1042 * ( pow ( 1.0 / r_1042__kms_s_0088r_1042 , 1.0 ) * pow ( 1.0 / r_1042__kms_s_0943r_1042 , 1.0 ) * ( pow ( s_0088 , 1.0 ) * pow ( s_0943 , 1.0 ) - pow ( s_0731 , 1.0 ) * pow ( s_0952 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_1042__Keq_r_1042 ) / ( ( 1.0 + s_0088 / r_1042__kms_s_0088r_1042 ) * ( 1.0 + s_0943 / r_1042__kms_s_0943r_1042 ) + ( 1.0 + s_0731 / r_1042__kmp_s_0731r_1042 ) * ( 1.0 + s_0952 / r_1042__kmp_s_0952r_1042 ) * ( 1.0 + s_1434_b / r_1042__kmp_s_1434_br_1042 ) - 1.0 ) ) / intracellular '

	########### tyrosine biosynthesis ###########

	# prephenate dehydrogenase (NADP)
	r_0913 = 'intracellular * r_0913__Vmax_r_0913 * ( pow ( 1.0 / r_0913__kms_s_1091r_0913 , 1.0 ) * pow ( 1.0 / r_0913__kms_s_1258r_0913 , 1.0 ) * ( pow ( s_1091 , 1.0 ) * pow ( s_1258 , 1.0 ) - pow ( s_0209 , 1.0 ) * pow ( s_0470 , 1.0 ) * pow ( s_1096 , 1.0 ) / r_0913__Keq_r_0913 ) / ( ( 1.0 + s_1091 / r_0913__kms_s_1091r_0913 ) * ( 1.0 + s_1258 / r_0913__kms_s_1258r_0913 ) + ( 1.0 + s_0209 / r_0913__kmp_s_0209r_0913 ) * ( 1.0 + s_0470 / r_0913__kmp_s_0470r_0913 ) * ( 1.0 + s_1096 / r_0913__kmp_s_1096r_0913 ) - 1.0 ) ) / intracellular '

	########### valine biosynthesis ###########

	# 2-aceto-2-hydroxybutanoate synthase
	r_0016 = 'intracellular * r_0016__Vmax_r_0016 * ( pow ( 1.0 / r_0016__kms_s_0183r_0016 , 1.0 ) * pow ( 1.0 / r_0016__kms_s_0763_br_0016 , 1.0 ) * pow ( 1.0 / r_0016__kms_s_1277r_0016 , 1.0 ) * ( pow ( s_0183 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1277 , 1.0 ) - pow ( s_0042 , 1.0 ) * pow ( s_0470 , 1.0 ) / r_0016__Keq_r_0016 ) / ( ( 1.0 + s_0183 / r_0016__kms_s_0183r_0016 ) * ( 1.0 + s_0763_b / r_0016__kms_s_0763_br_0016 ) * ( 1.0 + s_1277 / r_0016__kms_s_1277r_0016 ) + ( 1.0 + s_0042 / r_0016__kmp_s_0042r_0016 ) * ( 1.0 + s_0470 / r_0016__kmp_s_0470r_0016 ) - 1.0 ) ) / intracellular '
	# 2-oxo-4-methyl-3-carboxypentanoate decarboxylation
	r_0031 = 'intracellular * r_0031__Vmax_r_0031 * ( pow ( 1.0 / r_0031__kms_s_0010r_0031 , 1.0 ) * pow ( 1.0 / r_0031__kms_s_0763_br_0031 , 1.0 ) * ( pow ( s_0010 , 1.0 ) * pow ( s_0763_b , 1.0 ) - pow ( s_0297 , 1.0 ) * pow ( s_0470 , 1.0 ) / r_0031__Keq_r_0031 ) / ( ( 1.0 + s_0010 / r_0031__kms_s_0010r_0031 ) * ( 1.0 + s_0763_b / r_0031__kms_s_0763_br_0031 ) + ( 1.0 + s_0297 / r_0031__kmp_s_0297r_0031 ) * ( 1.0 + s_0470 / r_0031__kmp_s_0470r_0031 ) - 1.0 ) ) / intracellular '
	# acetohydroxy acid isomeroreductase
	r_0111 = 'intracellular * r_0111__Vmax_r_0111 * ( pow ( 1.0 / r_0111__kms_s_0150r_0111 , 1.0 ) * pow ( 1.0 / r_0111__kms_s_0763_br_0111 , 1.0 ) * pow ( 1.0 / r_0111__kms_s_1096r_0111 , 1.0 ) * ( pow ( s_0150 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) - pow ( s_0018 , 1.0 ) * pow ( s_1091 , 1.0 ) / r_0111__Keq_r_0111 ) / ( ( 1.0 + s_0150 / r_0111__kms_s_0150r_0111 ) * ( 1.0 + s_0763_b / r_0111__kms_s_0763_br_0111 ) * ( 1.0 + s_1096 / r_0111__kms_s_1096r_0111 ) + ( 1.0 + s_0018 / r_0111__kmp_s_0018r_0111 ) * ( 1.0 + s_1091 / r_0111__kmp_s_1091r_0111 ) - 1.0 ) ) / intracellular '
	# acetolactate synthase
	r_0112 = 'intracellular * r_0112__Vmax_r_0112 * ( pow ( 1.0 / r_0112__kms_s_0763_br_0112 , 1.0 ) * pow ( 1.0 / r_0112__kms_s_1277r_0112 , 2.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_1277 , 2.0 ) - pow ( s_0150 , 1.0 ) * pow ( s_0470 , 1.0 ) / r_0112__Keq_r_0112 ) / ( ( 1.0 + s_0763_b / r_0112__kms_s_0763_br_0112 ) * ( 1.0 + s_1277 / r_0112__kms_s_1277r_0112 ) + ( 1.0 + s_0150 / r_0112__kmp_s_0150r_0112 ) * ( 1.0 + s_0470 / r_0112__kmp_s_0470r_0112 ) - 1.0 ) ) / intracellular '
	# dihydroxy-acid dehydratase (2,3-dihydroxy-3-methylbutanoate)
	r_0384 = 'intracellular * r_0384__Vmax_r_0384 * ( pow ( 1.0 / r_0384__kms_s_0018r_0384 , 1.0 ) * ( pow ( s_0018 , 1.0 ) - pow ( s_0238 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0384__Keq_r_0384 ) / ( 1.0 + s_0018 / r_0384__kms_s_0018r_0384 + ( 1.0 + s_0238 / r_0384__kmp_s_0238r_0384 ) * ( 1.0 + s_1434_b / r_0384__kmp_s_1434_br_0384 ) - 1.0 ) ) / intracellular '
	# dihydroxy-acid dehydratase (2,3-dihydroxy-3-methylpentanoate)
	r_0385 = 'intracellular * r_0385__Vmax_r_0385 * ( pow ( 1.0 / r_0385__kms_s_0007r_0385 , 1.0 ) * ( pow ( s_0007 , 1.0 ) - pow ( s_0058 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0385__Keq_r_0385 ) / ( 1.0 + s_0007 / r_0385__kms_s_0007r_0385 + ( 1.0 + s_0058 / r_0385__kmp_s_0058r_0385 ) * ( 1.0 + s_1434_b / r_0385__kmp_s_1434_br_0385 ) - 1.0 ) ) / intracellular '
	# isoleucine transaminase
	r_0634 = 'intracellular * r_0634__Vmax_r_0634 * ( pow ( 1.0 / r_0634__kms_s_0058r_0634 , 1.0 ) * pow ( 1.0 / r_0634__kms_s_0899r_0634 , 1.0 ) * ( pow ( s_0058 , 1.0 ) * pow ( s_0899 , 1.0 ) - pow ( s_0185 , 1.0 ) * pow ( s_0920 , 1.0 ) / r_0634__Keq_r_0634 ) / ( ( 1.0 + s_0058 / r_0634__kms_s_0058r_0634 ) * ( 1.0 + s_0899 / r_0634__kms_s_0899r_0634 ) + ( 1.0 + s_0185 / r_0634__kmp_s_0185r_0634 ) * ( 1.0 + s_0920 / r_0634__kmp_s_0920r_0634 ) - 1.0 ) ) / intracellular '
	# ketol-acid reductoisomerase (2-aceto-2-hydroxybutanoate)
	r_0640 = 'intracellular * r_0640__Vmax_r_0640 * ( pow ( 1.0 / r_0640__kms_s_0042r_0640 , 1.0 ) * pow ( 1.0 / r_0640__kms_s_0763_br_0640 , 1.0 ) * pow ( 1.0 / r_0640__kms_s_1096r_0640 , 1.0 ) * ( pow ( s_0042 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) - pow ( s_0007 , 1.0 ) * pow ( s_1091 , 1.0 ) / r_0640__Keq_r_0640 ) / ( ( 1.0 + s_0042 / r_0640__kms_s_0042r_0640 ) * ( 1.0 + s_0763_b / r_0640__kms_s_0763_br_0640 ) * ( 1.0 + s_1096 / r_0640__kms_s_1096r_0640 ) + ( 1.0 + s_0007 / r_0640__kmp_s_0007r_0640 ) * ( 1.0 + s_1091 / r_0640__kmp_s_1091r_0640 ) - 1.0 ) ) / intracellular '
	# leucine transaminase
	r_0674 = 'intracellular * r_0674__Vmax_r_0674 * ( pow ( 1.0 / r_0674__kms_s_0297r_0674 , 1.0 ) * pow ( 1.0 / r_0674__kms_s_0899r_0674 , 1.0 ) * ( pow ( s_0297 , 1.0 ) * pow ( s_0899 , 1.0 ) - pow ( s_0185 , 1.0 ) * pow ( s_0925 , 1.0 ) / r_0674__Keq_r_0674 ) / ( ( 1.0 + s_0297 / r_0674__kms_s_0297r_0674 ) * ( 1.0 + s_0899 / r_0674__kms_s_0899r_0674 ) + ( 1.0 + s_0185 / r_0674__kmp_s_0185r_0674 ) * ( 1.0 + s_0925 / r_0674__kmp_s_0925r_0674 ) - 1.0 ) ) / intracellular '
	# valine transaminase
	r_1073 = 'intracellular * r_1073__Vmax_r_1073 * ( pow ( 1.0 / r_1073__kms_s_0238r_1073 , 1.0 ) * pow ( 1.0 / r_1073__kms_s_0899r_1073 , 1.0 ) * ( pow ( s_0238 , 1.0 ) * pow ( s_0899 , 1.0 ) - pow ( s_0185 , 1.0 ) * pow ( s_0960 , 1.0 ) / r_1073__Keq_r_1073 ) / ( ( 1.0 + s_0238 / r_1073__kms_s_0238r_1073 ) * ( 1.0 + s_0899 / r_1073__kms_s_0899r_1073 ) + ( 1.0 + s_0185 / r_1073__kmp_s_0185r_1073 ) * ( 1.0 + s_0960 / r_1073__kmp_s_0960r_1073 ) - 1.0 ) ) / intracellular '

	########### very long chain fatty acid biosynthesis ###########

	# fatty acid synthase (n-C24:0), lumped reaction
	r_0425 = 'intracellular * r_0425__Vmax_r_0425 * ( pow ( 1.0 / r_0425__kms_s_0763_br_0425 , 9.0 ) * pow ( 1.0 / r_0425__kms_s_1005r_0425 , 3.0 ) * pow ( 1.0 / r_0425__kms_s_1096r_0425 , 6.0 ) * pow ( 1.0 / r_0425__kms_s_1329r_0425 , 1.0 ) * ( pow ( s_0763_b , 9.0 ) * pow ( s_1005 , 3.0 ) * pow ( s_1096 , 6.0 ) * pow ( s_1329 , 1.0 ) - pow ( s_0470 , 3.0 ) * pow ( s_0514 , 3.0 ) * pow ( s_0987 , 1.0 ) * pow ( s_1091 , 6.0 ) * pow ( s_1434_b , 3.0 ) / r_0425__Keq_r_0425 ) / ( ( 1.0 + s_0763_b / r_0425__kms_s_0763_br_0425 ) * ( 1.0 + s_1005 / r_0425__kms_s_1005r_0425 ) * ( 1.0 + s_1096 / r_0425__kms_s_1096r_0425 ) * ( 1.0 + s_1329 / r_0425__kms_s_1329r_0425 ) + ( 1.0 + s_0470 / r_0425__kmp_s_0470r_0425 ) * ( 1.0 + s_0514 / r_0425__kmp_s_0514r_0425 ) * ( 1.0 + s_0987 / r_0425__kmp_s_0987r_0425 ) * ( 1.0 + s_1091 / r_0425__kmp_s_1091r_0425 ) * ( 1.0 + s_1434_b / r_0425__kmp_s_1434_br_0425 ) - 1.0 ) ) / intracellular '
	# microsomal beta-keto-reductase
	r_0719 = 'intracellular * r_0719__Vmax_r_0719 * ( pow ( 1.0 / r_0719__kms_s_0046r_0719 , 1.0 ) * pow ( 1.0 / r_0719__kms_s_1091r_0719 , 1.0 ) * ( pow ( s_0046 , 1.0 ) * pow ( s_1091 , 1.0 ) - pow ( s_0247 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) / r_0719__Keq_r_0719 ) / ( ( 1.0 + s_0046 / r_0719__kms_s_0046r_0719 ) * ( 1.0 + s_1091 / r_0719__kms_s_1091r_0719 ) + ( 1.0 + s_0247 / r_0719__kmp_s_0247r_0719 ) * ( 1.0 + s_0763_b / r_0719__kmp_s_0763_br_0719 ) * ( 1.0 + s_1096 / r_0719__kmp_s_1096r_0719 ) - 1.0 ) ) / intracellular '
	# microsomal beta-keto-reductase_2
	r_0720 = 'intracellular * r_0720__Vmax_r_0720 * ( pow ( 1.0 / r_0720__kms_s_0052r_0720 , 1.0 ) * pow ( 1.0 / r_0720__kms_s_1091r_0720 , 1.0 ) * ( pow ( s_0052 , 1.0 ) * pow ( s_1091 , 1.0 ) - pow ( s_0257 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) / r_0720__Keq_r_0720 ) / ( ( 1.0 + s_0052 / r_0720__kms_s_0052r_0720 ) * ( 1.0 + s_1091 / r_0720__kms_s_1091r_0720 ) + ( 1.0 + s_0257 / r_0720__kmp_s_0257r_0720 ) * ( 1.0 + s_0763_b / r_0720__kmp_s_0763_br_0720 ) * ( 1.0 + s_1096 / r_0720__kmp_s_1096r_0720 ) - 1.0 ) ) / intracellular '
	# microsomal beta-keto-reductase_3
	r_0721 = 'intracellular * r_0721__Vmax_r_0721 * ( pow ( 1.0 / r_0721__kms_s_0234r_0721 , 1.0 ) * pow ( 1.0 / r_0721__kms_s_1091r_0721 , 1.0 ) * ( pow ( s_0234 , 1.0 ) * pow ( s_1091 , 1.0 ) - pow ( s_0254 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) / r_0721__Keq_r_0721 ) / ( ( 1.0 + s_0234 / r_0721__kms_s_0234r_0721 ) * ( 1.0 + s_1091 / r_0721__kms_s_1091r_0721 ) + ( 1.0 + s_0254 / r_0721__kmp_s_0254r_0721 ) * ( 1.0 + s_0763_b / r_0721__kmp_s_0763_br_0721 ) * ( 1.0 + s_1096 / r_0721__kmp_s_1096r_0721 ) - 1.0 ) ) / intracellular '
	# microsomal beta-keto-reductase_4
	r_0722 = 'intracellular * r_0722__Vmax_r_0722 * ( pow ( 1.0 / r_0722__kms_s_0055r_0722 , 1.0 ) * pow ( 1.0 / r_0722__kms_s_1091r_0722 , 1.0 ) * ( pow ( s_0055 , 1.0 ) * pow ( s_1091 , 1.0 ) - pow ( s_0261 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) / r_0722__Keq_r_0722 ) / ( ( 1.0 + s_0055 / r_0722__kms_s_0055r_0722 ) * ( 1.0 + s_1091 / r_0722__kms_s_1091r_0722 ) + ( 1.0 + s_0261 / r_0722__kmp_s_0261r_0722 ) * ( 1.0 + s_0763_b / r_0722__kmp_s_0763_br_0722 ) * ( 1.0 + s_1096 / r_0722__kmp_s_1096r_0722 ) - 1.0 ) ) / intracellular '


	### reactions without pathway annotation

	# diacylglycerol pyrophosphate phosphatase
	r_0371 = 'intracellular * r_0371__Vmax_r_0371 * ( pow ( 1.0 / r_0371__kms_s_1215r_0371 , 1.0 ) * pow ( 1.0 / r_0371__kms_s_1434_br_0371 , 1.0 ) * ( pow ( s_1215 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0596 , 1.0 ) * pow ( s_0763_b , 2.0 ) * pow ( s_1207 , 1.0 ) / r_0371__Keq_r_0371 ) / ( ( 1.0 + s_1215 / r_0371__kms_s_1215r_0371 ) * ( 1.0 + s_1434_b / r_0371__kms_s_1434_br_0371 ) + ( 1.0 + s_0596 / r_0371__kmp_s_0596r_0371 ) * ( 1.0 + s_0763_b / r_0371__kmp_s_0763_br_0371 ) * ( 1.0 + s_1207 / r_0371__kmp_s_1207r_0371 ) - 1.0 ) ) / intracellular '
	# ATP synthase
	r_0246 = 'intracellular * r_0246__Vmax_r_0246 * ( pow ( 1.0 / r_0246__kms_s_0400r_0246 , 1.0 ) * pow ( 1.0 / r_0246__kms_s_0763_br_0246 , 3.0 ) * pow ( 1.0 / r_0246__kms_s_1207r_0246 , 1.0 ) * ( pow ( s_0400 , 1.0 ) * pow ( s_0763_b , 3.0 ) * pow ( s_1207 , 1.0 ) - pow ( s_0446 , 1.0 ) * pow ( s_0763_b , 2.0 ) * pow ( s_1434_b , 1.0 ) / r_0246__Keq_r_0246 ) / ( ( 1.0 + s_0400 / r_0246__kms_s_0400r_0246 ) * ( 1.0 + s_0763_b / r_0246__kms_s_0763_br_0246 ) * ( 1.0 + s_1207 / r_0246__kms_s_1207r_0246 ) + ( 1.0 + s_0446 / r_0246__kmp_s_0446r_0246 ) * ( 1.0 + s_0763_b / r_0246__kmp_s_0763_br_0246 ) * ( 1.0 + s_1434_b / r_0246__kmp_s_1434_br_0246 ) - 1.0 ) ) / intracellular '
	# ATPase, cytosolic
	r_0249 = 'r_0249__Vmax_r_0249 * ( pow ( 1.0 / r_0249__kms_s_0446r_0249 , 1.0 ) * pow ( 1.0 / r_0249__kms_s_1434_br_0249 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_0766_b , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0249__Keq_r_0249 ) / ( ( 1.0 + s_0446 / r_0249__kms_s_0446r_0249 ) * ( 1.0 + s_1434_b / r_0249__kms_s_1434_br_0249 ) + ( 1.0 + s_0400 / r_0249__kmp_s_0400r_0249 ) * ( 1.0 + s_0766_b / r_0249__kmp_s_0766_br_0249 ) * ( 1.0 + s_1207 / r_0249__kmp_s_1207r_0249 ) - 1.0 ) ) '
	# sulfate adenylyltransferase (ADP)
	r_1007 = 'intracellular * r_1007__Vmax_r_1007 * ( pow ( 1.0 / r_1007__kms_s_0400r_1007 , 1.0 ) * pow ( 1.0 / r_1007__kms_s_0763_br_1007 , 1.0 ) * pow ( 1.0 / r_1007__kms_s_1347r_1007 , 1.0 ) * ( pow ( s_0400 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1347 , 1.0 ) - pow ( s_0304 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_1007__Keq_r_1007 ) / ( ( 1.0 + s_0400 / r_1007__kms_s_0400r_1007 ) * ( 1.0 + s_0763_b / r_1007__kms_s_0763_br_1007 ) * ( 1.0 + s_1347 / r_1007__kms_s_1347r_1007 ) + ( 1.0 + s_0304 / r_1007__kmp_s_0304r_1007 ) * ( 1.0 + s_1207 / r_1007__kmp_s_1207r_1007 ) - 1.0 ) ) / intracellular '
	# CO2 transport
	r_1194 = 'r_1194__Vmax_r_1194 * ( pow ( 1.0 / r_1194__kms_s_0470r_1194 , 1.0 ) * ( pow ( s_0470 , 1.0 ) - pow ( s_0472_b , 1.0 ) / r_1194__Keq_r_1194 ) / ( 1.0 + s_0470 / r_1194__kms_s_0470r_1194 + 1.0 + s_0472_b / r_1194__kmp_s_0472_br_1194 - 1.0 ) ) '
	# cytochrome P450 lanosterol 14-alpha-demethylase (NAD)
	r_0347 = 'intracellular * r_0347__Vmax_r_0347 * ( pow ( 1.0 / r_0347__kms_s_0763_br_0347 , 2.0 ) * pow ( 1.0 / r_0347__kms_s_0963r_0347 , 1.0 ) * pow ( 1.0 / r_0347__kms_s_1087r_0347 , 3.0 ) * pow ( 1.0 / r_0347__kms_s_1160r_0347 , 3.0 ) * ( pow ( s_0763_b , 2.0 ) * pow ( s_0963 , 1.0 ) * pow ( s_1087 , 3.0 ) * pow ( s_1160 , 3.0 ) - pow ( s_0268 , 1.0 ) * pow ( s_0689 , 1.0 ) * pow ( s_1082 , 3.0 ) * pow ( s_1434_b , 4.0 ) / r_0347__Keq_r_0347 ) / ( ( 1.0 + s_0763_b / r_0347__kms_s_0763_br_0347 ) * ( 1.0 + s_0963 / r_0347__kms_s_0963r_0347 ) * ( 1.0 + s_1087 / r_0347__kms_s_1087r_0347 ) * ( 1.0 + s_1160 / r_0347__kms_s_1160r_0347 ) + ( 1.0 + s_0268 / r_0347__kmp_s_0268r_0347 ) * ( 1.0 + s_0689 / r_0347__kmp_s_0689r_0347 ) * ( 1.0 + s_1082 / r_0347__kmp_s_1082r_0347 ) * ( 1.0 + s_1434_b / r_0347__kmp_s_1434_br_0347 ) - 1.0 ) ) / intracellular '
	# triacylglycerol lipase
	r_1040 = 'intracellular * r_1040__Vmax_r_1040 * ( pow ( 1.0 / r_1040__kms_s_1399r_1040 , 1.0 ) * pow ( 1.0 / r_1040__kms_s_1434_br_1040 , 1.0 ) * ( pow ( s_1399 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0596 , 1.0 ) * pow ( s_0663 , 1.0 ) / r_1040__Keq_r_1040 ) / ( ( 1.0 + s_1399 / r_1040__kms_s_1399r_1040 ) * ( 1.0 + s_1434_b / r_1040__kms_s_1434_br_1040 ) + ( 1.0 + s_0596 / r_1040__kmp_s_0596r_1040 ) * ( 1.0 + s_0663 / r_1040__kmp_s_0663r_1040 ) - 1.0 ) ) / intracellular '
	# isa acyl-CoA
	r_1672 = 'intracellular * r_1672__Vmax_r_1672 * ( pow ( 1.0 / r_1672__kms_s_1342r_1672 , 1.0 ) * ( pow ( s_1342 , 1.0 ) - pow ( s_0386 , 1.0 ) / r_1672__Keq_r_1672 ) / ( 1.0 + s_1342 / r_1672__kms_s_1342r_1672 + 1.0 + s_0386 / r_1672__kmp_s_0386r_1672 - 1.0 ) ) / intracellular '
	# phosphoribosylaminoimidazole synthase
	r_0884 = 'intracellular * r_0884__Vmax_r_0884 * ( pow ( 1.0 / r_0884__kms_s_0158r_0884 , 1.0 ) * pow ( 1.0 / r_0884__kms_s_0446r_0884 , 1.0 ) * ( pow ( s_0158 , 1.0 ) * pow ( s_0446 , 1.0 ) - pow ( s_0316 , 1.0 ) * pow ( s_0400 , 1.0 ) * pow ( s_0763_b , 2.0 ) * pow ( s_1207 , 1.0 ) / r_0884__Keq_r_0884 ) / ( ( 1.0 + s_0158 / r_0884__kms_s_0158r_0884 ) * ( 1.0 + s_0446 / r_0884__kms_s_0446r_0884 ) + ( 1.0 + s_0316 / r_0884__kmp_s_0316r_0884 ) * ( 1.0 + s_0400 / r_0884__kmp_s_0400r_0884 ) * ( 1.0 + s_0763_b / r_0884__kmp_s_0763_br_0884 ) * ( 1.0 + s_1207 / r_0884__kmp_s_1207r_0884 ) - 1.0 ) ) / intracellular '
	# sulfate uniport
	r_1507 = 'r_1507__Vmax_r_1507 * ( pow ( 1.0 / r_1507__kms_s_1348_br_1507 , 1.0 ) * ( pow ( s_1348_b , 1.0 ) - pow ( s_1347 , 1.0 ) / r_1507__Keq_r_1507 ) / ( 1.0 + s_1348_b / r_1507__kms_s_1348_br_1507 + 1.0 + s_1347 / r_1507__kmp_s_1347r_1507 - 1.0 ) ) '
	# dCMP deaminase
	r_0357 = 'intracellular * r_0357__Vmax_r_0357 * ( pow ( 1.0 / r_0357__kms_s_0430r_0357 , 1.0 ) * pow ( 1.0 / r_0357__kms_s_0624r_0357 , 1.0 ) * ( pow ( s_0430 , 1.0 ) * pow ( s_0624 , 1.0 ) - pow ( s_0569 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0357__Keq_r_0357 ) / ( ( 1.0 + s_0430 / r_0357__kms_s_0430r_0357 ) * ( 1.0 + s_0624 / r_0357__kms_s_0624r_0357 ) + ( 1.0 + s_0569 / r_0357__kmp_s_0569r_0357 ) * ( 1.0 + s_0763_b / r_0357__kmp_s_0763_br_0357 ) * ( 1.0 + s_1434_b / r_0357__kmp_s_1434_br_0357 ) - 1.0 ) ) / intracellular '
	# cholestenol delta-isomerase, lumped reaction
	r_0298 = 'intracellular * r_0298__Vmax_r_0298 * ( pow ( 1.0 / r_0298__kms_s_1160r_0298 , 1.0 ) * pow ( 1.0 / r_0298__kms_s_1293r_0298 , 1.0 ) * pow ( 1.0 / r_0298__kms_s_1447r_0298 , 1.0 ) * ( pow ( s_1160 , 1.0 ) * pow ( s_1293 , 1.0 ) * pow ( s_1447 , 1.0 ) - pow ( s_0632 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1290 , 1.0 ) * pow ( s_1434_b , 2.0 ) / r_0298__Keq_r_0298 ) / ( ( 1.0 + s_1160 / r_0298__kms_s_1160r_0298 ) * ( 1.0 + s_1293 / r_0298__kms_s_1293r_0298 ) * ( 1.0 + s_1447 / r_0298__kms_s_1447r_0298 ) + ( 1.0 + s_0632 / r_0298__kmp_s_0632r_0298 ) * ( 1.0 + s_0763_b / r_0298__kmp_s_0763_br_0298 ) * ( 1.0 + s_1290 / r_0298__kmp_s_1290r_0298 ) * ( 1.0 + s_1434_b / r_0298__kmp_s_1434_br_0298 ) - 1.0 ) ) / intracellular '
	# acetyl-CoA hydrolase
	r_0125 = 'intracellular * r_0125__Vmax_r_0125 * ( pow ( 1.0 / r_0125__kms_s_0369r_0125 , 1.0 ) * pow ( 1.0 / r_0125__kms_s_0514r_0125 , 1.0 ) * pow ( 1.0 / r_0125__kms_s_0763_br_0125 , 1.0 ) * ( pow ( s_0369 , 1.0 ) * pow ( s_0514 , 1.0 ) * pow ( s_0763_b , 1.0 ) - pow ( s_0380 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0125__Keq_r_0125 ) / ( ( 1.0 + s_0369 / r_0125__kms_s_0369r_0125 ) * ( 1.0 + s_0514 / r_0125__kms_s_0514r_0125 ) * ( 1.0 + s_0763_b / r_0125__kms_s_0763_br_0125 ) + ( 1.0 + s_0380 / r_0125__kmp_s_0380r_0125 ) * ( 1.0 + s_1434_b / r_0125__kmp_s_1434_br_0125 ) - 1.0 ) ) / intracellular '
	# steryl ester hydrolase
	r_0995 = 'intracellular * r_0995__Vmax_r_0995 * ( pow ( 1.0 / r_0995__kms_s_0635r_0995 , 1.0 ) * pow ( 1.0 / r_0995__kms_s_0663r_0995 , 1.0 ) * ( pow ( s_0635 , 1.0 ) * pow ( s_0663 , 1.0 ) - pow ( s_0641 , 1.0 ) * pow ( s_1434_b , 1.0 ) / r_0995__Keq_r_0995 ) / ( ( 1.0 + s_0635 / r_0995__kms_s_0635r_0995 ) * ( 1.0 + s_0663 / r_0995__kms_s_0663r_0995 ) + ( 1.0 + s_0641 / r_0995__kmp_s_0641r_0995 ) * ( 1.0 + s_1434_b / r_0995__kmp_s_1434_br_0995 ) - 1.0 ) ) / intracellular '
	# phosphate transport
	r_1461 = 'function_279 ( r_1461__Keq_r_1461 , r_1461__Vmax_r_1461 , r_1461__kmp_s_0763_br_1461 , r_1461__kmp_s_1207r_1461 , r_1461__kms_s_0766_br_1461 , r_1461__kms_s_1209_br_1461 , s_0763_b , s_0766_b , s_1207 , s_1209_b ) '
	# deoxyadenylate kinase
	r_0360 = 'intracellular * r_0360__Vmax_r_0360 * ( pow ( 1.0 / r_0360__kms_s_0400r_0360 , 1.0 ) * pow ( 1.0 / r_0360__kms_s_0562r_0360 , 1.0 ) * ( pow ( s_0400 , 1.0 ) * pow ( s_0562 , 1.0 ) - pow ( s_0446 , 1.0 ) * pow ( s_0564 , 1.0 ) / r_0360__Keq_r_0360 ) / ( ( 1.0 + s_0400 / r_0360__kms_s_0400r_0360 ) * ( 1.0 + s_0562 / r_0360__kms_s_0562r_0360 ) + ( 1.0 + s_0446 / r_0360__kmp_s_0446r_0360 ) * ( 1.0 + s_0564 / r_0360__kmp_s_0564r_0360 ) - 1.0 ) ) / intracellular '
	# 3',5'-bisphosphate nucleotidase
	r_0034 = 'intracellular * r_0034__Vmax_r_0034 * ( pow ( 1.0 / r_0034__kms_s_0397r_0034 , 1.0 ) * pow ( 1.0 / r_0034__kms_s_1434_br_0034 , 1.0 ) * ( pow ( s_0397 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0434 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0034__Keq_r_0034 ) / ( ( 1.0 + s_0397 / r_0034__kms_s_0397r_0034 ) * ( 1.0 + s_1434_b / r_0034__kms_s_1434_br_0034 ) + ( 1.0 + s_0434 / r_0034__kmp_s_0434r_0034 ) * ( 1.0 + s_1207 / r_0034__kmp_s_1207r_0034 ) - 1.0 ) ) / intracellular '
	# acetylglutamate kinase
	r_0130 = 'intracellular * r_0130__Vmax_r_0130 * ( pow ( 1.0 / r_0130__kms_s_0446r_0130 , 1.0 ) * pow ( 1.0 / r_0130__kms_s_1071r_0130 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_1071 , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_1070 , 1.0 ) / r_0130__Keq_r_0130 ) / ( ( 1.0 + s_0446 / r_0130__kms_s_0446r_0130 ) * ( 1.0 + s_1071 / r_0130__kms_s_1071r_0130 ) + ( 1.0 + s_0400 / r_0130__kmp_s_0400r_0130 ) * ( 1.0 + s_1070 / r_0130__kmp_s_1070r_0130 ) - 1.0 ) ) / intracellular '
	# pyrimidine phosphatase
	r_0934 = 'intracellular * r_0934__Vmax_r_0934 * ( pow ( 1.0 / r_0934__kms_s_0319r_0934 , 1.0 ) * pow ( 1.0 / r_0934__kms_s_1434_br_0934 , 1.0 ) * ( pow ( s_0319 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0320 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0934__Keq_r_0934 ) / ( ( 1.0 + s_0319 / r_0934__kms_s_0319r_0934 ) * ( 1.0 + s_1434_b / r_0934__kms_s_1434_br_0934 ) + ( 1.0 + s_0320 / r_0934__kmp_s_0320r_0934 ) * ( 1.0 + s_1207 / r_0934__kmp_s_1207r_0934 ) - 1.0 ) ) / intracellular '
	# succinate transport
	r_1503 = 'r_1503__Vmax_r_1503 * ( pow ( 1.0 / r_1503__kms_s_0763_br_1503 , 1.0 ) * pow ( 1.0 / r_1503__kms_s_1338r_1503 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_1338 , 1.0 ) - pow ( s_0766_b , 1.0 ) * pow ( s_1339_b , 1.0 ) / r_1503__Keq_r_1503 ) / ( ( 1.0 + s_0763_b / r_1503__kms_s_0763_br_1503 ) * ( 1.0 + s_1338 / r_1503__kms_s_1338r_1503 ) + ( 1.0 + s_0766_b / r_1503__kmp_s_0766_br_1503 ) * ( 1.0 + s_1339_b / r_1503__kmp_s_1339_br_1503 ) - 1.0 ) ) '
	# glycerol dehydrogenase (NADP-dependent)
	r_0526 = 'intracellular * r_0526__Vmax_r_0526 * ( pow ( 1.0 / r_0526__kms_s_0732r_0526 , 1.0 ) * pow ( 1.0 / r_0526__kms_s_1091r_0526 , 1.0 ) * ( pow ( s_0732 , 1.0 ) * pow ( s_1091 , 1.0 ) - pow ( s_0734 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1096 , 1.0 ) / r_0526__Keq_r_0526 ) / ( ( 1.0 + s_0732 / r_0526__kms_s_0732r_0526 ) * ( 1.0 + s_1091 / r_0526__kms_s_1091r_0526 ) + ( 1.0 + s_0734 / r_0526__kmp_s_0734r_0526 ) * ( 1.0 + s_0763_b / r_0526__kmp_s_0763_br_0526 ) * ( 1.0 + s_1096 / r_0526__kmp_s_1096r_0526 ) - 1.0 ) ) / intracellular '
	# N-acetyl-g-glutamyl-phosphate reductase
	r_0728 = 'intracellular * r_0728__Vmax_r_0728 * ( pow ( 1.0 / r_0728__kms_s_0763_br_0728 , 1.0 ) * pow ( 1.0 / r_0728__kms_s_1070r_0728 , 1.0 ) * pow ( 1.0 / r_0728__kms_s_1096r_0728 , 1.0 ) * ( pow ( s_0763_b , 1.0 ) * pow ( s_1070 , 1.0 ) * pow ( s_1096 , 1.0 ) - pow ( s_0149 , 1.0 ) * pow ( s_1091 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0728__Keq_r_0728 ) / ( ( 1.0 + s_0763_b / r_0728__kms_s_0763_br_0728 ) * ( 1.0 + s_1070 / r_0728__kms_s_1070r_0728 ) * ( 1.0 + s_1096 / r_0728__kms_s_1096r_0728 ) + ( 1.0 + s_0149 / r_0728__kmp_s_0149r_0728 ) * ( 1.0 + s_1091 / r_0728__kmp_s_1091r_0728 ) * ( 1.0 + s_1207 / r_0728__kmp_s_1207r_0728 ) - 1.0 ) ) / intracellular '
	# ammonia transport
	r_1157 = '1.0 * r_1157__Vmax_r_1157 * ( pow ( 1.0 / r_1157__kms_s_0431_br_1157 , 1.0 ) * ( pow ( s_0431_b , 1.0 ) - pow ( s_0430 , 1.0 ) / r_1157__Keq_r_1157 ) / ( 1.0 + s_0431_b / r_1157__kms_s_0431_br_1157 + 1.0 + s_0430 / r_1157__kmp_s_0430r_1157 - 1.0 ) ) '
	# ethanol transport
	r_1247 = 'r_1247__Vmax_r_1247 * ( pow ( 1.0 / r_1247__kms_s_0650r_1247 , 1.0 ) * ( pow ( s_0650 , 1.0 ) - pow ( s_0651_b , 1.0 ) / r_1247__Keq_r_1247 ) / ( 1.0 + s_0650 / r_1247__kms_s_0650r_1247 + 1.0 + s_0651_b / r_1247__kmp_s_0651_br_1247 - 1.0 ) ) '
	# O2 transport
	r_1435 = 'r_1435__Vmax_r_1435 * ( pow ( 1.0 / r_1435__kms_s_1162_br_1435 , 1.0 ) * ( pow ( s_1162_b , 1.0 ) - pow ( s_1160 , 1.0 ) / r_1435__Keq_r_1435 ) / ( 1.0 + s_1162_b / r_1435__kms_s_1162_br_1435 + 1.0 + s_1160 / r_1435__kmp_s_1160r_1435 - 1.0 ) ) '
	# phosphoribosylglycinamide synthase
	r_0890 = 'intracellular * r_0890__Vmax_r_0890 * ( pow ( 1.0 / r_0890__kms_s_0333r_0890 , 1.0 ) * pow ( 1.0 / r_0890__kms_s_0446r_0890 , 1.0 ) * pow ( 1.0 / r_0890__kms_s_0740r_0890 , 1.0 ) * ( pow ( s_0333 , 1.0 ) * pow ( s_0446 , 1.0 ) * pow ( s_0740 , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1048 , 1.0 ) * pow ( s_1207 , 1.0 ) / r_0890__Keq_r_0890 ) / ( ( 1.0 + s_0333 / r_0890__kms_s_0333r_0890 ) * ( 1.0 + s_0446 / r_0890__kms_s_0446r_0890 ) * ( 1.0 + s_0740 / r_0890__kms_s_0740r_0890 ) + ( 1.0 + s_0400 / r_0890__kmp_s_0400r_0890 ) * ( 1.0 + s_0763_b / r_0890__kmp_s_0763_br_0890 ) * ( 1.0 + s_1048 / r_0890__kmp_s_1048r_0890 ) * ( 1.0 + s_1207 / r_0890__kmp_s_1207r_0890 ) - 1.0 ) ) / intracellular '
	# inorganic diphosphatase
	r_0610 = 'intracellular * r_0610__Vmax_r_0610 * ( pow ( 1.0 / r_0610__kms_s_0605r_0610 , 1.0 ) * pow ( 1.0 / r_0610__kms_s_1434_br_0610 , 1.0 ) * ( pow ( s_0605 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0763_b , 1.0 ) * pow ( s_1207 , 2.0 ) / r_0610__Keq_r_0610 ) / ( ( 1.0 + s_0605 / r_0610__kms_s_0605r_0610 ) * ( 1.0 + s_1434_b / r_0610__kms_s_1434_br_0610 ) + ( 1.0 + s_0763_b / r_0610__kmp_s_0763_br_0610 ) * ( 1.0 + s_1207 / r_0610__kmp_s_1207r_0610 ) - 1.0 ) ) / intracellular '
	# non-enzymatic reaction
	r_0765 = 'intracellular * r_0765__Vmax_r_0765 * ( pow ( 1.0 / r_0765__kms_s_0180r_0765 , 1.0 ) * pow ( 1.0 / r_0765__kms_s_0763_br_0765 , 1.0 ) * ( pow ( s_0180 , 1.0 ) * pow ( s_0763_b , 1.0 ) - pow ( s_0181 , 1.0 ) * pow ( s_0470 , 1.0 ) / r_0765__Keq_r_0765 ) / ( ( 1.0 + s_0180 / r_0765__kms_s_0180r_0765 ) * ( 1.0 + s_0763_b / r_0765__kms_s_0763_br_0765 ) + ( 1.0 + s_0181 / r_0765__kmp_s_0181r_0765 ) * ( 1.0 + s_0470 / r_0765__kmp_s_0470r_0765 ) - 1.0 ) ) / intracellular '
	# lipid production
	r_1816 = 'intracellular * r_1816__V_o * ( 1.0 + r_1816__a_s_0090r_1816 * log ( s_0090 / r_1816__s_0090_or_1816 ) + r_1816__a_s_0124r_1816 * log ( s_0124 / r_1816__s_0124_or_1816 ) + r_1816__a_s_0627r_1816 * log ( s_0627 / r_1816__s_0627_or_1816 ) + r_1816__a_s_0632r_1816 * log ( s_0632 / r_1816__s_0632_or_1816 ) + r_1816__a_s_0635r_1816 * log ( s_0635 / r_1816__s_0635_or_1816 ) + r_1816__a_s_0641r_1816 * log ( s_0641 / r_1816__s_0641_or_1816 ) + r_1816__a_s_0663r_1816 * log ( s_0663 / r_1816__s_0663_or_1816 ) + r_1816__a_s_0669r_1816 * log ( s_0669 / r_1816__s_0669_or_1816 ) + r_1816__a_s_0824r_1816 * log ( s_0824 / r_1816__s_0824_or_1816 ) + r_1816__a_s_0963r_1816 * log ( s_0963 / r_1816__s_0963_or_1816 ) + r_1816__a_s_1219r_1816 * log ( s_1219 / r_1816__s_1219_or_1816 ) + r_1816__a_s_1228r_1816 * log ( s_1228 / r_1816__s_1228_or_1816 ) + r_1816__a_s_1233r_1816 * log ( s_1233 / r_1816__s_1233_or_1816 ) + r_1816__a_s_1399r_1816 * log ( s_1399 / r_1816__s_1399_or_1816 ) + r_1816__a_s_1447r_1816 * log ( s_1447 / r_1816__s_1447_or_1816 ) ) / intracellular '
	# growth
	r_1814 = 'r_1814__V_o * ( 1.0 + r_1814__a_s_0463r_1814 * log ( s_0463 / r_1814__s_0463_or_1814 ) ) '
	# biomass production
	r_1812 = 'intracellular * r_1812__V_o * ( 1.0 + r_1812__a_s_0001r_1812 * log ( s_0001 / r_1812__s_0001_or_1812 ) + r_1812__a_s_0416r_1812 * log ( s_0416 / r_1812__s_0416_or_1812 ) + r_1812__a_s_0434r_1812 * log ( s_0434 / r_1812__s_0434_or_1812 ) + r_1812__a_s_0446r_1812 * log ( s_0446 / r_1812__s_0446_or_1812 ) + r_1812__a_s_0511r_1812 * log ( s_0511 / r_1812__s_0511_or_1812 ) + r_1812__a_s_0564r_1812 * log ( s_0564 / r_1812__s_0564_or_1812 ) + r_1812__a_s_0569r_1812 * log ( s_0569 / r_1812__s_0569_or_1812 ) + r_1812__a_s_0593r_1812 * log ( s_0593 / r_1812__s_0593_or_1812 ) + r_1812__a_s_0619r_1812 * log ( s_0619 / r_1812__s_0619_or_1812 ) + r_1812__a_s_0740r_1812 * log ( s_0740 / r_1812__s_0740_or_1812 ) + r_1812__a_s_0743r_1812 * log ( s_0743 / r_1812__s_0743_or_1812 ) + r_1812__a_s_0752r_1812 * log ( s_0752 / r_1812__s_0752_or_1812 ) + r_1812__a_s_0863r_1812 * log ( s_0863 / r_1812__s_0863_or_1812 ) + r_1812__a_s_0873r_1812 * log ( s_0873 / r_1812__s_0873_or_1812 ) + r_1812__a_s_0877r_1812 * log ( s_0877 / r_1812__s_0877_or_1812 ) + r_1812__a_s_0881r_1812 * log ( s_0881 / r_1812__s_0881_or_1812 ) + r_1812__a_s_0889r_1812 * log ( s_0889 / r_1812__s_0889_or_1812 ) + r_1812__a_s_0899r_1812 * log ( s_0899 / r_1812__s_0899_or_1812 ) + r_1812__a_s_0907r_1812 * log ( s_0907 / r_1812__s_0907_or_1812 ) + r_1812__a_s_0911r_1812 * log ( s_0911 / r_1812__s_0911_or_1812 ) + r_1812__a_s_0920r_1812 * log ( s_0920 / r_1812__s_0920_or_1812 ) + r_1812__a_s_0925r_1812 * log ( s_0925 / r_1812__s_0925_or_1812 ) + r_1812__a_s_0929r_1812 * log ( s_0929 / r_1812__s_0929_or_1812 ) + r_1812__a_s_0933r_1812 * log ( s_0933 / r_1812__s_0933_or_1812 ) + r_1812__a_s_0936r_1812 * log ( s_0936 / r_1812__s_0936_or_1812 ) + r_1812__a_s_0939r_1812 * log ( s_0939 / r_1812__s_0939_or_1812 ) + r_1812__a_s_0943r_1812 * log ( s_0943 / r_1812__s_0943_or_1812 ) + r_1812__a_s_0949r_1812 * log ( s_0949 / r_1812__s_0949_or_1812 ) + r_1812__a_s_0952r_1812 * log ( s_0952 / r_1812__s_0952_or_1812 ) + r_1812__a_s_0955r_1812 * log ( s_0955 / r_1812__s_0955_or_1812 ) + r_1812__a_s_0960r_1812 * log ( s_0960 / r_1812__s_0960_or_1812 ) + r_1812__a_s_1000r_1812 * log ( s_1000 / r_1812__s_1000_or_1812 ) + r_1812__a_s_1011r_1812 * log ( s_1011 / r_1812__s_1011_or_1812 ) + r_1812__a_s_1347r_1812 * log ( s_1347 / r_1812__s_1347_or_1812 ) + r_1812__a_s_1417r_1812 * log ( s_1417 / r_1812__s_1417_or_1812 ) + r_1812__a_s_1283r_1812 * log ( s_1283 / r_1812__s_1283_or_1812 ) ) / intracellular '
	# ribonucleoside-diphosphate reductase
	r_0951 = 'intracellular * r_0951__Vmax_r_0951 * ( pow ( 1.0 / r_0951__kms_s_0400r_0951 , 1.0 ) * pow ( 1.0 / r_0951__kms_s_1521r_0951 , 1.0 ) * ( pow ( s_0400 , 1.0 ) * pow ( s_1521 , 1.0 ) - pow ( s_0562 , 1.0 ) * pow ( s_1434_b , 1.0 ) * pow ( s_1517 , 1.0 ) / r_0951__Keq_r_0951 ) / ( ( 1.0 + s_0400 / r_0951__kms_s_0400r_0951 ) * ( 1.0 + s_1521 / r_0951__kms_s_1521r_0951 ) + ( 1.0 + s_0562 / r_0951__kmp_s_0562r_0951 ) * ( 1.0 + s_1434_b / r_0951__kmp_s_1434_br_0951 ) * ( 1.0 + s_1517 / r_0951__kmp_s_1517r_0951 ) - 1.0 ) ) / intracellular '
	# glucose transport
	r_1293 = 'r_1293__Vmax_r_1293 * ( pow ( 1.0 / r_1293__kms_s_0547_br_1293 , 1.0 ) * ( pow ( s_0547_b , 1.0 ) - pow ( s_0545 , 1.0 ) / r_1293__Keq_r_1293 ) / ( 1.0 + s_0547_b / r_1293__kms_s_0547_br_1293 + 1.0 + s_0545 / r_1293__kmp_s_0545r_1293 - 1.0 ) ) '
	# dihydroxyacetone kinase
	r_0386 = 'intracellular * r_0386__Vmax_r_0386 * ( pow ( 1.0 / r_0386__kms_s_0446r_0386 , 1.0 ) * pow ( 1.0 / r_0386__kms_s_0734r_0386 , 1.0 ) * ( pow ( s_0446 , 1.0 ) * pow ( s_0734 , 1.0 ) - pow ( s_0400 , 1.0 ) * pow ( s_0735 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0386__Keq_r_0386 ) / ( ( 1.0 + s_0446 / r_0386__kms_s_0446r_0386 ) * ( 1.0 + s_0734 / r_0386__kms_s_0734r_0386 ) + ( 1.0 + s_0400 / r_0386__kmp_s_0400r_0386 ) * ( 1.0 + s_0735 / r_0386__kmp_s_0735r_0386 ) * ( 1.0 + s_0763_b / r_0386__kmp_s_0763_br_0386 ) - 1.0 ) ) / intracellular '
	# 1-acyl-sn-gylcerol-3-phosphate acyltransferase
	r_0009 = 'intracellular * r_0009__Vmax_r_0009 * ( pow ( 1.0 / r_0009__kms_s_0083r_0009 , 1.0 ) * pow ( 1.0 / r_0009__kms_s_0386r_0009 , 1.0 ) * ( pow ( s_0083 , 1.0 ) * pow ( s_0386 , 1.0 ) - pow ( s_0514 , 1.0 ) * pow ( s_0763_b , 4.0 ) * pow ( s_1215 , 1.0 ) / r_0009__Keq_r_0009 ) / ( ( 1.0 + s_0083 / r_0009__kms_s_0083r_0009 ) * ( 1.0 + s_0386 / r_0009__kms_s_0386r_0009 ) + ( 1.0 + s_0514 / r_0009__kmp_s_0514r_0009 ) * ( 1.0 + s_0763_b / r_0009__kmp_s_0763_br_0009 ) * ( 1.0 + s_1215 / r_0009__kmp_s_1215r_0009 ) - 1.0 ) ) / intracellular '
	# 1,3-beta-glucan synthase
	r_0005 = 'intracellular * r_0005__Vmax_r_0005 * ( pow ( 1.0 / r_0005__kms_s_1415r_0005 , 1.0 ) * ( pow ( s_1415 , 1.0 ) - pow ( s_0001 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1411 , 1.0 ) / r_0005__Keq_r_0005 ) / ( 1.0 + s_1415 / r_0005__kms_s_1415r_0005 + ( 1.0 + s_0001 / r_0005__kmp_s_0001r_0005 ) * ( 1.0 + s_0763_b / r_0005__kmp_s_0763_br_0005 ) * ( 1.0 + s_1411 / r_0005__kmp_s_1411r_0005 ) - 1.0 ) ) / intracellular '
	# bicarbonate formation
	r_0251 = 'intracellular * r_0251__Vmax_r_0251 * ( pow ( 1.0 / r_0251__kms_s_0470r_0251 , 1.0 ) * pow ( 1.0 / r_0251__kms_s_1434_br_0251 , 1.0 ) * ( pow ( s_0470 , 1.0 ) * pow ( s_1434_b , 1.0 ) - pow ( s_0458 , 1.0 ) * pow ( s_0763_b , 1.0 ) / r_0251__Keq_r_0251 ) / ( ( 1.0 + s_0470 / r_0251__kms_s_0470r_0251 ) * ( 1.0 + s_1434_b / r_0251__kms_s_1434_br_0251 ) + ( 1.0 + s_0458 / r_0251__kmp_s_0458r_0251 ) * ( 1.0 + s_0763_b / r_0251__kmp_s_0763_br_0251 ) - 1.0 ) ) / intracellular '
	# dolichyl-phosphate-mannose--protein mannosyltransferase
	r_0394 = 'intracellular * r_0394__Vmax_r_0394 * ( pow ( 1.0 / r_0394__kms_s_0615r_0394 , 1.0 ) * ( pow ( s_0615 , 1.0 ) - pow ( s_0616 , 1.0 ) * pow ( s_0763_b , 1.0 ) * pow ( s_1011 , 1.0 ) / r_0394__Keq_r_0394 ) / ( 1.0 + s_0615 / r_0394__kms_s_0615r_0394 + ( 1.0 + s_0616 / r_0394__kmp_s_0616r_0394 ) * ( 1.0 + s_0763_b / r_0394__kmp_s_0763_br_0394 ) * ( 1.0 + s_1011 / r_0394__kmp_s_1011r_0394 ) - 1.0 ) ) / intracellular '


	### odes
	odes = {}
	# (1->3)-beta-D-glucan [intracellular]
	odes['s_0001'] = '1.0' + ' * ' + r_0005 + ' - ' + '1.1358' + ' * ' + r_1812
	# (2R,3R)-2,3-dihydroxy-3-methylpentanoate [intracellular]
	odes['s_0007'] = '-1.0' + ' * ' + r_0385 + ' + ' + '1.0' + ' * ' + r_0640
	# (2R,3S)-3-isopropylmalate(2-) [intracellular]
	odes['s_0008'] = '1.0' + ' * ' + r_0063 + ' - ' + '1.0' + ' * ' + r_0064
	# (2S)-2-[5-amino-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamido]succinic acid [intracellular]
	odes['s_0009'] = '-1.0' + ' * ' + r_0169 + ' + ' + '1.0' + ' * ' + r_0886
	# (2S)-2-isopropyl-3-oxosuccinate(2-) [intracellular]
	odes['s_0010'] = '-1.0' + ' * ' + r_0031 + ' + ' + '1.0' + ' * ' + r_0064
	# (6R)-5,10-methenyltetrahydrofolic acid [intracellular]
	odes['s_0015'] = '-1.0' + ' * ' + r_0699 + ' + ' + '1.0' + ' * ' + r_0707
	# (N(omega)-L-arginino)succinic acid [intracellular]
	odes['s_0017'] = '-1.0' + ' * ' + r_0225 + ' + ' + '1.0' + ' * ' + r_0226
	# (R)-2,3-dihydroxy-3-methylbutanoate [intracellular]
	odes['s_0018'] = '1.0' + ' * ' + r_0111 + ' - ' + '1.0' + ' * ' + r_0384
	# (R)-5-diphosphomevalonic acid [intracellular]
	odes['s_0021'] = '-1.0' + ' * ' + r_0715 + ' + ' + '1.0' + ' * ' + r_0877
	# (R)-5-phosphomevalonic acid [intracellular]
	odes['s_0022'] = '1.0' + ' * ' + r_0712 + ' - ' + '1.0' + ' * ' + r_0877
	# (R)-mevalonate [intracellular]
	odes['s_0031'] = '1.0' + ' * ' + r_0598 + ' - ' + '1.0' + ' * ' + r_0712
	# (S)-2,3-epoxysqualene [intracellular]
	odes['s_0040'] = '-1.0' + ' * ' + r_0673 + ' + ' + '1.0' + ' * ' + r_0991
	# (S)-2-acetyl-2-hydroxybutanoate [intracellular]
	odes['s_0042'] = '1.0' + ' * ' + r_0016 + ' - ' + '1.0' + ' * ' + r_0640
	# (S)-3-hydroxyhexacosanoyl-CoA [intracellular]
	odes['s_0046'] = '1.0' + ' * ' + r_0057 + ' - ' + '1.0' + ' * ' + r_0719
	# (S)-3-hydroxypalmitoyl-CoA [intracellular]
	odes['s_0052'] = '1.0' + ' * ' + r_0058 + ' - ' + '1.0' + ' * ' + r_0720
	# (S)-3-hydroxytetradecanoyl-CoA [intracellular]
	odes['s_0055'] = '1.0' + ' * ' + r_0060 + ' - ' + '1.0' + ' * ' + r_0722
	# (S)-3-methyl-2-oxopentanoate [intracellular]
	odes['s_0058'] = '1.0' + ' * ' + r_0385 + ' - ' + '1.0' + ' * ' + r_0634
	# (S)-dihydroorotate [intracellular]
	odes['s_0064'] = '-1.0' + ' * ' + r_0374 + ' + ' + '1.0' + ' * ' + r_0381
	# (S)-malate(2-) [intracellular]
	odes['s_0069'] = '-1.0' + ' * ' + r_0485 + ' + ' + '1.0' + ' * ' + r_0688
	# 1-(2-carboxyphenylamino)-1-deoxy-D-ribulose 5-phosphate [intracellular]
	odes['s_0078'] = '-1.0' + ' * ' + r_0608 + ' + ' + '1.0' + ' * ' + r_0887
	# 1-(5-phospho-D-ribosyl)-5-[(5-phospho-D-ribosylamino)methylideneamino]imidazole-4-carboxamide [intracellular]
	odes['s_0079'] = '-1.0' + ' * ' + r_0008 + ' + ' + '1.0' + ' * ' + r_0881
	# 1-(5-phosphoribosyl)-5'-AMP [intracellular]
	odes['s_0080'] = '-1.0' + ' * ' + r_0881 + ' + ' + '1.0' + ' * ' + r_0882
	# 1-acyl-sn-glycerol 3-phosphate [intracellular]
	odes['s_0083'] = '-1.0' + ' * ' + r_0009 + ' + ' + '1.0' + ' * ' + r_0534
	# 1-C-(indol-3-yl)glycerol 3-phosphate [intracellular]
	odes['s_0088'] = '1.0' + ' * ' + r_0608 + ' - ' + '1.0' + ' * ' + r_1042
	# 1-phosphatidyl-1D-myo-inositol [intracellular]
	odes['s_0090'] = '1.0' + ' * ' + r_0847 + ' - ' + '0.001531' + ' * ' + r_1816
	# 1-pyrroline-3-hydroxy-5-carboxylic acid [intracellular]
	odes['s_0118'] = '1.0' + ' * ' + r_0660 + ' - ' + '1.0' + ' * ' + r_0661
	# 1-pyrroline-5-carboxylate [intracellular]
	odes['s_0120'] = '1.0' + ' * ' + r_0657 + ' - ' + '1.0' + ' * ' + r_0936
	# 10-formyltetrahydrofolic acid [intracellular]
	odes['s_0122'] = '1.0' + ' * ' + r_0479 + ' + ' + '1.0' + ' * ' + r_0699 + ' - ' + '1.0' + ' * ' + r_0885 + ' - ' + '1.0' + ' * ' + r_0889
	# 14-demethyllanosterol [intracellular]
	odes['s_0124'] = '1.0' + ' * ' + r_0258 + ' - ' + '1.0' + ' * ' + r_0268 + ' - ' + '5.6e-5' + ' * ' + r_1816
	# 1D-myo-inositol 1-phosphate [intracellular]
	odes['s_0128'] = '-1.0' + ' * ' + r_0618 + ' - ' + '1.0' + ' * ' + r_0621 + ' - ' + '1.0' + ' * ' + r_0725 + ' + ' + '1.0' + ' * ' + r_0726
	# 2,5-diamino-4-hydroxy-6-(5-phosphoribosylamino)pyrimidine [intracellular]
	odes['s_0145'] = '-1.0' + ' * ' + r_0015 + ' + ' + '1.0' + ' * ' + r_0562
	# 2,5-diamino-6-(5-phosphono)ribitylamino-4(3H)-pyrimidinone [intracellular]
	odes['s_0146'] = '-1.0' + ' * ' + r_0014 + ' + ' + '1.0' + ' * ' + r_0015
	# 2-acetamido-5-oxopentanoate [intracellular]
	odes['s_0149'] = '-1.0' + ' * ' + r_0133 + ' + ' + '1.0' + ' * ' + r_0728
	# 2-acetyllactic acid [intracellular]
	odes['s_0150'] = '-1.0' + ' * ' + r_0111 + ' + ' + '1.0' + ' * ' + r_0112
	# 2-formamido-N(1)-(5-phospho-D-ribosyl)acetamidine [intracellular]
	odes['s_0158'] = '-1.0' + ' * ' + r_0884 + ' + ' + '1.0' + ' * ' + r_0888
	# 2-hydroxy-3-oxobutyl phosphate [intracellular]
	odes['s_0163'] = '1.0' + ' * ' + r_0040 + ' - ' + '1.0' + ' * ' + r_0948
	# 2-isopropylmalate(2-) [intracellular]
	odes['s_0167'] = '-1.0' + ' * ' + r_0025 + ' + ' + '1.0' + ' * ' + r_0026
	# 2-isopropylmaleic acid [intracellular]
	odes['s_0170'] = '1.0' + ' * ' + r_0025 + ' - ' + '1.0' + ' * ' + r_0063
	# 2-oxaloglutaric acid [intracellular]
	odes['s_0180'] = '1.0' + ' * ' + r_0585 + ' - ' + '1.0' + ' * ' + r_0765
	# 2-oxoadipic acid [intracellular]
	odes['s_0181'] = '-1.0' + ' * ' + r_0018 + ' + ' + '1.0' + ' * ' + r_0765
	# 2-oxobutanoate [intracellular]
	odes['s_0183'] = '-1.0' + ' * ' + r_0016 + ' + ' + '1.0' + ' * ' + r_0339 + ' + ' + '1.0' + ' * ' + r_0667
	# 2-oxoglutarate [intracellular]
	odes['s_0185'] = '1.0' + ' * ' + r_0018 + ' + ' + '1.0' + ' * ' + r_0133 + ' + ' + '1.0' + ' * ' + r_0235 + ' - ' + '1.0' + ' * ' + r_0509 + ' - ' + '1.0' + ' * ' + r_0510 + ' + ' + '1.0' + ' * ' + r_0577 + ' - ' + '1.0' + ' * ' + r_0582 + ' + ' + '1.0' + ' * ' + r_0630 + ' + ' + '1.0' + ' * ' + r_0634 + ' + ' + '1.0' + ' * ' + r_0647 + ' + ' + '1.0' + ' * ' + r_0674 + ' + ' + '1.0' + ' * ' + r_0825 + ' + ' + '1.0' + ' * ' + r_0969 + ' + ' + '1.0' + ' * ' + r_1050 + ' + ' + '1.0' + ' * ' + r_1073
	# 2-phospho-D-glyceric acid [intracellular]
	odes['s_0193'] = '-1.0' + ' * ' + r_0398 + ' + ' + '1.0' + ' * ' + r_0866
	# 2-trans,6-trans-farnesyl diphosphate [intracellular]
	odes['s_0195'] = '1.0' + ' * ' + r_0496 + ' - ' + '2.0' + ' * ' + r_0993
	# 3'-phospho-5'-adenylyl sulfate [intracellular]
	odes['s_0206'] = '1.0' + ' * ' + r_0172 + ' - ' + '1.0' + ' * ' + r_0856
	# 3-(4-hydroxyphenyl)pyruvate [intracellular]
	odes['s_0209'] = '1.0' + ' * ' + r_0913 + ' - ' + '1.0' + ' * ' + r_1050
	# 3-(imidazol-4-yl)-2-oxopropyl dihydrogen phosphate [intracellular]
	odes['s_0212'] = '-1.0' + ' * ' + r_0577 + ' + ' + '1.0' + ' * ' + r_0605
	# 3-dehydro-4-methylzymosterol [intracellular]
	odes['s_0215'] = '1.0' + ' * ' + r_0262 + ' - ' + '1.0' + ' * ' + r_0263
	# 3-dehydroquinate [intracellular]
	odes['s_0216'] = '-1.0' + ' * ' + r_0042 + ' + ' + '1.0' + ' * ' + r_0043
	# 3-dehydroshikimate [intracellular]
	odes['s_0217'] = '1.0' + ' * ' + r_0042 + ' - ' + '1.0' + ' * ' + r_0976
	# 3-dehydrosphinganine [intracellular]
	odes['s_0218'] = '-1.0' + ' * ' + r_0044 + ' + ' + '1.0' + ' * ' + r_0972
	# 3-hydroxy-3-methylglutaryl-CoA [intracellular]
	odes['s_0225'] = '-1.0' + ' * ' + r_0598 + ' + ' + '1.0' + ' * ' + r_0599
	# 3-hydroxyoctadecanoyl-CoA [intracellular]
	odes['s_0234'] = '1.0' + ' * ' + r_0059 + ' - ' + '1.0' + ' * ' + r_0721
	# 3-methyl-2-oxobutanoate [intracellular]
	odes['s_0238'] = '-1.0' + ' * ' + r_0026 + ' + ' + '1.0' + ' * ' + r_0384 + ' - ' + '1.0' + ' * ' + r_1073
	# 3-oxohexacosanoyl-CoA [intracellular]
	odes['s_0247'] = '-1.0' + ' * ' + r_0057 + ' + ' + '1.0' + ' * ' + r_0719
	# 3-oxooctadecanoyl-CoA [intracellular]
	odes['s_0254'] = '-1.0' + ' * ' + r_0059 + ' + ' + '1.0' + ' * ' + r_0721
	# 3-oxopalmitoyl-CoA [intracellular]
	odes['s_0257'] = '-1.0' + ' * ' + r_0058 + ' + ' + '1.0' + ' * ' + r_0720
	# 3-oxotetradecanoyl-CoA [intracellular]
	odes['s_0261'] = '-1.0' + ' * ' + r_0060 + ' + ' + '1.0' + ' * ' + r_0722
	# 3-phospho-D-glyceric acid [intracellular]
	odes['s_0264'] = '1.0' + ' * ' + r_0865 + ' - ' + '1.0' + ' * ' + r_0866
	# 3-phospho-D-glyceroyl dihydrogen phosphate [intracellular]
	odes['s_0265'] = '1.0' + ' * ' + r_0525 + ' - ' + '1.0' + ' * ' + r_0865
	# 3-phosphoshikimic acid [intracellular]
	odes['s_0267'] = '-1.0' + ' * ' + r_0068 + ' + ' + '1.0' + ' * ' + r_0977
	# 4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol [intracellular]
	odes['s_0268'] = '-1.0' + ' * ' + r_0258 + ' + ' + '1.0' + ' * ' + r_0347
	# 4-methyl-2-oxopentanoate [intracellular]
	odes['s_0297'] = '1.0' + ' * ' + r_0031 + ' - ' + '1.0' + ' * ' + r_0674
	# 4-phospho-L-aspartate [intracellular]
	odes['s_0301'] = '1.0' + ' * ' + r_0233 + ' - ' + '1.0' + ' * ' + r_0238
	# 4alpha-methylzymosterol [intracellular]
	odes['s_0302'] = '1.0' + ' * ' + r_0263 + ' - ' + '1.0' + ' * ' + r_0265
	# 4beta-methylzymosterol-4alpha-carboxylic acid [intracellular]
	odes['s_0303'] = '-1.0' + ' * ' + r_0262 + ' + ' + '1.0' + ' * ' + r_0268
	# 5'-adenylyl sulfate [intracellular]
	odes['s_0304'] = '-1.0' + ' * ' + r_0172 + ' + ' + '1.0' + ' * ' + r_1007
	# 5'-xanthylic acid [intracellular]
	odes['s_0306'] = '-1.0' + ' * ' + r_0551 + ' + ' + '1.0' + ' * ' + r_0607
	# 5,10-methylenetetrahydrofolate(2-) [intracellular]
	odes['s_0307'] = '-1.0' + ' * ' + r_0093 + ' + ' + '1.0' + ' * ' + r_0538 + ' - ' + '1.0' + ' * ' + r_0539 + ' - ' + '1.0' + ' * ' + r_0707 + ' - ' + '1.0' + ' * ' + r_1032
	# 5,6,7,8-tetrahydrofolic acid [intracellular]
	odes['s_0309'] = '1.0' + ' * ' + r_0375 + ' - ' + '1.0' + ' * ' + r_0479 + ' - ' + '1.0' + ' * ' + r_0538 + ' + ' + '1.0' + ' * ' + r_0539 + ' + ' + '1.0' + ' * ' + r_0702 + ' + ' + '1.0' + ' * ' + r_0885 + ' + ' + '1.0' + ' * ' + r_0889
	# 5-[(5-phospho-1-deoxy-D-ribulos-1-ylamino)methylideneamino]-1-(5-phospho-D-ribosyl)imidazole-4-carboxamide [intracellular]
	odes['s_0315'] = '1.0' + ' * ' + r_0008 + ' - ' + '1.0' + ' * ' + r_0604
	# 5-amino-1-(5-phospho-D-ribosyl)imidazole [intracellular]
	odes['s_0316'] = '-1.0' + ' * ' + r_0883 + ' + ' + '1.0' + ' * ' + r_0884
	# 5-amino-1-(5-phospho-D-ribosyl)imidazole-4-carboxamide [intracellular]
	odes['s_0317'] = '1.0' + ' * ' + r_0169 + ' + ' + '1.0' + ' * ' + r_0604 + ' - ' + '1.0' + ' * ' + r_0885
	# 5-amino-1-(5-phospho-D-ribosyl)imidazole-4-carboxylic acid [intracellular]
	odes['s_0318'] = '1.0' + ' * ' + r_0883 + ' - ' + '1.0' + ' * ' + r_0886
	# 5-amino-6-(5-phosphoribitylamino)uracil [intracellular]
	odes['s_0319'] = '1.0' + ' * ' + r_0014 + ' - ' + '1.0' + ' * ' + r_0934
	# 5-amino-6-(D-ribitylamino)uracil [intracellular]
	odes['s_0320'] = '1.0' + ' * ' + r_0934 + ' - ' + '1.0' + ' * ' + r_0948 + ' + ' + '1.0' + ' * ' + r_0949
	# 5-formamido-1-(5-phospho-D-ribosyl)imidazole-4-carboxamide [intracellular]
	odes['s_0325'] = '-1.0' + ' * ' + r_0606 + ' + ' + '1.0' + ' * ' + r_0885
	# 5-methyltetrahydrofolate(2-) [intracellular]
	odes['s_0328'] = '1.0' + ' * ' + r_0093 + ' - ' + '1.0' + ' * ' + r_0702
	# 5-O-(1-carboxyvinyl)-3-phosphoshikimic acid [intracellular]
	odes['s_0330'] = '1.0' + ' * ' + r_0068 + ' - ' + '1.0' + ' * ' + r_0306
	# 5-O-phosphono-alpha-D-ribofuranosyl diphosphate [intracellular]
	odes['s_0331'] = '-1.0' + ' * ' + r_0220 + ' - ' + '1.0' + ' * ' + r_0245 + ' - ' + '1.0' + ' * ' + r_0514 + ' - ' + '1.0' + ' * ' + r_0793 + ' + ' + '1.0' + ' * ' + r_0891
	# 5-phospho-beta-D-ribosylamine [intracellular]
	odes['s_0333'] = '1.0' + ' * ' + r_0514 + ' - ' + '1.0' + ' * ' + r_0890
	# 5-phosphoribosyl-ATP [intracellular]
	odes['s_0334'] = '1.0' + ' * ' + r_0245 + ' - ' + '1.0' + ' * ' + r_0882
	# 6,7-dimethyl-8-(1-D-ribityl)lumazine [intracellular]
	odes['s_0335'] = '1.0' + ' * ' + r_0948 + ' - ' + '2.0' + ' * ' + r_0949
	# 7-phospho-2-dehydro-3-deoxy-D-arabino-heptonic acid [intracellular]
	odes['s_0356'] = '1.0' + ' * ' + r_0021 + ' - ' + '1.0' + ' * ' + r_0043
	# acetaldehyde [intracellular]
	odes['s_0366'] = '-1.0' + ' * ' + r_0183 + ' - ' + '1.0' + ' * ' + r_0191 + ' + ' + '1.0' + ' * ' + r_0938 + ' + ' + '1.0' + ' * ' + r_1026
	# acetate [intracellular]
	odes['s_0369'] = '-1.0' + ' * ' + r_0125 + ' + ' + '1.0' + ' * ' + r_0127 + ' + ' + '1.0' + ' * ' + r_0191 + ' + ' + '1.0' + ' * ' + r_0340 + ' + ' + '1.0' + ' * ' + r_0783
	# acetoacetyl-CoA [intracellular]
	odes['s_0374'] = '1.0' + ' * ' + r_0118 + ' - ' + '1.0' + ' * ' + r_0599
	# acetyl-CoA [intracellular]
	odes['s_0380'] = '-1.0' + ' * ' + r_0026 + ' - ' + '2.0' + ' * ' + r_0118 + ' - ' + '1.0' + ' * ' + r_0123 + ' + ' + '1.0' + ' * ' + r_0125 + ' - ' + '1.0' + ' * ' + r_0127 + ' - ' + '1.0' + ' * ' + r_0328 + ' - ' + '1.0' + ' * ' + r_0430 + ' - ' + '1.0' + ' * ' + r_0582 + ' - ' + '1.0' + ' * ' + r_0589 + ' - ' + '1.0' + ' * ' + r_0599 + ' + ' + '1.0' + ' * ' + r_0940
	# acyl-CoA [intracellular]
	odes['s_0386'] = '-1.0' + ' * ' + r_0009 + ' - ' + '1.0' + ' * ' + r_0370 + ' - ' + '1.0' + ' * ' + r_0534 + ' + ' + '1.0' + ' * ' + r_1672
	# adenosine [intracellular]
	odes['s_0393'] = '-1.0' + ' * ' + r_0157 + ' + ' + '1.0' + ' * ' + r_0159
	# adenosine 3',5'-bismonophosphate [intracellular]
	odes['s_0397'] = '-1.0' + ' * ' + r_0034 + ' + ' + '1.0' + ' * ' + r_0856
	# ADP [intracellular]
	odes['s_0400'] = '1.0' + ' * ' + r_0123 + ' + ' + '1.0' + ' * ' + r_0130 + ' + ' + '1.0' + ' * ' + r_0157 + ' - ' + '2.0' + ' * ' + r_0163 + ' - ' + '1.0' + ' * ' + r_0165 + ' + ' + '1.0' + ' * ' + r_0172 + ' + ' + '1.0' + ' * ' + r_0233 + ' - ' + '1.0' + ' * ' + r_0246 + ' + ' + '1.0' + ' * ' + r_0249 + ' + ' + '2.0' + ' * ' + r_0277 + ' + ' + '1.0' + ' * ' + r_0336 + ' - ' + '1.0' + ' * ' + r_0345 + ' - ' + '1.0' + ' * ' + r_0360 + ' - ' + '1.0' + ' * ' + r_0362 + ' + ' + '1.0' + ' * ' + r_0386 + ' + ' + '1.0' + ' * ' + r_0479 + ' + ' + '1.0' + ' * ' + r_0499 + ' + ' + '1.0' + ' * ' + r_0506 + ' + ' + '1.0' + ' * ' + r_0515 + ' + ' + '1.0' + ' * ' + r_0567 + ' + ' + '1.0' + ' * ' + r_0573 + ' + ' + '1.0' + ' * ' + r_0588 + ' + ' + '1.0' + ' * ' + r_0715 + ' - ' + '1.0' + ' * ' + r_0771 + ' + ' + '1.0' + ' * ' + r_0779 + ' + ' + '1.0' + ' * ' + r_0859 + ' - ' + '1.0' + ' * ' + r_0865 + ' + ' + '1.0' + ' * ' + r_0877 + ' + ' + '1.0' + ' * ' + r_0884 + ' + ' + '1.0' + ' * ' + r_0886 + ' + ' + '1.0' + ' * ' + r_0888 + ' + ' + '1.0' + ' * ' + r_0890 + ' + ' + '1.0' + ' * ' + r_0937 + ' - ' + '1.0' + ' * ' + r_0941 + ' - ' + '1.0' + ' * ' + r_0951 + ' + ' + '1.0' + ' * ' + r_0977 + ' + ' + '1.0' + ' * ' + r_1003 + ' - ' + '1.0' + ' * ' + r_1007 + ' + ' + '1.0' + ' * ' + r_1059 + ' - ' + '1.0' + ' * ' + r_1066 + ' + ' + '59.276' + ' * ' + r_1812
	# aldehydo-D-glucose 6-phosphate [intracellular]
	odes['s_0410'] = '-1.0' + ' * ' + r_0213 + ' - ' + '1.0' + ' * ' + r_0505 + ' + ' + '1.0' + ' * ' + r_0573 + ' - ' + '1.0' + ' * ' + r_0726 + ' - ' + '1.0' + ' * ' + r_0861
	# alpha,alpha-trehalose [intracellular]
	odes['s_0416'] = '1.0' + ' * ' + r_1038 + ' - ' + '0.023371' + ' * ' + r_1812
	# alpha,alpha-trehalose 6-phosphate [intracellular]
	odes['s_0419'] = '1.0' + ' * ' + r_0213 + ' - ' + '1.0' + ' * ' + r_1038
	# alpha-D-ribose 5-phosphate [intracellular]
	odes['s_0427'] = '-1.0' + ' * ' + r_0891 + ' + ' + '1.0' + ' * ' + r_0963 + ' + ' + '1.0' + ' * ' + r_1036
	# ammonium [intracellular]
	odes['s_0430'] = '1.0' + ' * ' + r_0014 + ' - ' + '1.0' + ' * ' + r_0336 + ' + ' + '1.0' + ' * ' + r_0339 + ' - ' + '1.0' + ' * ' + r_0357 + ' - ' + '1.0' + ' * ' + r_0509 + ' - ' + '1.0' + ' * ' + r_0515 + ' + ' + '1.0' + ' * ' + r_0538 + ' + ' + '1.0' + ' * ' + r_0667 + ' + ' + '1.0' + ' * ' + r_1157
	# AMP [intracellular]
	odes['s_0434'] = '1.0' + ' * ' + r_0034 + ' - ' + '1.0' + ' * ' + r_0127 + ' + ' + '1.0' + ' * ' + r_0157 + ' + ' + '1.0' + ' * ' + r_0163 + ' + ' + '1.0' + ' * ' + r_0165 + ' + ' + '1.0' + ' * ' + r_0171 + ' + ' + '1.0' + ' * ' + r_0226 + ' + ' + '1.0' + ' * ' + r_0229 + ' + ' + '1.0' + ' * ' + r_0437 + ' - ' + '1.0' + ' * ' + r_0439 + ' - ' + '1.0' + ' * ' + r_0442 + ' + ' + '1.0' + ' * ' + r_0551 + ' + ' + '1.0' + ' * ' + r_0650 + ' + ' + '1.0' + ' * ' + r_0891 + ' - ' + '0.051' + ' * ' + r_1812
	# amylose [intracellular]
	odes['s_0438'] = '-1.0' + ' * ' + r_0006 + ' + ' + '1.0' + ' * ' + r_0547
	# anthranilate [intracellular]
	odes['s_0439'] = '-1.0' + ' * ' + r_0220 + ' + ' + '1.0' + ' * ' + r_0221
	# ATP [intracellular]
	odes['s_0446'] = '-1.0' + ' * ' + r_0123 + ' + ' + '1.0' + ' * ' + r_0127 + ' - ' + '1.0' + ' * ' + r_0130 + ' - ' + '1.0' + ' * ' + r_0157 + ' + ' + '1.0' + ' * ' + r_0163 + ' - ' + '1.0' + ' * ' + r_0172 + ' - ' + '1.0' + ' * ' + r_0226 + ' - ' + '1.0' + ' * ' + r_0229 + ' - ' + '1.0' + ' * ' + r_0233 + ' - ' + '1.0' + ' * ' + r_0245 + ' + ' + '1.0' + ' * ' + r_0246 + ' - ' + '1.0' + ' * ' + r_0249 + ' - ' + '2.0' + ' * ' + r_0277 + ' - ' + '1.0' + ' * ' + r_0336 + ' + ' + '1.0' + ' * ' + r_0345 + ' + ' + '1.0' + ' * ' + r_0360 + ' + ' + '1.0' + ' * ' + r_0362 + ' - ' + '1.0' + ' * ' + r_0386 + ' - ' + '1.0' + ' * ' + r_0437 + ' + ' + '1.0' + ' * ' + r_0439 + ' + ' + '1.0' + ' * ' + r_0442 + ' - ' + '1.0' + ' * ' + r_0479 + ' - ' + '1.0' + ' * ' + r_0499 + ' - ' + '1.0' + ' * ' + r_0506 + ' - ' + '1.0' + ' * ' + r_0515 + ' - ' + '1.0' + ' * ' + r_0551 + ' - ' + '1.0' + ' * ' + r_0567 + ' - ' + '1.0' + ' * ' + r_0573 + ' - ' + '1.0' + ' * ' + r_0588 + ' - ' + '1.0' + ' * ' + r_0650 + ' - ' + '1.0' + ' * ' + r_0701 + ' - ' + '1.0' + ' * ' + r_0715 + ' + ' + '1.0' + ' * ' + r_0771 + ' - ' + '1.0' + ' * ' + r_0779 + ' - ' + '1.0' + ' * ' + r_0859 + ' + ' + '1.0' + ' * ' + r_0865 + ' - ' + '1.0' + ' * ' + r_0877 + ' - ' + '1.0' + ' * ' + r_0884 + ' - ' + '1.0' + ' * ' + r_0886 + ' - ' + '1.0' + ' * ' + r_0888 + ' - ' + '1.0' + ' * ' + r_0890 + ' - ' + '1.0' + ' * ' + r_0891 + ' - ' + '1.0' + ' * ' + r_0937 + ' + ' + '1.0' + ' * ' + r_0941 + ' - ' + '1.0' + ' * ' + r_0959 + ' - ' + '1.0' + ' * ' + r_0977 + ' - ' + '1.0' + ' * ' + r_1003 + ' - ' + '1.0' + ' * ' + r_1059 + ' + ' + '1.0' + ' * ' + r_1066 + ' - ' + '59.276' + ' * ' + r_1812
	# beta-D-glucose 6-phosphate [intracellular]
	odes['s_0455'] = '1.0' + ' * ' + r_0499 + ' - ' + '1.0' + ' * ' + r_0504
	# bicarbonate [intracellular]
	odes['s_0458'] = '-1.0' + ' * ' + r_0123 + ' + ' + '1.0' + ' * ' + r_0251 + ' - ' + '1.0' + ' * ' + r_0277 + ' - ' + '1.0' + ' * ' + r_0937
	# biomass [intracellular]
	odes['s_0463'] = '1.0' + ' * ' + r_1812 + ' - ' + '1.0' + ' * ' + r_1814
	# but-1-ene-1,2,4-tricarboxylic acid [intracellular]
	odes['s_0468'] = '1.0' + ' * ' + r_0029 + ' - ' + '1.0' + ' * ' + r_0581
	# carbamoyl phosphate [intracellular]
	odes['s_0469'] = '-1.0' + ' * ' + r_0232 + ' + ' + '1.0' + ' * ' + r_0277 + ' - ' + '1.0' + ' * ' + r_0789
	# carbon dioxide [intracellular]
	odes['s_0470'] = '1.0' + ' * ' + r_0016 + ' + ' + '1.0' + ' * ' + r_0031 + ' + ' + '1.0' + ' * ' + r_0112 + ' - ' + '1.0' + ' * ' + r_0251 + ' + ' + '1.0' + ' * ' + r_0261 + ' + ' + '1.0' + ' * ' + r_0262 + ' + ' + '1.0' + ' * ' + r_0417 + ' + ' + '1.0' + ' * ' + r_0418 + ' + ' + '1.0' + ' * ' + r_0419 + ' + ' + '1.0' + ' * ' + r_0421 + ' + ' + '1.0' + ' * ' + r_0423 + ' + ' + '3.0' + ' * ' + r_0425 + ' + ' + '1.0' + ' * ' + r_0429 + ' + ' + '3.0' + ' * ' + r_0430 + ' + ' + '1.0' + ' * ' + r_0464 + ' + ' + '1.0' + ' * ' + r_0465 + ' + ' + '1.0' + ' * ' + r_0466 + ' + ' + '1.0' + ' * ' + r_0467 + ' + ' + '1.0' + ' * ' + r_0538 + ' + ' + '1.0' + ' * ' + r_0608 + ' + ' + '1.0' + ' * ' + r_0630 + ' + ' + '1.0' + ' * ' + r_0715 + ' + ' + '1.0' + ' * ' + r_0765 + ' + ' + '1.0' + ' * ' + r_0794 + ' + ' + '1.0' + ' * ' + r_0850 + ' - ' + '1.0' + ' * ' + r_0883 + ' + ' + '1.0' + ' * ' + r_0911 + ' + ' + '1.0' + ' * ' + r_0913 + ' + ' + '1.0' + ' * ' + r_0938 + ' + ' + '1.0' + ' * ' + r_0940 + ' + ' + '1.0' + ' * ' + r_0972 + ' - ' + '1.0' + ' * ' + r_1194
	# CDP [intracellular]
	odes['s_0481'] = '-1.0' + ' * ' + r_0345 + ' + ' + '1.0' + ' * ' + r_0712 + ' + ' + '1.0' + ' * ' + r_0771
	# CDP-diacylglycerol [intracellular]
	odes['s_0485'] = '1.0' + ' * ' + r_0284 + ' - ' + '1.0' + ' * ' + r_0847 + ' - ' + '1.0' + ' * ' + r_0853
	# chorismate(2-) [intracellular]
	odes['s_0500'] = '-1.0' + ' * ' + r_0221 + ' - ' + '1.0' + ' * ' + r_0304 + ' + ' + '1.0' + ' * ' + r_0306
	# cis-aconitate(3-) [intracellular]
	odes['s_0501'] = '-1.0' + ' * ' + r_0307 + ' + ' + '1.0' + ' * ' + r_0330
	# citrate(3-) [intracellular]
	odes['s_0507'] = '1.0' + ' * ' + r_0328 + ' - ' + '1.0' + ' * ' + r_0330
	# CMP [intracellular]
	odes['s_0511'] = '1.0' + ' * ' + r_0345 + ' + ' + '1.0' + ' * ' + r_0847 + ' + ' + '1.0' + ' * ' + r_0853 + ' - ' + '0.05' + ' * ' + r_1812
	# coenzyme A [intracellular]
	odes['s_0514'] = '1.0' + ' * ' + r_0009 + ' + ' + '1.0' + ' * ' + r_0026 + ' + ' + '1.0' + ' * ' + r_0118 + ' - ' + '1.0' + ' * ' + r_0125 + ' + ' + '1.0' + ' * ' + r_0127 + ' + ' + '1.0' + ' * ' + r_0290 + ' + ' + '1.0' + ' * ' + r_0328 + ' + ' + '1.0' + ' * ' + r_0370 + ' + ' + '1.0' + ' * ' + r_0417 + ' + ' + '1.0' + ' * ' + r_0418 + ' + ' + '1.0' + ' * ' + r_0419 + ' + ' + '1.0' + ' * ' + r_0421 + ' + ' + '1.0' + ' * ' + r_0423 + ' + ' + '3.0' + ' * ' + r_0425 + ' + ' + '1.0' + ' * ' + r_0429 + ' + ' + '3.0' + ' * ' + r_0430 + ' - ' + '1.0' + ' * ' + r_0437 + ' + ' + '1.0' + ' * ' + r_0439 + ' + ' + '1.0' + ' * ' + r_0442 + ' + ' + '1.0' + ' * ' + r_0464 + ' + ' + '1.0' + ' * ' + r_0465 + ' + ' + '1.0' + ' * ' + r_0466 + ' + ' + '1.0' + ' * ' + r_0467 + ' + ' + '1.0' + ' * ' + r_0534 + ' + ' + '1.0' + ' * ' + r_0582 + ' + ' + '1.0' + ' * ' + r_0589 + ' + ' + '1.0' + ' * ' + r_0598 + ' + ' + '1.0' + ' * ' + r_0599 + ' - ' + '1.0' + ' * ' + r_0940 + ' + ' + '1.0' + ' * ' + r_0972 + ' - ' + '1.0' + ' * ' + r_1003
	# CTP [intracellular]
	odes['s_0521'] = '-1.0' + ' * ' + r_0284 + ' + ' + '1.0' + ' * ' + r_0336 + ' - ' + '1.0' + ' * ' + r_0712 + ' - ' + '1.0' + ' * ' + r_0771
	# D-arabinono-1,4-lactone [intracellular]
	odes['s_0529'] = '-1.0' + ' * ' + r_0351 + ' + ' + '1.0' + ' * ' + r_0352
	# D-arabinose [intracellular]
	odes['s_0530'] = '1.0' + ' * ' + r_0351 + ' - ' + '1.0' + ' * ' + r_0352
	# D-erythro-1-(imidazol-4-yl)glycerol 3-phosphate [intracellular]
	odes['s_0532'] = '1.0' + ' * ' + r_0604 + ' - ' + '1.0' + ' * ' + r_0605
	# D-erythrose 4-phosphate(2-) [intracellular]
	odes['s_0533'] = '-1.0' + ' * ' + r_0021 + ' - ' + '1.0' + ' * ' + r_1035 + ' + ' + '1.0' + ' * ' + r_1037
	# D-fructose 1,6-bisphosphate [intracellular]
	odes['s_0537'] = '-1.0' + ' * ' + r_0484 + ' + ' + '1.0' + ' * ' + r_0859
	# D-fructose 6-phosphate [intracellular]
	odes['s_0539'] = '1.0' + ' * ' + r_0504 + ' + ' + '1.0' + ' * ' + r_0505 + ' - ' + '1.0' + ' * ' + r_0698 + ' - ' + '1.0' + ' * ' + r_0859 + ' - ' + '1.0' + ' * ' + r_1035 + ' - ' + '1.0' + ' * ' + r_1037
	# D-glucose [intracellular]
	odes['s_0545'] = '-1.0' + ' * ' + r_0499 + ' - ' + '1.0' + ' * ' + r_0573 + ' + ' + '1.0' + ' * ' + r_1293
	# D-glucose 1-phosphate [intracellular]
	odes['s_0549'] = '1.0' + ' * ' + r_0861 + ' - ' + '1.0' + ' * ' + r_1072
	# D-mannose 1-phosphate [intracellular]
	odes['s_0553'] = '-1.0' + ' * ' + r_0697 + ' + ' + '1.0' + ' * ' + r_0875
	# D-mannose 6-phosphate [intracellular]
	odes['s_0554'] = '1.0' + ' * ' + r_0698 + ' - ' + '1.0' + ' * ' + r_0875
	# D-ribulose 5-phosphate [intracellular]
	odes['s_0557'] = '-1.0' + ' * ' + r_0040 + ' - ' + '1.0' + ' * ' + r_0963 + ' + ' + '1.0' + ' * ' + r_0965
	# D-xylulose 5-phosphate [intracellular]
	odes['s_0561'] = '-1.0' + ' * ' + r_0965 + ' + ' + '1.0' + ' * ' + r_1036 + ' + ' + '1.0' + ' * ' + r_1037
	# dADP [intracellular]
	odes['s_0562'] = '-1.0' + ' * ' + r_0360 + ' + ' + '1.0' + ' * ' + r_0568 + ' + ' + '1.0' + ' * ' + r_0951
	# dAMP [intracellular]
	odes['s_0564'] = '1.0' + ' * ' + r_0360 + ' - ' + '0.003587' + ' * ' + r_1812
	# dATP [intracellular]
	odes['s_0566'] = '-1.0' + ' * ' + r_0568 + ' + ' + '1.0' + ' * ' + r_0959
	# dCMP [intracellular]
	odes['s_0569'] = '1.0' + ' * ' + r_0357 + ' - ' + '0.002432' + ' * ' + r_1812
	# decanoate [intracellular]
	odes['s_0574'] = '1.0' + ' * ' + r_0417 + ' - ' + '1.0' + ' * ' + r_0418
	# decanoyl-CoA [intracellular]
	odes['s_0582'] = '1.0' + ' * ' + r_0429 + ' - ' + '1.0' + ' * ' + r_0464
	# dGDP [intracellular]
	odes['s_0591'] = '-1.0' + ' * ' + r_0362 + ' + ' + '1.0' + ' * ' + r_0955
	# dGMP [intracellular]
	odes['s_0593'] = '1.0' + ' * ' + r_0362 + ' - ' + '0.002432' + ' * ' + r_1812
	# diglyceride [intracellular]
	odes['s_0596'] = '-1.0' + ' * ' + r_0370 + ' + ' + '1.0' + ' * ' + r_0371 + ' + ' + '1.0' + ' * ' + r_1040
	# dihydrofolic acid [intracellular]
	odes['s_0601'] = '-1.0' + ' * ' + r_0375 + ' + ' + '1.0' + ' * ' + r_1032
	# diphosphate [intracellular]
	odes['s_0605'] = '-1.0' + ' * ' + r_0127 + ' + ' + '1.0' + ' * ' + r_0220 + ' + ' + '1.0' + ' * ' + r_0226 + ' + ' + '1.0' + ' * ' + r_0229 + ' + ' + '1.0' + ' * ' + r_0245 + ' + ' + '1.0' + ' * ' + r_0284 + ' + ' + '1.0' + ' * ' + r_0387 + ' + ' + '1.0' + ' * ' + r_0437 + ' - ' + '1.0' + ' * ' + r_0439 + ' - ' + '1.0' + ' * ' + r_0442 + ' + ' + '1.0' + ' * ' + r_0496 + ' + ' + '1.0' + ' * ' + r_0514 + ' + ' + '1.0' + ' * ' + r_0551 + ' + ' + '1.0' + ' * ' + r_0562 + ' - ' + '1.0' + ' * ' + r_0610 + ' + ' + '1.0' + ' * ' + r_0650 + ' + ' + '1.0' + ' * ' + r_0697 + ' + ' + '1.0' + ' * ' + r_0701 + ' + ' + '1.0' + ' * ' + r_0793 + ' + ' + '1.0' + ' * ' + r_0882 + ' + ' + '2.0' + ' * ' + r_0993 + ' + ' + '1.0' + ' * ' + r_1072
	# dolichyl D-mannosyl phosphate [intracellular]
	odes['s_0615'] = '1.0' + ' * ' + r_0393 + ' - ' + '1.0' + ' * ' + r_0394
	# dolichyl phosphate [intracellular]
	odes['s_0616'] = '-1.0' + ' * ' + r_0393 + ' + ' + '1.0' + ' * ' + r_0394
	# dTMP [intracellular]
	odes['s_0619'] = '1.0' + ' * ' + r_1032 + ' - ' + '0.003587' + ' * ' + r_1812
	# dUDP [intracellular]
	odes['s_0622'] = '1.0' + ' * ' + r_0957 + ' - ' + '1.0' + ' * ' + r_1066
	# dUMP [intracellular]
	odes['s_0624'] = '-1.0' + ' * ' + r_0357 + ' - ' + '1.0' + ' * ' + r_1032 + ' + ' + '1.0' + ' * ' + r_1066
	# episterol [intracellular]
	odes['s_0627'] = '1.0' + ' * ' + r_0270 + ' - ' + '9.6e-5' + ' * ' + r_1816
	# ergosta-5,7,22,24(28)-tetraen-3beta-ol [intracellular]
	odes['s_0632'] = '-1.0' + ' * ' + r_0271 + ' + ' + '1.0' + ' * ' + r_0298 + ' - ' + '0.000125' + ' * ' + r_1816
	# ergosterol [intracellular]
	odes['s_0635'] = '1.0' + ' * ' + r_0271 + ' - ' + '1.0' + ' * ' + r_0995 + ' - ' + '0.005603' + ' * ' + r_1816
	# ergosterol ester [intracellular]
	odes['s_0641'] = '1.0' + ' * ' + r_0995 + ' - ' + '0.000812' + ' * ' + r_1816
	# ethanol [intracellular]
	odes['s_0650'] = '1.0' + ' * ' + r_0183 + ' - ' + '1.0' + ' * ' + r_1247
	# FAD [intracellular]
	odes['s_0657'] = '1.0' + ' * ' + r_0488 + ' - ' + '1.0' + ' * ' + r_0529
	# FADH2 [intracellular]
	odes['s_0659'] = '-1.0' + ' * ' + r_0488 + ' + ' + '1.0' + ' * ' + r_0529
	# fatty acid [intracellular]
	odes['s_0663'] = '-1.0' + ' * ' + r_0995 + ' + ' + '1.0' + ' * ' + r_1040 + ' - ' + '0.000206' + ' * ' + r_1816
	# fecosterol [intracellular]
	odes['s_0669'] = '-1.0' + ' * ' + r_0270 + ' + ' + '1.0' + ' * ' + r_0967 + ' - ' + '0.000114' + ' * ' + r_1816
	# formate [intracellular]
	odes['s_0689'] = '1.0' + ' * ' + r_0040 + ' + ' + '1.0' + ' * ' + r_0347 + ' - ' + '1.0' + ' * ' + r_0479 + ' + ' + '1.0' + ' * ' + r_0562
	# fumarate(2-) [intracellular]
	odes['s_0692'] = '1.0' + ' * ' + r_0169 + ' + ' + '1.0' + ' * ' + r_0171 + ' + ' + '1.0' + ' * ' + r_0225 + ' + ' + '1.0' + ' * ' + r_0485 + ' - ' + '1.0' + ' * ' + r_0488
	# GDP [intracellular]
	odes['s_0706'] = '-1.0' + ' * ' + r_0165 + ' + ' + '1.0' + ' * ' + r_0170 + ' + ' + '1.0' + ' * ' + r_0393 + ' + ' + '1.0' + ' * ' + r_0567 + ' + ' + '1.0' + ' * ' + r_0568 + ' - ' + '1.0' + ' * ' + r_0955
	# GDP-alpha-D-mannose [intracellular]
	odes['s_0710'] = '-1.0' + ' * ' + r_0393 + ' + ' + '1.0' + ' * ' + r_0697 + ' - ' + '1.0' + ' * ' + r_0723
	# geranyl diphosphate [intracellular]
	odes['s_0712'] = '1.0' + ' * ' + r_0387 + ' - ' + '1.0' + ' * ' + r_0496
	# glyceraldehyde 3-phosphate [intracellular]
	odes['s_0731'] = '1.0' + ' * ' + r_0484 + ' - ' + '1.0' + ' * ' + r_0525 + ' + ' + '1.0' + ' * ' + r_1035 + ' - ' + '1.0' + ' * ' + r_1036 + ' - ' + '1.0' + ' * ' + r_1037 + ' + ' + '1.0' + ' * ' + r_1041 + ' + ' + '1.0' + ' * ' + r_1042
	# glycerol [intracellular]
	odes['s_0732'] = '-1.0' + ' * ' + r_0526 + ' + ' + '1.0' + ' * ' + r_0528
	# glycerone [intracellular]
	odes['s_0734'] = '-1.0' + ' * ' + r_0386 + ' + ' + '1.0' + ' * ' + r_0526
	# glycerone phosphate [intracellular]
	odes['s_0735'] = '1.0' + ' * ' + r_0386 + ' + ' + '1.0' + ' * ' + r_0484 + ' + ' + '1.0' + ' * ' + r_0529 + ' - ' + '1.0' + ' * ' + r_0530 + ' - ' + '1.0' + ' * ' + r_1041
	# glycine [intracellular]
	odes['s_0740'] = '1.0' + ' * ' + r_0174 + ' - ' + '1.0' + ' * ' + r_0538 + ' - ' + '1.0' + ' * ' + r_0539 + ' - ' + '1.0' + ' * ' + r_0890 + ' + ' + '1.0' + ' * ' + r_1026 + ' - ' + '0.32518' + ' * ' + r_1812
	# glycogen [intracellular]
	odes['s_0743'] = '1.0' + ' * ' + r_0006 + ' - ' + '0.51852' + ' * ' + r_1812
	# glyoxylate [intracellular]
	odes['s_0749'] = '-1.0' + ' * ' + r_0174 + ' + ' + '1.0' + ' * ' + r_0633
	# GMP [intracellular]
	odes['s_0752'] = '1.0' + ' * ' + r_0551 + ' - ' + '1.0' + ' * ' + r_0567 + ' - ' + '1.0' + ' * ' + r_0568 + ' - ' + '0.051' + ' * ' + r_1812
	# GTP [intracellular]
	odes['s_0755'] = '1.0' + ' * ' + r_0165 + ' - ' + '1.0' + ' * ' + r_0170 + ' - ' + '1.0' + ' * ' + r_0562 + ' - ' + '1.0' + ' * ' + r_0697
	# homocitrate(3-) [intracellular]
	odes['s_0798'] = '-1.0' + ' * ' + r_0029 + ' + ' + '1.0' + ' * ' + r_0582
	# homoisocitrate(3-) [intracellular]
	odes['s_0800'] = '1.0' + ' * ' + r_0581 + ' - ' + '1.0' + ' * ' + r_0585
	# hydrogen peroxide [intracellular]
	odes['s_0801'] = '-2.0' + ' * ' + r_0282 + ' + ' + '1.0' + ' * ' + r_0374
	# hydrogen sulfide [intracellular]
	odes['s_0805'] = '-1.0' + ' * ' + r_0783 + ' + ' + '1.0' + ' * ' + r_1008
	# IMP [intracellular]
	odes['s_0816'] = '-1.0' + ' * ' + r_0170 + ' + ' + '1.0' + ' * ' + r_0606 + ' - ' + '1.0' + ' * ' + r_0607
	# inositol phosphomannosylinositol phosphoceramide [intracellular]
	odes['s_0824'] = '1.0' + ' * ' + r_0618 + ' - ' + '0.000417' + ' * ' + r_1816
	# inositol-P-ceramide B [intracellular]
	odes['s_0828'] = '1.0' + ' * ' + r_0621 + ' - ' + '1.0' + ' * ' + r_0723
	# isocitrate(3-) [intracellular]
	odes['s_0847'] = '1.0' + ' * ' + r_0307 + ' - ' + '1.0' + ' * ' + r_0630 + ' - ' + '1.0' + ' * ' + r_0633
	# isopentenyl diphosphate [intracellular]
	odes['s_0850'] = '-1.0' + ' * ' + r_0387 + ' - ' + '1.0' + ' * ' + r_0496 + ' - ' + '1.0' + ' * ' + r_0638 + ' + ' + '1.0' + ' * ' + r_0715
	# keto-phenylpyruvate [intracellular]
	odes['s_0859'] = '-1.0' + ' * ' + r_0825 + ' + ' + '1.0' + ' * ' + r_0911
	# L-2-aminoadipate(2-) [intracellular]
	odes['s_0861'] = '1.0' + ' * ' + r_0018 + ' - ' + '1.0' + ' * ' + r_0650
	# L-alanine [intracellular]
	odes['s_0863'] = '-1.0' + ' * ' + r_0174 + ' + ' + '1.0' + ' * ' + r_0647 + ' - ' + '0.35734' + ' * ' + r_1812
	# L-allysine [intracellular]
	odes['s_0867'] = '1.0' + ' * ' + r_0650 + ' - ' + '1.0' + ' * ' + r_0970
	# L-arginine [intracellular]
	odes['s_0873'] = '1.0' + ' * ' + r_0225 + ' - ' + '0.13579' + ' * ' + r_1812
	# L-asparagine [intracellular]
	odes['s_0877'] = '1.0' + ' * ' + r_0229 + ' - ' + '0.17152' + ' * ' + r_1812
	# L-aspartate [intracellular]
	odes['s_0881'] = '-1.0' + ' * ' + r_0170 + ' - ' + '1.0' + ' * ' + r_0226 + ' - ' + '1.0' + ' * ' + r_0229 + ' - ' + '1.0' + ' * ' + r_0232 + ' - ' + '1.0' + ' * ' + r_0233 + ' + ' + '1.0' + ' * ' + r_0235 + ' - ' + '1.0' + ' * ' + r_0886 + ' - ' + '0.17152' + ' * ' + r_1812
	# L-aspartate 4-semialdehyde [intracellular]
	odes['s_0886'] = '1.0' + ' * ' + r_0238 + ' - ' + '1.0' + ' * ' + r_0586
	# L-citrulline [intracellular]
	odes['s_0887'] = '-1.0' + ' * ' + r_0226 + ' + ' + '1.0' + ' * ' + r_0789
	# L-cystathionine [intracellular]
	odes['s_0888'] = '1.0' + ' * ' + r_0338 + ' - ' + '1.0' + ' * ' + r_0339 + ' + ' + '1.0' + ' * ' + r_0340
	# L-cysteine [intracellular]
	odes['s_0889'] = '1.0' + ' * ' + r_0339 + ' - ' + '1.0' + ' * ' + r_0340 + ' - ' + '0.04288' + ' * ' + r_1812
	# L-gamma-glutamyl phosphate [intracellular]
	odes['s_0894'] = '1.0' + ' * ' + r_0506 + ' - ' + '1.0' + ' * ' + r_0512
	# L-glutamate [intracellular]
	odes['s_0899'] = '-1.0' + ' * ' + r_0018 + ' - ' + '1.0' + ' * ' + r_0133 + ' + ' + '1.0' + ' * ' + r_0221 + ' + ' + '1.0' + ' * ' + r_0229 + ' - ' + '1.0' + ' * ' + r_0235 + ' + ' + '1.0' + ' * ' + r_0277 + ' - ' + '1.0' + ' * ' + r_0506 + ' + ' + '1.0' + ' * ' + r_0509 + ' + ' + '2.0' + ' * ' + r_0510 + ' + ' + '1.0' + ' * ' + r_0514 + ' - ' + '1.0' + ' * ' + r_0515 + ' + ' + '1.0' + ' * ' + r_0551 + ' - ' + '1.0' + ' * ' + r_0577 + ' + ' + '1.0' + ' * ' + r_0604 + ' - ' + '1.0' + ' * ' + r_0634 + ' - ' + '1.0' + ' * ' + r_0647 + ' - ' + '1.0' + ' * ' + r_0674 + ' - ' + '1.0' + ' * ' + r_0791 + ' - ' + '1.0' + ' * ' + r_0825 + ' + ' + '1.0' + ' * ' + r_0888 + ' - ' + '1.0' + ' * ' + r_0970 + ' - ' + '1.0' + ' * ' + r_1050 + ' - ' + '1.0' + ' * ' + r_1073 + ' - ' + '0.268' + ' * ' + r_1812
	# L-glutamic 5-semialdehyde [intracellular]
	odes['s_0905'] = '1.0' + ' * ' + r_0512 + ' - ' + '1.0' + ' * ' + r_0657
	# L-glutamine [intracellular]
	odes['s_0907'] = '-1.0' + ' * ' + r_0221 + ' - ' + '1.0' + ' * ' + r_0229 + ' - ' + '1.0' + ' * ' + r_0277 + ' - ' + '1.0' + ' * ' + r_0510 + ' - ' + '1.0' + ' * ' + r_0514 + ' + ' + '1.0' + ' * ' + r_0515 + ' - ' + '1.0' + ' * ' + r_0551 + ' - ' + '1.0' + ' * ' + r_0604 + ' - ' + '1.0' + ' * ' + r_0888 + ' - ' + '0.268' + ' * ' + r_1812
	# L-histidine [intracellular]
	odes['s_0911'] = '1.0' + ' * ' + r_0575 + ' - ' + '0.075041' + ' * ' + r_1812
	# L-histidinol [intracellular]
	odes['s_0915'] = '-1.0' + ' * ' + r_0575 + ' + ' + '1.0' + ' * ' + r_0576
	# L-histidinol phosphate [intracellular]
	odes['s_0916'] = '-1.0' + ' * ' + r_0576 + ' + ' + '1.0' + ' * ' + r_0577
	# L-homocysteine [intracellular]
	odes['s_0917'] = '1.0' + ' * ' + r_0159 + ' - ' + '1.0' + ' * ' + r_0338 + ' - ' + '1.0' + ' * ' + r_0702 + ' + ' + '1.0' + ' * ' + r_0783
	# L-homoserine [intracellular]
	odes['s_0919'] = '1.0' + ' * ' + r_0586 + ' - ' + '1.0' + ' * ' + r_0588 + ' - ' + '1.0' + ' * ' + r_0589
	# L-isoleucine [intracellular]
	odes['s_0920'] = '1.0' + ' * ' + r_0634 + ' - ' + '0.17152' + ' * ' + r_1812
	# L-leucine [intracellular]
	odes['s_0925'] = '1.0' + ' * ' + r_0674 + ' - ' + '0.25014' + ' * ' + r_1812
	# L-lysine [intracellular]
	odes['s_0929'] = '1.0' + ' * ' + r_0969 + ' - ' + '0.23942' + ' * ' + r_1812
	# L-methionine [intracellular]
	odes['s_0933'] = '-1.0' + ' * ' + r_0701 + ' + ' + '1.0' + ' * ' + r_0702 + ' - ' + '0.050027' + ' * ' + r_1812
	# L-phenylalanine [intracellular]
	odes['s_0936'] = '1.0' + ' * ' + r_0825 + ' - ' + '0.11435' + ' * ' + r_1812
	# L-proline [intracellular]
	odes['s_0939'] = '1.0' + ' * ' + r_0936 + ' - ' + '0.12864' + ' * ' + r_1812
	# L-saccharopine [intracellular]
	odes['s_0942'] = '-1.0' + ' * ' + r_0969 + ' + ' + '1.0' + ' * ' + r_0970
	# L-serine [intracellular]
	odes['s_0943'] = '-1.0' + ' * ' + r_0338 + ' + ' + '1.0' + ' * ' + r_0539 + ' - ' + '1.0' + ' * ' + r_0853 + ' - ' + '1.0' + ' * ' + r_0972 + ' - ' + '1.0' + ' * ' + r_1042 + ' - ' + '0.25371' + ' * ' + r_1812
	# L-threonine [intracellular]
	odes['s_0949'] = '-1.0' + ' * ' + r_0667 + ' - ' + '1.0' + ' * ' + r_1026 + ' + ' + '1.0' + ' * ' + r_1027 + ' - ' + '0.19653' + ' * ' + r_1812
	# L-tryptophan [intracellular]
	odes['s_0952'] = '1.0' + ' * ' + r_1042 + ' - ' + '0.028' + ' * ' + r_1812
	# L-tyrosine [intracellular]
	odes['s_0955'] = '1.0' + ' * ' + r_1050 + ' - ' + '0.096481' + ' * ' + r_1812
	# L-valine [intracellular]
	odes['s_0960'] = '1.0' + ' * ' + r_1073 + ' - ' + '0.25728' + ' * ' + r_1812
	# lanosterol [intracellular]
	odes['s_0963'] = '-1.0' + ' * ' + r_0347 + ' + ' + '1.0' + ' * ' + r_0673 + ' - ' + '3.2e-5' + ' * ' + r_1816
	# laurate [intracellular]
	odes['s_0968'] = '1.0' + ' * ' + r_0418 + ' - ' + '1.0' + ' * ' + r_0419
	# lauroyl-CoA [intracellular]
	odes['s_0977'] = '1.0' + ' * ' + r_0464 + ' - ' + '1.0' + ' * ' + r_0465
	# lignocerate [intracellular]
	odes['s_0987'] = '1.0' + ' * ' + r_0425 + ' - ' + '1.0' + ' * ' + r_0437
	# lipid [intracellular]
	odes['s_1000'] = '0'
	# malonyl-CoA [intracellular]
	odes['s_1005'] = '1.0' + ' * ' + r_0123 + ' - ' + '1.0' + ' * ' + r_0417 + ' - ' + '1.0' + ' * ' + r_0418 + ' - ' + '1.0' + ' * ' + r_0419 + ' - ' + '1.0' + ' * ' + r_0421 + ' - ' + '1.0' + ' * ' + r_0423 + ' - ' + '3.0' + ' * ' + r_0425 + ' - ' + '1.0' + ' * ' + r_0429 + ' - ' + '3.0' + ' * ' + r_0430 + ' - ' + '1.0' + ' * ' + r_0464 + ' - ' + '1.0' + ' * ' + r_0465 + ' - ' + '1.0' + ' * ' + r_0466 + ' - ' + '1.0' + ' * ' + r_0467
	# mannan [intracellular]
	odes['s_1011'] = '1.0' + ' * ' + r_0394 + ' - ' + '0.82099' + ' * ' + r_1812
	# mannosylinositol phosphorylceramide [intracellular]
	odes['s_1013'] = '-1.0' + ' * ' + r_0618 + ' + ' + '1.0' + ' * ' + r_0723
	# myo-inositol [intracellular]
	odes['s_1020'] = '1.0' + ' * ' + r_0725 + ' - ' + '1.0' + ' * ' + r_0847
	# myristate [intracellular]
	odes['s_1028'] = '1.0' + ' * ' + r_0419 + ' - ' + '1.0' + ' * ' + r_0421
	# myristoyl-CoA [intracellular]
	odes['s_1044'] = '1.0' + ' * ' + r_0465 + ' - ' + '1.0' + ' * ' + r_0466
	# N(1)-(5-phospho-D-ribosyl)glycinamide [intracellular]
	odes['s_1048'] = '-1.0' + ' * ' + r_0889 + ' + ' + '1.0' + ' * ' + r_0890
	# N(2)-acetyl-L-ornithine [intracellular]
	odes['s_1051'] = '1.0' + ' * ' + r_0133 + ' - ' + '1.0' + ' * ' + r_0791
	# N(2)-formyl-N(1)-(5-phospho-D-ribosyl)glycinamide [intracellular]
	odes['s_1052'] = '-1.0' + ' * ' + r_0888 + ' + ' + '1.0' + ' * ' + r_0889
	# N(6)-(1,2-dicarboxyethyl)-AMP [intracellular]
	odes['s_1053'] = '1.0' + ' * ' + r_0170 + ' - ' + '1.0' + ' * ' + r_0171
	# N-(24-hydroxytetracosanyl)sphinganine [intracellular]
	odes['s_1060'] = '1.0' + ' * ' + r_0287 + ' - ' + '1.0' + ' * ' + r_0621
	# N-(5-phospho-beta-D-ribosyl)anthranilate [intracellular]
	odes['s_1066'] = '1.0' + ' * ' + r_0220 + ' - ' + '1.0' + ' * ' + r_0887
	# N-acetyl-L-gamma-glutamyl phosphate [intracellular]
	odes['s_1070'] = '1.0' + ' * ' + r_0130 + ' - ' + '1.0' + ' * ' + r_0728
	# N-acetyl-L-glutamate(2-) [intracellular]
	odes['s_1071'] = '-1.0' + ' * ' + r_0130 + ' + ' + '1.0' + ' * ' + r_0791
	# N-carbamoyl-L-aspartate [intracellular]
	odes['s_1073'] = '1.0' + ' * ' + r_0232 + ' - ' + '1.0' + ' * ' + r_0381
	# N-tetracosanylsphinganine [intracellular]
	odes['s_1080'] = '-1.0' + ' * ' + r_0287 + ' + ' + '1.0' + ' * ' + r_0290
	# NAD(+) [intracellular]
	odes['s_1082'] = '1.0' + ' * ' + r_0057 + ' + ' + '1.0' + ' * ' + r_0058 + ' + ' + '1.0' + ' * ' + r_0059 + ' + ' + '1.0' + ' * ' + r_0060 + ' - ' + '1.0' + ' * ' + r_0064 + ' + ' + '1.0' + ' * ' + r_0183 + ' - ' + '1.0' + ' * ' + r_0262 + ' + ' + '3.0' + ' * ' + r_0347 + ' + ' + '1.0' + ' * ' + r_0351 + ' + ' + '1.0' + ' * ' + r_0510 + ' + ' + '1.0' + ' * ' + r_0512 + ' - ' + '1.0' + ' * ' + r_0525 + ' + ' + '1.0' + ' * ' + r_0530 + ' - ' + '1.0' + ' * ' + r_0538 + ' - ' + '2.0' + ' * ' + r_0575 + ' - ' + '1.0' + ' * ' + r_0585 + ' + ' + '1.0' + ' * ' + r_0586 + ' - ' + '1.0' + ' * ' + r_0607 + ' + ' + '1.0' + ' * ' + r_0650 + ' + ' + '1.0' + ' * ' + r_0661 + ' + ' + '1.0' + ' * ' + r_0688 + ' - ' + '1.0' + ' * ' + r_0940 + ' - ' + '1.0' + ' * ' + r_0969 + ' + ' + '1.0' + ' * ' + r_0991
	# NADH [intracellular]
	odes['s_1087'] = '-1.0' + ' * ' + r_0057 + ' - ' + '1.0' + ' * ' + r_0058 + ' - ' + '1.0' + ' * ' + r_0059 + ' - ' + '1.0' + ' * ' + r_0060 + ' + ' + '1.0' + ' * ' + r_0064 + ' - ' + '1.0' + ' * ' + r_0183 + ' + ' + '1.0' + ' * ' + r_0262 + ' - ' + '3.0' + ' * ' + r_0347 + ' - ' + '1.0' + ' * ' + r_0351 + ' - ' + '1.0' + ' * ' + r_0510 + ' - ' + '1.0' + ' * ' + r_0512 + ' + ' + '1.0' + ' * ' + r_0525 + ' - ' + '1.0' + ' * ' + r_0530 + ' + ' + '1.0' + ' * ' + r_0538 + ' + ' + '2.0' + ' * ' + r_0575 + ' + ' + '1.0' + ' * ' + r_0585 + ' - ' + '1.0' + ' * ' + r_0586 + ' + ' + '1.0' + ' * ' + r_0607 + ' - ' + '1.0' + ' * ' + r_0650 + ' - ' + '1.0' + ' * ' + r_0661 + ' - ' + '1.0' + ' * ' + r_0688 + ' + ' + '1.0' + ' * ' + r_0940 + ' + ' + '1.0' + ' * ' + r_0969 + ' - ' + '1.0' + ' * ' + r_0991
	# NADP(+) [intracellular]
	odes['s_1091'] = '1.0' + ' * ' + r_0015 + ' + ' + '1.0' + ' * ' + r_0044 + ' + ' + '1.0' + ' * ' + r_0093 + ' + ' + '1.0' + ' * ' + r_0111 + ' - ' + '1.0' + ' * ' + r_0191 + ' + ' + '1.0' + ' * ' + r_0238 + ' + ' + '1.0' + ' * ' + r_0258 + ' - ' + '1.0' + ' * ' + r_0261 + ' + ' + '1.0' + ' * ' + r_0263 + ' + ' + '1.0' + ' * ' + r_0264 + ' + ' + '1.0' + ' * ' + r_0265 + ' + ' + '1.0' + ' * ' + r_0266 + ' + ' + '1.0' + ' * ' + r_0267 + ' + ' + '3.0' + ' * ' + r_0268 + ' + ' + '1.0' + ' * ' + r_0271 + ' + ' + '1.0' + ' * ' + r_0287 + ' - ' + '1.0' + ' * ' + r_0352 + ' + ' + '1.0' + ' * ' + r_0375 + ' + ' + '2.0' + ' * ' + r_0417 + ' + ' + '2.0' + ' * ' + r_0418 + ' + ' + '2.0' + ' * ' + r_0419 + ' + ' + '2.0' + ' * ' + r_0421 + ' + ' + '2.0' + ' * ' + r_0423 + ' + ' + '6.0' + ' * ' + r_0425 + ' + ' + '2.0' + ' * ' + r_0429 + ' + ' + '6.0' + ' * ' + r_0430 + ' + ' + '2.0' + ' * ' + r_0464 + ' + ' + '2.0' + ' * ' + r_0465 + ' + ' + '2.0' + ' * ' + r_0466 + ' + ' + '2.0' + ' * ' + r_0467 + ' + ' + '1.0' + ' * ' + r_0509 + ' - ' + '1.0' + ' * ' + r_0526 + ' + ' + '2.0' + ' * ' + r_0598 + ' - ' + '1.0' + ' * ' + r_0630 + ' + ' + '1.0' + ' * ' + r_0640 + ' - ' + '1.0' + ' * ' + r_0660 + ' - ' + '1.0' + ' * ' + r_0707 + ' - ' + '1.0' + ' * ' + r_0719 + ' - ' + '1.0' + ' * ' + r_0720 + ' - ' + '1.0' + ' * ' + r_0721 + ' - ' + '1.0' + ' * ' + r_0722 + ' + ' + '1.0' + ' * ' + r_0728 + ' - ' + '1.0' + ' * ' + r_0913 + ' + ' + '1.0' + ' * ' + r_0936 + ' + ' + '1.0' + ' * ' + r_0970 + ' + ' + '1.0' + ' * ' + r_0976 + ' + ' + '1.0' + ' * ' + r_0993 + ' + ' + '3.0' + ' * ' + r_1008 + ' + ' + '1.0' + ' * ' + r_1024
	# NADPH [intracellular]
	odes['s_1096'] = '-1.0' + ' * ' + r_0015 + ' - ' + '1.0' + ' * ' + r_0044 + ' - ' + '1.0' + ' * ' + r_0093 + ' - ' + '1.0' + ' * ' + r_0111 + ' + ' + '1.0' + ' * ' + r_0191 + ' - ' + '1.0' + ' * ' + r_0238 + ' - ' + '1.0' + ' * ' + r_0258 + ' + ' + '1.0' + ' * ' + r_0261 + ' - ' + '1.0' + ' * ' + r_0263 + ' - ' + '1.0' + ' * ' + r_0264 + ' - ' + '1.0' + ' * ' + r_0265 + ' - ' + '1.0' + ' * ' + r_0266 + ' - ' + '1.0' + ' * ' + r_0267 + ' - ' + '3.0' + ' * ' + r_0268 + ' - ' + '1.0' + ' * ' + r_0271 + ' - ' + '1.0' + ' * ' + r_0287 + ' + ' + '1.0' + ' * ' + r_0352 + ' - ' + '1.0' + ' * ' + r_0375 + ' - ' + '2.0' + ' * ' + r_0417 + ' - ' + '2.0' + ' * ' + r_0418 + ' - ' + '2.0' + ' * ' + r_0419 + ' - ' + '2.0' + ' * ' + r_0421 + ' - ' + '2.0' + ' * ' + r_0423 + ' - ' + '6.0' + ' * ' + r_0425 + ' - ' + '2.0' + ' * ' + r_0429 + ' - ' + '6.0' + ' * ' + r_0430 + ' - ' + '2.0' + ' * ' + r_0464 + ' - ' + '2.0' + ' * ' + r_0465 + ' - ' + '2.0' + ' * ' + r_0466 + ' - ' + '2.0' + ' * ' + r_0467 + ' - ' + '1.0' + ' * ' + r_0509 + ' + ' + '1.0' + ' * ' + r_0526 + ' - ' + '2.0' + ' * ' + r_0598 + ' + ' + '1.0' + ' * ' + r_0630 + ' - ' + '1.0' + ' * ' + r_0640 + ' + ' + '1.0' + ' * ' + r_0660 + ' + ' + '1.0' + ' * ' + r_0707 + ' + ' + '1.0' + ' * ' + r_0719 + ' + ' + '1.0' + ' * ' + r_0720 + ' + ' + '1.0' + ' * ' + r_0721 + ' + ' + '1.0' + ' * ' + r_0722 + ' - ' + '1.0' + ' * ' + r_0728 + ' + ' + '1.0' + ' * ' + r_0913 + ' - ' + '1.0' + ' * ' + r_0936 + ' - ' + '1.0' + ' * ' + r_0970 + ' - ' + '1.0' + ' * ' + r_0976 + ' - ' + '1.0' + ' * ' + r_0993 + ' - ' + '3.0' + ' * ' + r_1008 + ' - ' + '1.0' + ' * ' + r_1024
	# O-acetyl-L-homoserine [intracellular]
	odes['s_1117'] = '-1.0' + ' * ' + r_0340 + ' + ' + '1.0' + ' * ' + r_0589 + ' - ' + '1.0' + ' * ' + r_0783
	# O-phospho-L-homoserine [intracellular]
	odes['s_1122'] = '1.0' + ' * ' + r_0588 + ' - ' + '1.0' + ' * ' + r_1027
	# octanoate [intracellular]
	odes['s_1132'] = '-1.0' + ' * ' + r_0417 + ' + ' + '1.0' + ' * ' + r_0442
	# octanoyl-CoA [intracellular]
	odes['s_1140'] = '-1.0' + ' * ' + r_0429 + ' + ' + '1.0' + ' * ' + r_0430 + ' - ' + '1.0' + ' * ' + r_0442
	# ornithine [intracellular]
	odes['s_1151'] = '-1.0' + ' * ' + r_0789 + ' + ' + '1.0' + ' * ' + r_0791
	# orotate [intracellular]
	odes['s_1154'] = '1.0' + ' * ' + r_0374 + ' - ' + '1.0' + ' * ' + r_0793
	# orotidine 5'-(dihydrogen phosphate) [intracellular]
	odes['s_1155'] = '1.0' + ' * ' + r_0793 + ' - ' + '1.0' + ' * ' + r_0794
	# oxaloacetate(2-) [intracellular]
	odes['s_1156'] = '-1.0' + ' * ' + r_0235 + ' - ' + '1.0' + ' * ' + r_0328 + ' - ' + '1.0' + ' * ' + r_0688 + ' + ' + '1.0' + ' * ' + r_0937
	# oxygen [intracellular]
	odes['s_1160'] = '-1.0' + ' * ' + r_0265 + ' - ' + '1.0' + ' * ' + r_0266 + ' - ' + '1.0' + ' * ' + r_0267 + ' - ' + '3.0' + ' * ' + r_0268 + ' + ' + '1.0' + ' * ' + r_0282 + ' - ' + '1.0' + ' * ' + r_0287 + ' - ' + '1.0' + ' * ' + r_0298 + ' - ' + '3.0' + ' * ' + r_0347 + ' - ' + '1.0' + ' * ' + r_0374 + ' - ' + '1.0' + ' * ' + r_0991 + ' + ' + '1.0' + ' * ' + r_1435
	# palmitate [intracellular]
	odes['s_1170'] = '1.0' + ' * ' + r_0421 + ' - ' + '1.0' + ' * ' + r_0423
	# palmitoyl-CoA [intracellular]
	odes['s_1187'] = '1.0' + ' * ' + r_0466 + ' - ' + '1.0' + ' * ' + r_0467 + ' - ' + '1.0' + ' * ' + r_0972
	# phosphate [intracellular]
	odes['s_1207'] = '0'
	# phosphatidate [intracellular]
	odes['s_1215'] = '1.0' + ' * ' + r_0009 + ' - ' + '1.0' + ' * ' + r_0284 + ' - ' + '1.0' + ' * ' + r_0371
	# phosphatidyl-L-serine [intracellular]
	odes['s_1219'] = '-1.0' + ' * ' + r_0850 + ' + ' + '1.0' + ' * ' + r_0853 + ' - ' + '0.000373' + ' * ' + r_1816
	# phosphatidyl-N,N-dimethylethanolamine [intracellular]
	odes['s_1225'] = '-1.0' + ' * ' + r_0873 + ' + ' + '1.0' + ' * ' + r_0874
	# phosphatidyl-N-methylethanolamine [intracellular]
	odes['s_1226'] = '1.0' + ' * ' + r_0831 + ' - ' + '1.0' + ' * ' + r_0874
	# phosphatidylcholine [intracellular]
	odes['s_1228'] = '1.0' + ' * ' + r_0873 + ' - ' + '0.002884' + ' * ' + r_1816
	# phosphatidylethanolamine [intracellular]
	odes['s_1233'] = '-1.0' + ' * ' + r_0831 + ' + ' + '1.0' + ' * ' + r_0850 + ' - ' + '0.000697' + ' * ' + r_1816
	# phosphoenolpyruvate [intracellular]
	odes['s_1243'] = '-1.0' + ' * ' + r_0021 + ' - ' + '1.0' + ' * ' + r_0068 + ' + ' + '1.0' + ' * ' + r_0398 + ' - ' + '1.0' + ' * ' + r_0941
	# prenyl diphosphate [intracellular]
	odes['s_1257'] = '-1.0' + ' * ' + r_0387 + ' + ' + '1.0' + ' * ' + r_0638
	# prephenate(2-) [intracellular]
	odes['s_1258'] = '1.0' + ' * ' + r_0304 + ' - ' + '1.0' + ' * ' + r_0911 + ' - ' + '1.0' + ' * ' + r_0913
	# pyruvate [intracellular]
	odes['s_1277'] = '-1.0' + ' * ' + r_0016 + ' - ' + '2.0' + ' * ' + r_0112 + ' + ' + '1.0' + ' * ' + r_0174 + ' + ' + '1.0' + ' * ' + r_0221 + ' - ' + '1.0' + ' * ' + r_0647 + ' - ' + '1.0' + ' * ' + r_0937 + ' - ' + '1.0' + ' * ' + r_0938 + ' - ' + '1.0' + ' * ' + r_0940 + ' + ' + '1.0' + ' * ' + r_0941
	# riboflavin [intracellular]
	odes['s_1283'] = '1.0' + ' * ' + r_0949 + ' - ' + '0.0009' + ' * ' + r_1812
	# S-adenosyl-L-homocysteine [intracellular]
	odes['s_1290'] = '-1.0' + ' * ' + r_0159 + ' + ' + '1.0' + ' * ' + r_0298 + ' + ' + '1.0' + ' * ' + r_0831 + ' + ' + '1.0' + ' * ' + r_0873 + ' + ' + '1.0' + ' * ' + r_0874 + ' + ' + '1.0' + ' * ' + r_0967
	# S-adenosyl-L-methionine [intracellular]
	odes['s_1293'] = '-1.0' + ' * ' + r_0298 + ' + ' + '1.0' + ' * ' + r_0701 + ' - ' + '1.0' + ' * ' + r_0831 + ' - ' + '1.0' + ' * ' + r_0873 + ' - ' + '1.0' + ' * ' + r_0874 + ' - ' + '1.0' + ' * ' + r_0967
	# sedoheptulose 7-phosphate [intracellular]
	odes['s_1304'] = '1.0' + ' * ' + r_1035 + ' - ' + '1.0' + ' * ' + r_1036
	# shikimate [intracellular]
	odes['s_1306'] = '1.0' + ' * ' + r_0976 + ' - ' + '1.0' + ' * ' + r_0977
	# sn-glycerol 3-phosphate [intracellular]
	odes['s_1315'] = '-1.0' + ' * ' + r_0528 + ' - ' + '1.0' + ' * ' + r_0529 + ' + ' + '1.0' + ' * ' + r_0530 + ' - ' + '1.0' + ' * ' + r_0534
	# sphinganine [intracellular]
	odes['s_1325'] = '1.0' + ' * ' + r_0044 + ' - ' + '1.0' + ' * ' + r_0290
	# squalene [intracellular]
	odes['s_1327'] = '-1.0' + ' * ' + r_0991 + ' + ' + '1.0' + ' * ' + r_0993
	# stearate [intracellular]
	odes['s_1329'] = '1.0' + ' * ' + r_0423 + ' - ' + '1.0' + ' * ' + r_0425 + ' + ' + '1.0' + ' * ' + r_0439
	# stearoyl-CoA [intracellular]
	odes['s_1334'] = '-1.0' + ' * ' + r_0439 + ' + ' + '1.0' + ' * ' + r_0467
	# succinate(2-) [intracellular]
	odes['s_1338'] = '1.0' + ' * ' + r_0488 + ' + ' + '1.0' + ' * ' + r_0633 + ' - ' + '1.0' + ' * ' + r_1003 + ' - ' + '1.0' + ' * ' + r_1503
	# succinyl-CoA [intracellular]
	odes['s_1342'] = '1.0' + ' * ' + r_1003 + ' - ' + '1.0' + ' * ' + r_1672
	# sulphate [intracellular]
	odes['s_1347'] = '-1.0' + ' * ' + r_1007 + ' + ' + '1.0' + ' * ' + r_1507 + ' - ' + '0.02' + ' * ' + r_1812
	# sulphite [intracellular]
	odes['s_1349'] = '1.0' + ' * ' + r_0856 + ' - ' + '1.0' + ' * ' + r_1008
	# tetracosanoyl-CoA [intracellular]
	odes['s_1355'] = '-1.0' + ' * ' + r_0290 + ' + ' + '1.0' + ' * ' + r_0437
	# trans-4-hydroxy-L-proline [intracellular]
	odes['s_1379'] = '-1.0' + ' * ' + r_0660 + ' + ' + '1.0' + ' * ' + r_0661
	# triglyceride [intracellular]
	odes['s_1399'] = '0'
	# UDP [intracellular]
	odes['s_1411'] = '1.0' + ' * ' + r_0005 + ' + ' + '1.0' + ' * ' + r_0213 + ' + ' + '1.0' + ' * ' + r_0547 + ' - ' + '1.0' + ' * ' + r_0779 + ' - ' + '1.0' + ' * ' + r_0957 + ' + ' + '1.0' + ' * ' + r_1059
	# UDP-D-glucose [intracellular]
	odes['s_1415'] = '-1.0' + ' * ' + r_0005 + ' - ' + '1.0' + ' * ' + r_0213 + ' - ' + '1.0' + ' * ' + r_0547 + ' + ' + '1.0' + ' * ' + r_1072
	# UMP [intracellular]
	odes['s_1417'] = '1.0' + ' * ' + r_0794 + ' - ' + '1.0' + ' * ' + r_1059 + ' - ' + '0.067' + ' * ' + r_1812
	# UTP [intracellular]
	odes['s_1430'] = '-1.0' + ' * ' + r_0336 + ' + ' + '1.0' + ' * ' + r_0779 + ' - ' + '1.0' + ' * ' + r_1072
	# zymosterol [intracellular]
	odes['s_1447'] = '1.0' + ' * ' + r_0264 + ' - ' + '1.0' + ' * ' + r_0298 + ' - ' + '1.0' + ' * ' + r_0967 + ' - ' + '1.5e-5' + ' * ' + r_1816
	# zymosterol intermediate 1a [intracellular]
	odes['s_1455'] = '1.0' + ' * ' + r_0265 + ' - ' + '1.0' + ' * ' + r_0266
	# zymosterol intermediate 1b [intracellular]
	odes['s_1456'] = '1.0' + ' * ' + r_0266 + ' - ' + '1.0' + ' * ' + r_0267
	# zymosterol intermediate 1c [intracellular]
	odes['s_1457'] = '-1.0' + ' * ' + r_0261 + ' + ' + '1.0' + ' * ' + r_0267
	# zymosterol intermediate 2 [intracellular]
	odes['s_1458'] = '1.0' + ' * ' + r_0261 + ' - ' + '1.0' + ' * ' + r_0264
	# thioredoxin disulfide [intracellular]
	odes['s_1517'] = '1.0' + ' * ' + r_0856 + ' + ' + '1.0' + ' * ' + r_0951 + ' + ' + '1.0' + ' * ' + r_0955 + ' + ' + '1.0' + ' * ' + r_0957 + ' + ' + '1.0' + ' * ' + r_0959 + ' - ' + '1.0' + ' * ' + r_1024
	# thioredoxin dithiol [intracellular]
	odes['s_1521'] = '-1.0' + ' * ' + r_0856 + ' - ' + '1.0' + ' * ' + r_0951 + ' - ' + '1.0' + ' * ' + r_0955 + ' - ' + '1.0' + ' * ' + r_0957 + ' - ' + '1.0' + ' * ' + r_0959 + ' + ' + '1.0' + ' * ' + r_1024
	# H+ [intracellular]
	odes['s_0763_b'] = '0'
	# water [intracellular]
	odes['s_1434_b'] = '0'
	# ammonium [extracellular]
	odes['s_0431_b'] = '0'
	# biomass [extracellular]
	odes['s_0464_b'] = '0'
	# carbon dioxide [extracellular]
	odes['s_0472_b'] = '0'
	# D-glucose [extracellular]
	odes['s_0547_b'] = '0'
	# ethanol [extracellular]
	odes['s_0651_b'] = '0'
	# H+ [extracellular]
	odes['s_0766_b'] = '0'
	# oxygen [extracellular]
	odes['s_1162_b'] = '0'
	# phosphate [extracellular]
	odes['s_1209_b'] = '0'
	# succinate(2-) [extracellular]
	odes['s_1339_b'] = '0'
	# sulphate [extracellular]
	odes['s_1348_b'] = '0'

	module_dict['odes'] = odes

	return module_dict
