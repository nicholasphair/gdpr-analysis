Timeout in resolving values
Timeout in running neo4j query
Running Main.py on readme-detonator

###########################
### Preprocessing stage ###
###########################
### Starting preproccessing!
Registering plugin to plugin database... Plugin registration done
╔[1] Preprocessing step "Add AST_JS label to JS nodes" (__label_js_nodes) begin.
╚[1] Preprocessing step "Add AST_JS label to JS nodes" (__label_js_nodes) finished successfully in 0:00:00.408527.

0 edges imported to Neo4j
Preprocessing step 0 done!
╔[2] Preprocessing step "Create DB indices" (__create_indices) begin.
Creating indices for commonly used features... done.
╚[2] Preprocessing step "Create DB indices" (__create_indices) finished successfully in 0:00:00.830558.

0 edges imported to Neo4j
Preprocessing step 1 done!
Analzying PHP class hierarchy...
Start filling class hierarchy information
Finished filling class hierarchy information
Start filling function information
Finished filling function information
0 edges imported to Neo4j
Preprocessing step 2 done!
╔[3] Preprocessing step "connect data flows for class properties" (__handle_class_properties) begin.
Added 0 PHP_REACHES edges.
╚[3] Preprocessing step "connect data flows for class properties" (__handle_class_properties) finished successfully in 0:00:00.189564.

╔[4] Preprocessing step "Connect AST_PARAM edges" (__connect_ASTPARAM_to_var) begin.
Added 0 REACHES edges for AST_PARAM to variables
╚[4] Preprocessing step "Connect AST_PARAM edges" (__connect_ASTPARAM_to_var) finished successfully in 0:00:00.468617.

╔[5] Preprocessing step "Create PHP_REACHES edges" (__php_reach_edges) begin.
Added 28 :PHP_REACHES for original :REACHES edges.
╚[5] Preprocessing step "Create PHP_REACHES edges" (__php_reach_edges) finished successfully in 0:00:00.622523.

╔[6] Preprocessing step "Create parent-to-self edges" (__parent_self_edges) begin.
Added 0 CALLS edges.
╚[6] Preprocessing step "Create parent-to-self edges" (__parent_self_edges) finished successfully in 0:00:00.666216.

╔[7] Preprocessing step "Connect data flows for class constants" (__class_constant_hierarchy) begin.
╚[7] Preprocessing step "Connect data flows for class constants" (__class_constant_hierarchy) finished successfully in 0:00:00.129670.

╔[8] Preprocessing step "Create AST assign hierarchy PHP_REACHES edges" (__ast_assign_function_edges) begin.
Added 16 PHP_REACHES edges.
╚[8] Preprocessing step "Create AST assign hierarchy PHP_REACHES edges" (__ast_assign_function_edges) finished successfully in 0:00:00.513627.

╔[9] Preprocessing step "Build hierarchical data flow edges for php and js" (__build_php_js_hierarchical_edges) begin.
Building hierarchical edges for PHP...
Number of rows: 423
Added 379 PHP_REACHES edges. 
Building hierarchical edges for JS...
Number of rows: 423
Added 0 JS_REACHES edges. 
╚[9] Preprocessing step "Build hierarchical data flow edges for php and js" (__build_php_js_hierarchical_edges) finished successfully in 0:00:00.924936.

╔[10] Preprocessing step "Building HTML ASTs" (__build_html_ast) begin.
HTML code from file '/home/ec2-user/GDPR-CCPA-violation-checker/navex_docker/tempApp/readme-detonator/index.php' cannot be parsed correct.
╚[10] Preprocessing step "Building HTML ASTs" (__build_html_ast) finished successfully in 0:00:00.148000.

423 PHP_REACHES edges created
423 edges imported to Neo4j
Preprocessing step 3 done!
╔[11] Preprocessing step "Remove wrong/excessive hierarchical edges" (__remove_wrong_hierarchical_edges) begin.
Deleted 142 incorrect PHP_REACHES edges. Deleted 0 incorrect JS_REACHES edges.
╚[11] Preprocessing step "Remove wrong/excessive hierarchical edges" (__remove_wrong_hierarchical_edges) finished successfully in 0:00:01.051580.

0 edges imported to Neo4j
Preprocessing step 4 done!
╔[12] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[12] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.716037.

╔[13] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[13] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.133786.

╔[14] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[14] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.195161.

╔[15] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[15] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.035574.

╔[16] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[16] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.005470.

╔[17] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[17] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.005882.

╔[18] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[18] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.034134.

╔[19] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[19] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.005763.

╔[20] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[20] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.006306.

╔[21] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[21] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.033686.

╔[22] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[22] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.005969.

╔[23] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[23] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.009826.

╔[24] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[24] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.054140.

╔[25] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[25] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.012269.

╔[26] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[26] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.006427.

╔[27] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[27] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.057962.

╔[28] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[28] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.008552.

╔[29] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[29] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.009391.

╔[30] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[30] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.046172.

╔[31] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[31] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.007086.

╔[32] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[32] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.009150.

╔[33] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[33] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.039046.

╔[34] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[34] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.005154.

╔[35] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[35] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.005606.

╔[36] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[36] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.050102.

╔[37] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[37] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.005290.

╔[38] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[38] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.008332.

╔[39] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[39] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.038463.

╔[40] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[40] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.005903.

