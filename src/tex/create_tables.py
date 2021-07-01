import latextable as ltx 
import numpy as np 

def save_eigen_table(data, name, dim, path):
    table = ltx.Texttable()
    table.set_cols_align(["c"]*(dim+1))
    rows = [['Iter'] + [str(i) for i in range(dim)]]
    for idx, values in enumerate(data):
        ar = [str(idx)] + list(np.round(values,2))
        rows.append(ar)
    table.add_rows(rows)
        
    
    with open(f"{path}{name}.tex", "a") as file:
        file.write(ltx.draw_latex(table, caption=f"{name}"))

def save_results_table(log_liks, train_errors, test_errors, names, path):
    table = ltx.Texttable()
    table.set_cols_align(["c"]*7)
    rows = [["Model", "ll (mean)", "Best ll", "mrmse (train)", "best rmse (train)", "mrmse (test)", "best rmse (test)"]]
    for idx in range(len(names)):
        model = names[idx]
        mean_ll, var_ll = np.round(np.mean(log_liks[idx]),2), np.round(np.var(log_liks[idx]),2)
        max_ll = np.round(np.max(log_liks[idx]),2)

        mean_train, var_train = np.round(np.mean(train_errors[idx]),2), np.round(np.var(train_errors[idx]),2)
        min_train = np.round(np.min(train_errors[idx]),2)

        mean_test, var_test = np.round(np.mean(test_errors[idx]),2), np.round(np.var(test_errors[idx]),2)
        min_test = np.round(np.min(test_errors[idx]),2)
        ar = [f"{model}", f"{mean_ll}({var_ll})", f"{max_ll}", f"{mean_train}({var_train})", f"{min_train}", f"{mean_test}({var_test})", f"{min_test}"]
        rows.append(ar)
    table.add_rows(rows)
        
    
    with open(f"{path}results.tex", "a") as file:
        file.write(ltx.draw_latex(table, caption=""))