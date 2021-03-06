


def stratData(strategy, token, vToken, vsp):
    decimals = token.decimals()
    print('\n----STRATEGY----')
    stratBal = token.balanceOf(strategy)
    vesperSharesU = vToken.balanceOf(strategy)
    vspBal = vsp.balanceOf(strategy)
    print("Token bal:", stratBal/(10 ** decimals))
    print("vsp bal:", vspBal/1e18)
    print("vesper shares vToken:", vesperSharesU / 1e18)
    print('Estimated total assets:', strategy.estimatedTotalAssets()/  (10 ** decimals))  

def vaultData(vault, token):
    print('\n----VAULT----')
    decimals = token.decimals()
    vaultBal = token.balanceOf(vault)
    balance = vault.totalAssets()/  (10 ** decimals)
    print("loose vault bal:", vaultBal/(10 ** decimals))
    debt = vault.totalDebt()/  (10 ** decimals)
    print(f"Total Debt: {debt:.5f}")
    print(f"Total Assets: {balance:.5f}")