╔[41] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[41] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.010907.

╔[42] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[42] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.179043.

╔[43] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[43] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.030715.

╔[44] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[44] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.045860.

╔[45] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[45] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.041476.

╔[46] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[46] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.008425.

╔[47] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[47] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.007479.

╔[48] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[48] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.043695.

╔[49] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[49] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.007857.

╔[50] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[50] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.005923.

╔[51] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[51] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.046906.

╔[52] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[52] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.009247.

╔[53] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[53] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.006046.

╔[54] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[54] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.038815.

╔[55] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[55] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.005342.

╔[56] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[56] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.007462.

╔[57] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[57] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.044264.

╔[58] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[58] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.005435.

╔[59] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[59] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.005811.

╔[60] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[60] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.035235.

╔[61] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[61] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.005677.

╔[62] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[62] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.005687.

╔[63] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[63] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.029329.

╔[64] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[64] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.004889.

╔[65] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[65] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.008403.

╔[66] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[66] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.035009.

╔[67] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[67] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.005148.

╔[68] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[68] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.005547.

╔[69] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[69] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.038357.

╔[70] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[70] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.005291.

╔[71] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[71] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.005753.

╔[72] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[72] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.031169.

╔[73] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[73] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.004172.

╔[74] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[74] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004923.

╔[75] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[75] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.028051.

╔[76] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[76] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.004044.

╔[77] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[77] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004617.

╔[78] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[78] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.026251.

╔[79] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[79] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.004443.

╔[80] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[80] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.005331.

╔[81] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[81] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.027760.

╔[82] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[82] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.004730.

╔[83] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[83] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004569.

╔[84] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[84] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.037214.

╔[85] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[85] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.004935.

╔[86] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[86] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004279.

╔[87] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[87] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.032315.

╔[88] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[88] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.004676.

╔[89] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[89] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.005746.

╔[90] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[90] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.033997.

╔[91] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[91] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.006253.

╔[92] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[92] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.005056.

╔[93] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[93] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.037857.

╔[94] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[94] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.004394.

╔[95] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[95] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003669.

╔[96] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[96] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.027434.

╔[97] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[97] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.004878.

╔[98] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[98] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004530.

╔[99] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[99] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.048048.

╔[100] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[100] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.004301.

╔[101] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[101] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004034.

╔[102] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[102] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.025386.

╔[103] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[103] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003814.

╔[104] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[104] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003737.

╔[105] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[105] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.035182.

╔[106] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[106] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.004191.

╔[107] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[107] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004753.

╔[108] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[108] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.028225.

╔[109] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[109] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.004186.

╔[110] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[110] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003320.

╔[111] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[111] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.038130.

╔[112] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[112] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.004438.

╔[113] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[113] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.007422.

╔[114] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[114] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.028732.

╔[115] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[115] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.008553.

╔[116] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[116] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004577.

╔[117] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[117] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.027813.

╔[118] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[118] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.005837.

╔[119] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[119] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004292.

╔[120] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[120] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.026726.

╔[121] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[121] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.004202.

╔[122] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[122] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003819.

╔[123] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[123] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.027074.

╔[124] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[124] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.004417.

╔[125] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[125] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004066.

╔[126] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[126] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.026767.

╔[127] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[127] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.005106.

╔[128] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[128] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004125.

╔[129] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[129] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.023568.

╔[130] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[130] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.006191.

╔[131] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[131] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004459.

╔[132] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[132] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.024663.

╔[133] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[133] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003717.

╔[134] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[134] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003844.

╔[135] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[135] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.020264.

╔[136] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[136] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003690.

╔[137] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[137] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003818.

╔[138] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[138] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.018103.

╔[139] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[139] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003744.

╔[140] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[140] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004117.

╔[141] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[141] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.020001.

╔[142] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[142] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003520.

╔[143] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[143] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003996.

╔[144] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[144] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.018473.

╔[145] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[145] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003264.

╔[146] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[146] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003368.

╔[147] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[147] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.025732.

╔[148] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[148] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003847.

╔[149] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[149] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004184.

╔[150] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[150] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.020343.

╔[151] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[151] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003281.

╔[152] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[152] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003750.

╔[153] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[153] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.020974.

╔[154] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[154] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003882.

╔[155] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[155] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004219.

╔[156] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[156] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.037267.

╔[157] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[157] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003747.

╔[158] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[158] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004146.

╔[159] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[159] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.024181.

╔[160] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[160] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.004369.

╔[161] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[161] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003728.

╔[162] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[162] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.025638.

╔[163] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[163] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003377.

╔[164] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[164] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004775.

╔[165] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[165] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.026927.

╔[166] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[166] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003522.

╔[167] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[167] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.005100.

╔[168] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[168] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.021613.

╔[169] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[169] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003293.

╔[170] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[170] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.006162.

╔[171] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[171] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.020206.

╔[172] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[172] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003467.

╔[173] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[173] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003859.

╔[174] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[174] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.027185.

╔[175] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[175] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.007364.

╔[176] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[176] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003953.

╔[177] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[177] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.021244.

╔[178] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[178] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003392.

╔[179] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[179] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003920.

╔[180] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[180] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.019719.

╔[181] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[181] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003885.

╔[182] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[182] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.007080.

╔[183] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[183] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.019046.

╔[184] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[184] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.006060.

