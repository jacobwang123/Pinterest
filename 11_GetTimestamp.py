import os
import pandas as pd
import numpy as np
from datetime import datetime
import json
import requests
from multiprocessing import Pool

cwd = os.path.dirname(os.path.realpath(__file__))
token_index = 0
token = ['Afz32BRh8gNvTk-kLK_8XlvzbuNIFMMv_bRRVKtEDFR_pSBBMwAAAAA',
			'AddzTdtGlkXHm5lK7aVqx94TBKZHFMMwDoaS4etEDFSitkA3owAAAAA',
			'Aan1IEOgH47TgvEtGXODh57yc1bdFMMwHIAXq8xEDFTAF0AswgAAAAA',
			'Ab-gP7-2LCoqghJbF6UxmeYHthKoFMMwKe8kQdVEDFTca6A4pwAAAAA',
			'AfK9cdnzwzVBUS638Wj_alpY6ERSFMMwN-nuf4VEDFT5tMApvQAAAAA',
			'AUzaKCx95hV3-atoA5ckeFcXP4m3FMMwR8coDVZEDFUa8oAqmwAAAAA',
			'ATj09G6hf_bVieT1Hs-Ar1xfIixOFMMwXl5OOy9EDFVKKoA--QAAAAA',
			'AafJZm0-fDBn5SIdgjX18aDxv2VpFMMwaTlCtEJEDFVhFaA6ugAAAAA',
			'ATqraQmLhZ8qHoDyFO1I1G1Qh57CFMMwcZw7uPdEDFVyqUA61AAAAAA',
			'AaksVMGlb1cwB00fw1j-QALPzI-dFMMweiK9L6FEDFWEn0AoLgAAAAA',
			'AelGfWVWzfBiKUOHYbvcmXPIZiL7FMMwgYUPGA5EDFWUGUA4rwAAAAA',
			'AU2dWLD3V2U5qAvCr3a2JPTPKHCwFMMwi_garx5EDFWp5KA0lwAAAAA',
			'AdCZjVrf81WfBV312gRlDtsmO3b6FMMwk_0Emt5EDFW6zuApVQAAAAA',
			'AbxLUGnpaB9ctrYw1eOQz44WT0t_FMMwm0XW1wtEDFXJ2IBH-QAAAAA',
			'AWgNMKUQl5s6I2FxbhPhrVmkpx1mFMMwpFF0CVZEDFXc-iA7TQAAAAA',
			'AZB-ORxXpd8CiuGlUnP3_nfNHAq2FMMwrSZNz41EDFXvmcAoXgAAAAA',
			'AR9RJuSGRT1IBWOhUcKSHrwKShVAFMMws9scjwFEDFX9f8AtgwAAAAA',
			'AVhDP76IYvJUkyxpZXiAAbP8VGPEFMMwveRzrC5EDFYSdEAv5wAAAAA',
			'AYbUQ8UfHmxALLGWoM038ySrf5ztFMMwxQKjOfBEDFYhe6At3AAAAAA',
			'AfivjwA4ylwzMv0utM_5BR4SXfsCFMMwzdGT-QVEDFYz2yA27QAAAAA',
			'Ab3z582fFq-UJGi7J8cq3sCy-LC4FMIG2wMcBa1ECeVcNcAo5QAAAAA',
			'Ae4SFazCrOXR-Ty1HryemIQVoIuhFMIG7hnbsnVECeWEAMBEkgAAAAA',
			'AbQZu3nqOMPLl6Mk2CfDHc_T9wgwFMIJcAywAFtECerGFSA2bwAAAAA',
			'ASfGLgfv3UG5PwpYvh18f4vkNWddFMIJhcbZzaZECerzmYA-rgAAAAA',
			'AewqKq5OrQRrbnvkCkP_zEeKmS2BFMIJsLjjpkNECetNmyA20gAAAAA',
			'ARtz-qfApXDF5qfCCCE63L4JiUNtFMIJwZSFVHJECetxSqBC-wAAAAA',
			'AQ8T3cv1UzNA-XfPMCiFk5ABKbceFMIJzy0hhp9ECeuN_aAo9AAAAAA',
			'ATZXPDHvpiEoENesAVAJRqSddgDLFMIJ22xl27FECeunckAr2gAAAAA',
			'AUq7hJ8HDIkmGL1-KXsB8CPjSs9MFMIJ7jB5CrJECevLG4A7lQAAAAA',
			'AXIF54XnOQESyIDpVSSm5gHv-gpKFMIKAfUjYSJECev4dyA5HQAAAAA',
			'AVGC_FiwmYPcRxcV0Y-6PVrE1xONFMIKEn7nxC1ECewawkBGYgAAAAA',
			'AXUBO4at2phWIp9CAazDLOFlqAewFMIKN9-4-OhECexpIYBHMQAAAAA',
			'ARmiw5l8eOeLvSrl-pHgI-_a2Es0FMIF_SvzuXFECIPk9oA3RAAAAAA',
			'AaWqeeQvj50-OsqMKYhOTeIsgx48FMIGDSHpNwZEBzHKMYBEGQAAAAA',
			'Abds7VdBN0YG3NLBp4Un7BeFPsGWFMIGItMv2zRECePZ3GBCIgAAAAA',
			'AWrpgsLX5DfvXnzX6lehjkygu_3eFMIGMgwyoSdECIYkVgAtZAAAAAA',
			'AZqcp2oo2aLzkPRVemmsmy1cHihtFMIGRQ-f0VRECeQhR8A32AAAAAA',
			'AecAeRpggyDOKMjD5yi2DRiFehtMFMIGVGovPiNECeRBpwA1bwAAAAA',
			'AYidnj6716_1HcgttS0inYrTK8k8FMIGZmtFF6NECeRnTeBGzgAAAAA',
			'AZHSp0gpAUVXZryrhWFCCPxrS5CEFMIGjZA3p6lECeS5tcAx1wAAAAA',
			'AUxhDuK1u2-O-5FGC5z7LHd5cdX1FMIGtKJXeK1ECeULsSAxUAAAAAA',
			'AU2BMJxwTSq5c-aQ1AahI2wsGOuGFMIGx-2ZWZNECeU0BmA7LAAAAAA',
			'Ad5ijnA3hBRb7daeiHP22mDtb4HHFMN4_Yita_lEB_x18aAu5wAAAAA',
			'AQYCTmkcnT_hLexiwV7pYMJaXcczFMN5QEGYxBhEDO4inCA-WQAAAAA',
			'AaOzR1MG8tWr81SgVLXofqyEvb58FMN5q9HR-29EDO8EL4BF_QAAAAA',
			'AWAvX9EbhkAqcVaoTuGLrDaC1VYqFMN5-Ko22IVEDO-lb8BDKgAAAAA',
			'AVb3430LMe0Rfs4PaBtPReKPtJ-OFMN6iNy2vUtEDPAO36A_5gAAAAA',
			'AYsd4nyxPSdD8XSgQKfNuZFLRVKWFMN6s8vmXBJEDPEt70Ax0QAAAAA',
			'AVplmT5y2eFb9hLWqoEdCF-NtE1mFMN66I5FCllEDPGcd6A0qQAAAAA',
			'AbJ64ZlcPIHc0PzIiB-LjlNdSSilFMN7BAXBKixEDPHWCwBFNQAAAAA',
			'Af-6RjNfet5d3Vx9j24Hc9DJ4ba4FMN7G_cWLQVEDPIIbeBA4QAAAAA',
			'AWBsBHGuKSedkNtvM9jHOlrpUA1PFMN7PHvnEy5EDPJMpWBAhQAAAAA',
			'AXF6GUDPEjzN20jzxDQBBWP3INpGFMN7UxaqMWtEDPJ79yA6yAAAAAA',
			'AcqGgj_KPDcvffNEnt8LmoQLQpwTFMN7bv0pSzVEDPK2fUBCKQAAAAA',
			'AYLAjX9w_g6ifdCgbkPIoE2M34I3FMN7gpPe1LVEDPLfqUA4AgAAAAA',
			'ATEkKCj6IMbA8TBv2k4uViNLZiI7FMN7l9l2Z7VEDPML-2BHfQAAAAA',
			'ARZ-5IBj2dgSc3jdVtI3E8admpTkFMN7qas3ppdEDPMxiKAykQAAAAA',
			'AeHqUmGn-QdS_HUPvFgwzBcXEkAeFMN7uoRX6wtEDPNUhuA_YwAAAAA',
			'AYEKm0mMtIvnV30QnnjIeFCXrw5iFMN7zv1iZjZEDPN_o6A-iwAAAAA',
			'ATcmTR26iIsnDeT9srHrGuf25F8oFMONVvn8RbNEDRhDlCA2hQAAAAA',
			'AQkrfiAklRilskyDwTVTK-3TXcfFFMONYyY9vCVEDRhdYyBAuQAAAAA',
			'AZBd_S6vs5imGHIuP-wL6aOFni7jFMONa5mIb55EDRhuzuBGrQAAAAA',
			'Af4IxDrXfdqPvUb42iD9HkfGBW2tFN1P5NqVtI5EQx4L6MA23wAAAAA',
			'AXSMqm0SEdP9xxNREdDOrDkfqMM3FN1QA7vJxxNEQx5MrgAvggAAAAA',
			'ATjgfJYdcQsvehQn5JjOYeVI1HfIFN1QHWSinAFEQx6Ct8Ax7AAAAAA',
			'AZryfrb5e13bCn65guED2O7PID2zFN1QNXJb0yxEQx609GAucAAAAAA',
			'AQuX0W5TCx9tizyUCJGZQtfYS2AvFN1QRsYGLv5EQx7ZfGAx4gAAAAA',
			'AcE80FH0szbDLReWOw_UYATJmVRHFN1QVVlFxhhEQx73_GA70wAAAAA',
			'AZJtQTtMth_7o5t9I9OdNwB452lyFN1QaRi7_wREQx8heyBB0AAAAAA',
			'Aek0yfpQ5bWbKPF1V6V4Yoo70LqHFN1Qf3GEcGpEQx9QSmA6zgAAAAA',
			'Aafoxb5Of_hf8hF-ejSHEAYAaCHVFN1Qn_tmL3ZEQx-UleA5zQAAAAA',
			'Aaxx4PHmcNXI8vdpGYj8wm5IJV4hFN1QsWlUspVEQx-5GABC8gAAAAA',
			'AVOenzhs4EOtJ9UahCv6-eg-inrwFN1QyFiZvutEQx_pGsA85wAAAAA',
			'AT3jqNbknJti7GgWeOdw76FVIfedFN1Q6HchTTFEQyAsdyA0mgAAAAA',
			'AV2f3Kbrt_V5EDHKEUL5-TK9DaLvFN1Q_31gd01EQyBc1MArVQAAAAA',
			'AYdO7gNbZqQ0SoTVTtFXbmsZ6efVFN1REGCZU5pEQyCAESAvxwAAAAA',
			'AUg3qcL52rP6U0XxkE7_xOJkj-kyFN1RHoSvL6FEQyCd3aArdwAAAAA',
			'AYcXBxo3HP5eEBDqtyf3ljOmiUhSFN1RNEqS9gNEQyDLj4ArVwAAAAA',
			'AfkoHYjlxUxE3LGV2QQJpVDqYUP8FN1RQhaSYolEQyDoWCA3MwAAAAA',
			'Aai116Vt8bKPR3LsT0TFv3WM_R__FN1RYDDEtQpEQyEne4BG6QAAAAA',
			'Ac6woaLiFLCs43iFk81JIvnI7quMFN1RbsWGvYlEQyFF_KAv2QAAAAA',
			'AWg6a0o3NX4xWq07U7922sFDF9AWFN1Renk2-ddEQyFezwAxtgAAAAA',
			'AURGoDjOY2eqEQ2lOK9I40ScpOxnFN1RiV7KM-hEQyF99uAr9wAAAAA',
			'ASZL118YLwE5AyChgug3JRoOu9d5FN1RlEYCkIVEQyGUuwA2FgAAAAA',
			'ATLKPJZT8V3ZNdibZjebnliwV96WFN1Rn73WvHxEQyGtAIAwqQAAAAA',
			'AQRCbJp8C8s-UPJvWmYlVyLzNAjMFN1Rq1PioAJEQyHFGEA10gAAAAA',
			'ASnHjeEgA1PwBcEv3W2d8w19GvYPFN1Rt8ulUSpEQyHfR4A8ogAAAAA',
			'Ae1-JjjDTebuK75NNSmhHJS4g30BFN1RwmOaEZxEQyH1aeA3HgAAAAA',
			'AQgv65QICHMy0KNY0k_i_b9tSZUGFN1RziNcTL1EQyIOQQAxygAAAAA',
			'AZ4m1dlwBnPbkYXeUIVMKLvyEQZpFN11-xdNrfZEQ23rn8A9PgAAAAA']

