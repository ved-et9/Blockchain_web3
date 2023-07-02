from brownie import accounts,config,SimpleStorage

#pytest docmentation

def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_st=SimpleStorage.deploy({"from":account})
    starting_val = simple_st.retrieve()
    expected = 0

    # Assert

    assert starting_val == expected


def test_update_storage():
    # Arrange
    account=accounts[0]
    simple_st=SimpleStorage.deploy({"from":account})
    
    #Act
    expected=15
    simple_st.store(expected,{"from":account})

    #Assert
    assert expected == simple_st.retrieve()