╔[185] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[185] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003977.

╔[186] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[186] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.031181.

╔[187] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[187] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003573.

╔[188] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[188] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003316.

╔[189] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[189] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.027273.

╔[190] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[190] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002863.

╔[191] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[191] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003636.

╔[192] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[192] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.017312.

╔[193] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[193] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002948.

╔[194] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[194] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003459.

╔[195] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[195] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.019012.

╔[196] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[196] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003352.

╔[197] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[197] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004483.

╔[198] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[198] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.026120.

╔[199] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[199] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.004648.

╔[200] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[200] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003723.

╔[201] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[201] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.017724.

╔[202] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[202] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002504.

╔[203] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[203] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002846.

╔[204] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[204] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.017249.

╔[205] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[205] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003603.

╔[206] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[206] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.006686.

╔[207] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[207] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.023750.

╔[208] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[208] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003844.

╔[209] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[209] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003848.

╔[210] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[210] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.025390.

╔[211] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[211] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003532.

╔[212] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[212] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004040.

╔[213] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[213] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.019222.

╔[214] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[214] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003734.

╔[215] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[215] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003858.

╔[216] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[216] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.018648.

╔[217] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[217] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002998.

╔[218] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[218] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003198.

╔[219] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[219] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.021187.

╔[220] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[220] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003090.

╔[221] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[221] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003528.

╔[222] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[222] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.019986.

╔[223] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[223] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002670.

╔[224] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[224] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004942.

╔[225] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[225] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.016284.

╔[226] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[226] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002589.

╔[227] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[227] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003899.

╔[228] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[228] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.019798.

╔[229] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[229] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003073.

╔[230] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[230] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002607.

╔[231] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[231] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.015788.

╔[232] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[232] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002569.

╔[233] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[233] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003012.

╔[234] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[234] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.017060.

╔[235] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[235] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003020.

╔[236] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[236] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.011583.

╔[237] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[237] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.019773.

╔[238] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[238] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003230.

╔[239] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[239] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003641.

╔[240] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[240] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.018787.

╔[241] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[241] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.005039.

╔[242] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[242] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003739.

╔[243] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[243] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.027662.

╔[244] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[244] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003422.

╔[245] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[245] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004443.

╔[246] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[246] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.016084.

╔[247] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[247] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003032.

╔[248] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[248] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003302.

╔[249] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[249] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.022097.

╔[250] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[250] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003110.

╔[251] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[251] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004519.

╔[252] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[252] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.020358.

╔[253] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[253] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002959.

╔[254] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[254] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003245.

╔[255] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[255] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.015928.

╔[256] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[256] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002811.

╔[257] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[257] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.013409.

╔[258] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[258] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.017549.

╔[259] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[259] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002800.

╔[260] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[260] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003207.

╔[261] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[261] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.015535.

╔[262] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[262] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002678.

╔[263] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[263] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002862.

╔[264] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[264] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.014232.

╔[265] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[265] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002850.

╔[266] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[266] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004736.

╔[267] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[267] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.017218.

╔[268] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[268] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002925.

╔[269] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[269] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003464.

╔[270] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[270] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.016677.

╔[271] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[271] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002978.

╔[272] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[272] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003370.

╔[273] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[273] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.020927.

╔[274] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[274] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002985.

╔[275] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[275] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003502.

╔[276] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[276] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.017450.

╔[277] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[277] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003234.

╔[278] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[278] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003097.

╔[279] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[279] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.017849.

╔[280] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[280] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002997.

╔[281] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[281] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003336.

╔[282] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[282] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.017312.

╔[283] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[283] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002397.

╔[284] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[284] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002832.

╔[285] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[285] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.025282.

╔[286] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[286] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003044.

╔[287] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[287] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002953.

╔[288] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[288] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013673.

╔[289] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[289] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002293.

╔[290] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[290] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003035.

╔[291] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[291] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.017581.

╔[292] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[292] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003354.

╔[293] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[293] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003380.

╔[294] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[294] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.018222.

╔[295] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[295] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003028.

╔[296] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[296] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003274.

╔[297] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[297] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.016205.

╔[298] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[298] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002897.

╔[299] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[299] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003151.

╔[300] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[300] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.033027.

╔[301] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[301] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003553.

╔[302] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[302] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003537.

╔[303] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[303] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.016725.

╔[304] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[304] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002977.

╔[305] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[305] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003253.

╔[306] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[306] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.015761.

╔[307] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[307] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002844.

╔[308] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[308] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.007428.

╔[309] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[309] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.017061.

╔[310] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[310] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002626.

╔[311] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[311] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002644.

╔[312] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[312] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013963.

╔[313] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[313] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002388.

╔[314] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[314] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002655.

╔[315] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[315] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.014860.

╔[316] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[316] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002756.

╔[317] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[317] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002982.

╔[318] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[318] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.014935.

╔[319] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[319] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002660.

╔[320] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[320] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002863.

╔[321] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[321] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.014293.

╔[322] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[322] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002530.

╔[323] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[323] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002872.

╔[324] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[324] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.014979.

╔[325] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[325] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003011.

╔[326] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[326] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002974.

╔[327] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[327] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.014485.

╔[328] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[328] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002615.

╔[329] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[329] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002976.

╔[330] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[330] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.014854.

╔[331] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[331] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002661.