def get_t(pinID):
	global token_index
	while True:
		url = 'https://api.pinterest.com/v1/pins/' + str(pinID) + '/?access_token=' +\
			  token[token_index] + '&fields=created_at'
		try:
			response = requests.get(url).text
		except:
			print('Buffer error...')
			return None
		if 'You have exceeded your rate limit' not in response:
			break
		else:
			if token_index == len(token) - 1:
				token_index = 0
			else:
				token_index += 1
			print(token_index, pinID)
	try:
		tstp = json.loads(response)['data']['created_at']
		tstp = datetime.strptime(tstp, '%Y-%m-%dT%H:%M:%S')
		return tstp
	except:
		return None

def downloader(thread):
	if thread == 3:
		temp = df.iloc[thread * trunk:, :]
	else:
		temp = df.iloc[thread * trunk : (thread+1) * trunk, :]

	for index, value in temp.iterrows():
		value['pin_timestamp'] = get_t(value['pinID'])
		with open(os.path.join(cwd, 'new_board_pins_'+str(thread)+'.txt'), 'a') as f:
			for i in range(len(cols)):
				if i == len(cols)-1:
					f.write(str(value[cols[i]]) + '\n')
				else:
					f.write(str(value[cols[i]]) + '\t')

if __name__ == '__main__':
	df = pd.read_csv(os.path.join(cwd, 'board_pins_0.txt'), sep='\t', header=0, names=['boardID','pinID','URL','dcrpt'], error_bad_lines=False)
	df['pin_timestamp'] = np.nan
	cols = df.columns.values
	trunk = int(df.shape[0] / 4)

	p = Pool(4)
	p.map(downloader, range(4))	

