from .connection import mysqldb


def get_tickets_brand_level_since(datetimestamp):
    query = '''
    SELECT
	    prod_cssurvey.tickets.ticketCreated as CreatedAt,
        prod_cssurvey.products.brand as Brand,
        IF(ISNULL(prod_cssurvey.agents.group),"L1 Agent",prod_cssurvey.agents.group) as Level
    FROM
	    prod_cssurvey.tickets
    LEFT JOIN
	    prod_cssurvey.agents ON prod_cssurvey.tickets.firstAssignee = prod_cssurvey.agents.agentId
    LEFT JOIN
	    prod_cssurvey.products ON prod_cssurvey.tickets.companyId = prod_cssurvey.products.productId
    WHERE
	    prod_cssurvey.tickets.ticketCreated >= "{}"
    ORDER BY
	    prod_cssurvey.tickets.ticketCreated DESC
    '''
    query = query.format(datetimestamp)
    cursor = mysqldb.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()

    return result, cursor.column_names, cursor.rowcount