╔[332] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[332] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002844.

╔[333] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[333] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.015726.

╔[334] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[334] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003039.

╔[335] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[335] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003246.

╔[336] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[336] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.015990.

╔[337] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[337] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002945.

╔[338] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[338] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003035.

╔[339] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[339] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.015747.

╔[340] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[340] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002935.

╔[341] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[341] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003194.

╔[342] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[342] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.016108.

╔[343] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[343] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002737.

╔[344] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[344] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002949.

╔[345] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[345] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.016166.

╔[346] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[346] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002895.

╔[347] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[347] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003278.

╔[348] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[348] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.017132.

╔[349] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[349] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002936.

╔[350] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[350] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003077.

╔[351] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[351] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.016165.

╔[352] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[352] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002701.

╔[353] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[353] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002915.

╔[354] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[354] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.015318.

╔[355] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[355] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002610.

╔[356] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[356] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002726.

╔[357] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[357] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013971.

╔[358] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[358] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002078.

╔[359] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[359] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002393.

╔[360] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[360] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.012560.

╔[361] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[361] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002176.

╔[362] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[362] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002414.

╔[363] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[363] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.012553.

╔[364] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[364] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002416.

╔[365] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[365] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002572.

╔[366] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[366] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.012274.

╔[367] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[367] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002404.

╔[368] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[368] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002320.

╔[369] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[369] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.012396.

╔[370] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[370] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002173.

╔[371] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[371] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002312.

╔[372] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[372] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.016217.

╔[373] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[373] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002724.

╔[374] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[374] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002739.

╔[375] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[375] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013907.

╔[376] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[376] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002379.

╔[377] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[377] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002552.

╔[378] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[378] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.014063.

╔[379] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[379] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002285.

╔[380] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[380] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002403.

╔[381] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[381] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.011595.

╔[382] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[382] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001972.

╔[383] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[383] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002171.

╔[384] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[384] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.011767.

╔[385] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[385] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002071.

╔[386] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[386] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002388.

╔[387] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[387] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013431.

╔[388] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[388] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002361.

╔[389] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[389] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003823.

╔[390] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[390] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013211.

╔[391] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[391] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002222.

╔[392] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[392] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002754.

╔[393] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[393] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.014681.

╔[394] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[394] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002514.

╔[395] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[395] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002699.

╔[396] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[396] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013748.

╔[397] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[397] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002633.

╔[398] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[398] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002639.

╔[399] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[399] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.014126.

╔[400] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[400] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002532.

╔[401] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[401] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002942.

╔[402] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[402] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.014199.

╔[403] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[403] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002388.

╔[404] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[404] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002838.

╔[405] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[405] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013125.

╔[406] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[406] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002147.

╔[407] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[407] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002454.

╔[408] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[408] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.014388.

╔[409] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[409] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002838.

╔[410] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[410] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003068.

╔[411] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[411] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.015023.

╔[412] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[412] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002545.

╔[413] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[413] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002748.

╔[414] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[414] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.015308.

╔[415] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[415] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002868.

╔[416] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[416] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002977.

╔[417] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[417] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.014915.

╔[418] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[418] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002425.

╔[419] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[419] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002765.

╔[420] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[420] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.014019.

╔[421] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[421] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002710.

╔[422] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[422] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002936.

╔[423] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[423] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.015053.

╔[424] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[424] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002538.

╔[425] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[425] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003266.

╔[426] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[426] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.014742.

╔[427] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[427] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002582.

╔[428] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[428] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003224.

╔[429] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[429] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.016495.

╔[430] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[430] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002878.

╔[431] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[431] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002952.

╔[432] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[432] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.015120.

╔[433] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[433] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003483.

╔[434] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[434] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002833.

╔[435] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[435] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.018003.

╔[436] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[436] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002722.

╔[437] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[437] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002705.

╔[438] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[438] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013989.

╔[439] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[439] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002371.

╔[440] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[440] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002542.

╔[441] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[441] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013827.

╔[442] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[442] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002427.

╔[443] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[443] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002596.

╔[444] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[444] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013405.

╔[445] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[445] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002241.

╔[446] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[446] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002178.

╔[447] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[447] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.012484.

╔[448] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[448] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002080.

╔[449] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[449] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002552.

╔[450] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[450] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.021816.

╔[451] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[451] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002721.

╔[452] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[452] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002973.

╔[453] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[453] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.015617.

╔[454] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[454] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002537.

╔[455] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[455] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002734.

╔[456] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[456] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013712.

╔[457] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[457] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002317.

╔[458] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[458] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.004153.

╔[459] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[459] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013184.

╔[460] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[460] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002170.

╔[461] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[461] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002169.

╔[462] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[462] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.012948.

╔[463] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[463] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002022.

╔[464] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[464] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002408.

╔[465] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[465] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.012171.

╔[466] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[466] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002189.

╔[467] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[467] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002470.

╔[468] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[468] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013276.

╔[469] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[469] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.003884.

╔[470] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[470] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003482.

╔[471] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[471] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.020405.

╔[472] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[472] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002700.

╔[473] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[473] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003745.

╔[474] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[474] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.017254.

╔[475] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[475] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002355.

╔[476] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[476] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002289.

╔[477] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[477] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.055046.

╔[478] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[478] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002693.

╔[479] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[479] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002893.

╔[480] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[480] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.014105.

╔[481] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[481] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002577.

╔[482] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[482] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002717.

╔[483] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[483] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013878.

╔[484] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[484] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002461.

╔[485] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[485] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003044.

╔[486] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[486] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013311.

╔[487] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[487] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002362.

╔[488] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[488] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002370.

╔[489] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[489] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.011437.

╔[490] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[490] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001953.

╔[491] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[491] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002151.

╔[492] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[492] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.011943.

╔[493] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[493] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001885.

╔[494] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[494] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002188.

╔[495] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[495] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.010971.

╔[496] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[496] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001987.

╔[497] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[497] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002071.

╔[498] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[498] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.010514.

╔[499] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[499] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001926.

╔[500] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[500] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.005981.

╔[501] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[501] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013145.

╔[502] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[502] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001956.

╔[503] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[503] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.001780.

╔[504] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[504] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.012307.

╔[505] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[505] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001911.

╔[506] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[506] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002077.

╔[507] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[507] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.010909.

╔[508] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[508] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001747.

╔[509] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[509] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002070.

╔[510] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[510] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.010351.

╔[511] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[511] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001641.

╔[512] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[512] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.001952.

╔[513] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[513] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.010671.

╔[514] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[514] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001849.

╔[515] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[515] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002051.

╔[516] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[516] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.010576.

╔[517] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[517] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001889.

╔[518] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[518] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.001886.

╔[519] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[519] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.011160.

╔[520] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[520] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002611.

╔[521] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[521] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.001989.

╔[522] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[522] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.014403.

╔[523] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[523] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002001.

╔[524] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[524] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002299.

╔[525] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[525] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.011739.

╔[526] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[526] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001906.

╔[527] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[527] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002206.

╔[528] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[528] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013113.

╔[529] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[529] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002102.

╔[530] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[530] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002211.

╔[531] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[531] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.011421.

╔[532] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[532] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001798.

╔[533] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[533] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002130.

╔[534] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[534] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.011345.

╔[535] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[535] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001863.

╔[536] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[536] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.001942.

╔[537] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[537] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.011994.

╔[538] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[538] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001892.

╔[539] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[539] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002223.

╔[540] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[540] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.012630.

╔[541] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[541] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002315.

╔[542] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[542] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002297.

╔[543] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[543] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.012367.

╔[544] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[544] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002368.

╔[545] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[545] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002225.

╔[546] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[546] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.011347.

╔[547] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[547] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001979.

╔[548] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[548] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002224.

╔[549] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[549] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.012361.

╔[550] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[550] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.004014.

╔[551] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[551] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002507.

╔[552] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[552] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.020639.

╔[553] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[553] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002111.

╔[554] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[554] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002442.

╔[555] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[555] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013875.

╔[556] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[556] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002252.

╔[557] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[557] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002458.

╔[558] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[558] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.012774.

╔[559] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[559] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001890.

╔[560] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[560] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002134.

╔[561] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[561] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.011938.

╔[562] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[562] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002009.

╔[563] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[563] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.001750.

╔[564] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[564] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.010632.

╔[565] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[565] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001885.

╔[566] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[566] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002461.

╔[567] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[567] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.010656.

╔[568] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[568] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001585.

╔[569] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[569] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002186.

╔[570] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[570] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.012577.

╔[571] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[571] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002029.

╔[572] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[572] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002263.

╔[573] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[573] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.011522.

╔[574] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[574] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001793.

╔[575] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[575] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003257.

╔[576] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[576] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.011241.

╔[577] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[577] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001944.

╔[578] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[578] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002140.

╔[579] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[579] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.011371.

╔[580] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[580] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001856.

╔[581] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[581] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002112.

╔[582] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[582] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.011440.

╔[583] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[583] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001924.

╔[584] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[584] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002008.

╔[585] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[585] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.012524.

╔[586] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[586] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002120.

╔[587] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[587] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002225.

╔[588] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[588] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.012214.

╔[589] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[589] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.002011.

╔[590] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[590] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002232.

╔[591] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[591] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.011541.

╔[592] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[592] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001859.

╔[593] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[593] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002164.

╔[594] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[594] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.011279.

╔[595] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[595] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001936.

╔[596] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[596] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.001885.

╔[597] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[597] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.013444.

╔[598] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[598] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001677.

╔[599] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[599] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002173.

╔[600] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[600] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.011399.

╔[601] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[601] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001748.

╔[602] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[602] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002132.

╔[603] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[603] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.012351.

╔[604] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[604] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001955.

╔[605] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[605] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002332.

╔[606] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[606] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.012192.

╔[607] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[607] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001861.

╔[608] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[608] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.002108.

╔[609] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) begin.
Added 0 CALLS edges.
╚[609] Preprocessing step "Handle class hierarchy and make CALLS edges and certain data flows" (__handle_class_hierarchy) finished successfully in 0:00:00.012188.

╔[610] Preprocessing step "Create function call edges" (__function_call_edges) begin.
╚[610] Preprocessing step "Create function call edges" (__function_call_edges) finished successfully in 0:00:00.001793.

╔[611] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) begin.
╚[611] Preprocessing step "Create PHP_REACHES edges between function returns and callers" (__ast_call_return_edges) finished successfully in 0:00:00.003382.

╔[612] Preprocessing step "Create HTML_TO_PHP_REACHES edges between form inputs and PHP request vars" (__html_to_php_reaches) begin.
Added 0 HTML_TO_PHP_REACHES edges. Successfully connect 0 out of 0 inputs to PHP. 
╚[612] Preprocessing step "Create HTML_TO_PHP_REACHES edges between form inputs and PHP request vars" (__html_to_php_reaches) finished successfully in 0:00:00.058696.

0 edges imported to Neo4j
Preprocessing step 5 done!
╔[613] Preprocessing step "Overtaint Function Calls" (__overtaintFunctionCalls) begin.
Deleted 0 PHP_REACHES edges that overtaint function call data flows.
╚[613] Preprocessing step "Overtaint Function Calls" (__overtaintFunctionCalls) finished successfully in 0:00:00.130140.

0 edges imported to Neo4j
Preprocessing step 6 done!
╔[614] Preprocessing step "Create SQL AST" (__add_sql_ast) begin.
No SQL nodes to process.
╚[614] Preprocessing step "Create SQL AST" (__add_sql_ast) finished successfully in 0:00:00.107290.

╔[615] Preprocessing step "Build HTML AST for HTML embedded in PHP code (HTML to PHP traversal)" (__build_html_ast_in_php) begin.
HTML code '$'ERROR: Could not able to execute SELECT * FROM wp_users. mysqli_error($connection)'' cannot be parsed correct.
HTML code '$'<br><a href=\'admin.php?page=readme_detonator-settings\'>'' cannot be parsed correct.
HTML code '$'</a>.</p>'' cannot be parsed correct.
HTML code '$'<h1>Readme Detonator</h1><h5>'' cannot be parsed correct.
HTML code '$' <a href="http://wphaker.pl" target="_blank">WPhaker.pl</a></h1><h5>'' cannot be parsed correct.
HTML code '$'<hr></h4>'' cannot be parsed correct.
HTML code '$'<div id=\'supportcards\' class=\'cardright\'>'' cannot be parsed correct.
HTML code '$'<div class=\'card\' style=\'float:right\'>
			<div id=\'contactmethod\'>
				<a href=\'mailto:kontakt@wphaker.pl?Subject=Readme%20Detonator%20Support\' target=\'_top\'><span id=\'status\' class=\'ofinfo\'>'' cannot be parsed correct.
HTML code '$'</span></a>
				<br><br><a href=\'https://wphaker.pl/kontakt/\' target=\'_blank\'>
				<span id=\'status\' class=\'ofinfo\'>'' cannot be parsed correct.
HTML code '$'</span>
				</a>
			</div>
			<div id=\'contacttext\'>
				<h3 class=\'title\'>'' cannot be parsed correct.
HTML code '$'</h3><p>'' cannot be parsed correct.
HTML code '$'</p>
			</div>
		</div>'' cannot be parsed correct.
HTML code '$'<div class=\'card\' style=\'float:right\' class=\'cardright\'>
			<div id=\'contactmethod\'>
				<a href=\'https://www.paypal.me/prezydent/14,99usd\' target=\'_blank\'><span id=\'status\' class=\'ofinfo\'>'' cannot be parsed correct.
HTML code '$'</span>
				</a>
			</div>
			<div id=\'contacttext\'>
				<h3 class=\'title\'>'' cannot be parsed correct.
HTML code '$'</h3><p>'' cannot be parsed correct.
HTML code '$'</p>
			</div>
		</div>'' cannot be parsed correct.
HTML code '$'<div class=\'card\' style=\'float:right\' class=\'cardright\'>
			<div id=\'contacttext\' style=\'width:100%\'>
				<h3 class=\'title\'><form action=\'https://www.paypal.com/cgi-bin/webscr\' method=\'post\' target=\'_top\'>
<input type=\'hidden\' name=\'cmd\' value=\'_s-xclick\'>
<input type=\'hidden\' name=\'hosted_button_id\' value=\'USLXUBE6HLKDU\'>
<input type=\'image\' src=\'https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif\' border=\'0\' name=\'submit\' alt=\'PayPal - The safer, easier way to pay online!\'>
<img alt=\'\' border=\'0\' src=\'https://www.paypalobjects.com/en_US/i/scr/pixel.gif\' width=\'1\' height=\'1\'>
</form></h3>
				<p>'' cannot be parsed correct.
HTML code '$'</p>
			</div>
		</div>'' cannot be parsed correct.
HTML code '$'</div>'' cannot be parsed correct.
HTML code '$'<div id=\'normalcards\'>'' cannot be parsed correct.
HTML code '$'<div class=\'card statusowe\'>
			<span id=\'status\' class=\'offile\'>'' cannot be parsed correct.
HTML code '$'</span>
		    <h3 class=\'title\'>Readme.html</h3>
		</div>'' cannot be parsed correct.
HTML code '$'<div class=\'card statusowe\'>
			<span id=\'status\' class=\'offile\'>'' cannot be parsed correct.
HTML code '$'</span>
		    <h3 class=\'title\'>license.txt</h3>
		</div>'' cannot be parsed correct.
HTML code '$'<div class=\'card statusowe\'>
				<span id=\'statuscdn\' class=\'ofinfo\'>Do not exist</span>
			    <h3 class=\'title\' id=\'tytul\'></h3>
			    <p id=\'opis\'></p>
			</div>'' cannot be parsed correct.
HTML code '$'</div>'' cannot be parsed correct.
HTML code '$'<div id=\'supportcards\' class=\'cardright\'>'' cannot be parsed correct.
HTML code '$'<div class=\'card\' style=\'float:right\'>
			<div id=\'contactmethod\'>
				<a href=\'mailto:kontakt@wphaker.pl?Subject=Readme%20Detonator%20Support\' target=\'_top\'><span id=\'status\' class=\'ofinfo\'>'' cannot be parsed correct.
HTML code '$'</span></a>
				<br><br><a href=\'https://wphaker.pl/kontakt/\' target=\'_blank\'>
				<span id=\'status\' class=\'ofinfo\'>'' cannot be parsed correct.
HTML code '$'</span>
				</a>
			</div>
			<div id=\'contacttext\'>
				<h3 class=\'title\'>'' cannot be parsed correct.
HTML code '$'</h3><p>'' cannot be parsed correct.
HTML code '$'</p>
			</div>
		</div>'' cannot be parsed correct.
HTML code '$'<div class=\'card\' style=\'float:right\' class=\'cardright\'>
			<div id=\'contactmethod\'>
				<a href=\'https://www.paypal.me/prezydent/14,99usd\' target=\'_blank\'><span id=\'status\' class=\'ofinfo\'>'' cannot be parsed correct.
HTML code '$'</span>
				</a>
			</div>
			<div id=\'contacttext\'>
				<h3 class=\'title\'>'' cannot be parsed correct.
HTML code '$'</h3><p>'' cannot be parsed correct.
HTML code '$'</p>
			</div>
		</div>'' cannot be parsed correct.
HTML code '$'<div class=\'card\' style=\'float:right\' class=\'cardright\'>
			<div id=\'contacttext\' style=\'width:100%\'>
				<h3 class=\'title\'><form action=\'https://www.paypal.com/cgi-bin/webscr\' method=\'post\' target=\'_top\'>
<input type=\'hidden\' name=\'cmd\' value=\'_s-xclick\'>
<input type=\'hidden\' name=\'hosted_button_id\' value=\'USLXUBE6HLKDU\'>
<input type=\'image\' src=\'https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif\' border=\'0\' name=\'submit\' alt=\'PayPal - The safer, easier way to pay online!\'>
<img alt=\'\' border=\'0\' src=\'https://www.paypalobjects.com/en_US/i/scr/pixel.gif\' width=\'1\' height=\'1\'>
</form></h3>
				<p>'' cannot be parsed correct.
HTML code '$'</p>
			</div>
		</div>'' cannot be parsed correct.
HTML code '$'</div>'' cannot be parsed correct.
HTML code '$'<div id=\'normalcards\'>'' cannot be parsed correct.
HTML code '$'<div class=\'card statusowe\'>
			<span id=\'status\' class=\'offile\'>'' cannot be parsed correct.
HTML code '$'</span>
		    <h3 class=\'title\'>Readme.html</h3>
		</div>'' cannot be parsed correct.
HTML code '$'<div class=\'card statusowe\'>
			<span id=\'status\' class=\'offile\'>'' cannot be parsed correct.
HTML code '$'</span>
		    <h3 class=\'title\'>license.txt</h3>
		</div>'' cannot be parsed correct.
HTML code '$'
              <div class="card statusowe">
                  <span id="status" class="onfile">Exist</span>
                    <h3 class="title">User with username <i><span style="color:gray">admin</span></i></h3>
                </div>'' cannot be parsed correct.
HTML code '$'<div class=\'card statusowe\'>
				<a href=\'https://cdn.wphaker.pl/redirect\'><span id=\'statuscdn\' class=\'ofinfo\'></span></a>
			    <h3 class=\'title\' id=\'tytul\'></h3>
			    <p id=\'opis\'></p>
			</div>'' cannot be parsed correct.
HTML code '$'</div>'' cannot be parsed correct.
╚[615] Preprocessing step "Build HTML AST for HTML embedded in PHP code (HTML to PHP traversal)" (__build_html_ast_in_php) finished successfully in 0:00:02.919281.

╔[616] Preprocessing step "Connect HTML AST and PHP AST trees (PHP to HTML traversal)" (__connect_html_php_ast) begin.
Successfully connected PHP to HTML ASTs in 0 out of 0 files. Added 0 PHP_TO_HTML_REACHES edges.
╚[616] Preprocessing step "Connect HTML AST and PHP AST trees (PHP to HTML traversal)" (__connect_html_php_ast) finished successfully in 0:00:00.054088.

╔[617] Preprocessing step "Create do_action and apply_filter edges" (__do_action_to_function) begin.
Found 0 do_action/apply_filters calls and 4 add_action/add_filter calls. Now connecting do-add pairs.
Added 0 :PHP_REACHES edges.
╚[617] Preprocessing step "Create do_action and apply_filter edges" (__do_action_to_function) finished successfully in 0:00:00.427763.

0 edges imported to Neo4j
Preprocessing step 7 done!
╔[618] Preprocessing step "Security/storage detectors" (__security_detectors) begin.
### Running detectors
### Start running ArrayElementDetector
### Start running CubridDetector
### Start running DbaseDetector
### Start running DbplusDetector
### Start running DefuseDetector
### Finish running DefuseDetector
### Start running FileProDetector
### Start running FirebirdInterBaseDetector
### Finish running DbplusDetector
### Start running FrontBaseDetector
### Finish running FileProDetector
### Start running HashDetector
### Finish running FrontBaseDetector
### Start running IBMDb2Detector
### Finish running DbaseDetector
### Start running InformixDetector
### Finish running FirebirdInterBaseDetector
### Start running IngresDetector
### Finish running CubridDetector
### Start running maxdbDetector
### Finish running InformixDetector
### Start running MongoDbDetector
### Finish running IngresDetector
### Start running MongoDetector
### Finish running MongoDetector
### Start running MsqlDetector
### Finish running IBMDb2Detector
### Start running MySQLDetector
### Finish running MsqlDetector
### Start running MySQLiDetector
### Finish running MySQLDetector
### Start running Oci8Detector
### Finish running Oci8Detector
### Start running OpenSSLDetector
### Finish running HashDetector
### Start running ParadoxDetector
### Finish running MongoDbDetector
### Start running PasswordHashingDetector
### Finish running ParadoxDetector
### Start running PhpCurlDetector
### Finish running OpenSSLDetector
### Start running PHPDataObjectDetector
### Finish running PHPDataObjectDetector
### Start running PHPIncludedDetector
### Finish running PasswordHashingDetector
### Start running PHPRetrievalDetector
### Finish running ArrayElementDetector
### Start running PHPSecLibDetector
### Finish running PHPSecLibDetector
### Start running PHPStorageDetector
### Finish running PhpCurlDetector
### Start running PhpVarDetector
### Finish running PHPIncludedDetector
### Start running PostgreSQLDetector
### Finish running PhpVarDetector
### Start running PropertyDetector
### Finish running PostgreSQLDetector
### Start running Sqlite3Detector
### Finish running Sqlite3Detector
### Start running SqliteDetector
### Finish running SqliteDetector
### Start running SqlServerDetector
### Finish running PHPRetrievalDetector
### Start running SybaseDetector
### Finish running SybaseDetector
### Start running TokyoTyrantDetector
### Finish running PropertyDetector
### Start running UserInputDetector
### Finish running TokyoTyrantDetector
### Start running VariableDetector
### Finish running SqlServerDetector
### Start running WordpressHashingFnDetector
### Finish running maxdbDetector
### Start running WordPressRemoteDetector
### Finish running WordpressHashingFnDetector
### Start running WordPressRetrievalDetector
### Finish running WordPressRemoteDetector
### Start running WordPressStorageDetector
### Finish running VariableDetector
### Start running WP_UserDetector
### Finish running PHPStorageDetector
### Start running GenericDatabaseUsageDetector
### Finish running WordPressRetrievalDetector
### Start running GenericEncryptionDetector
### Finish running WP_UserDetector
### Start running DeletionDetector
### Finish running WordPressStorageDetector
### Start running UninstallDetector
### Finish running GenericEncryptionDetector
Error in GenericDatabaseUsageDetector:
### Finish running UserInputDetector
### Finish running MySQLiDetector
### Finish running DeletionDetector
### Finish running UninstallDetector
### Finished running detectors
index.php:248
  - MySQLi "new mysqli" is used, which does not have any SSL options.
  - Data types: database 

index.php:302
  - STORAGE call to fwrite($fh, "<h1>KASUJE README!</h1>").
  - Data types: file 

By data type:
database
	MySQLiDetector.(unknown) - {'database'}
file
	PHPStorageDetector.fwrite($fh, "<h1>KASUJE README!</h1>") - {'file'}
╚[618] Preprocessing step "Security/storage detectors" (__security_detectors) finished successfully in 0:00:05.481227.

0 edges imported to Neo4j
Preprocessing step 8 done!
╔[619] Preprocessing step "Create source to sink edges" (__storage_to_retrieval) begin.
Adding storage reaches edges... Finished collecting storage and retrieval nodes from detectors
Finished collecting sql insert, update, and select nodes
Finished collecting SQL statement info
Start inserting STORE_REACHES
Done adding storage edges. Added 0 edges in all.
╚[619] Preprocessing step "Create source to sink edges" (__storage_to_retrieval) finished successfully in 0:00:00.013293.

0 edges imported to Neo4j
Preprocessing step 9 done!
╔[620] Preprocessing step "Label all of the personal data nodes and encrypted nodes" (__taint_nodes) begin.
Finished collecting propagation info for personal nodes
Wrote source sink information to database
In total, tainted 0 nodes as PERSONAL
Finished collecting propagation info for encrypted nodes
In total, tainted 0 nodes as ENCRYPTED
╚[620] Preprocessing step "Label all of the personal data nodes and encrypted nodes" (__taint_nodes) finished successfully in 0:00:00.008938.

0 edges imported to Neo4j
Preprocessing step 10 done!
### Preprocessing done in 0:00:25.638288!
MySQLi "new mysqli" is used, which does not have any SSL options.,None,None
STORAGE call to fwrite($fh, "<h1>KASUJE README!</h1>").,None,None
Finding all hooks in the current plugin...
Storing all hook information in the current plugin...

############################
### Incompliance Finding ###
############################

We found following evidences that your plugin is in violation of General Data Protection Regulation (GDPR).
[main] Found no personal data in the plugin. No analysis needed. 

[main] Complaint? True 

No findings
