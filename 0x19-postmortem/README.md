# **Postmortem: E-commerce Checkout Failure (May 5, 2024)**

## **Issue Summary**

### **Duration: 75 minutes (10:15 AM EAT - 11:30 AM EAT)**

Impact: Slow checkout process for our e-commerce platform. Several online users complained that they experienced extended page loading times and delays during checkout. Most users complained that they experienced total product catalogue page failure to load during the outage window.

#### **Root Cause:**

- Database connection exceeded due to a recent database query optimization which resulted in multiple queries to the database by users from a single catalogue request.

**Timeline**

- 10:15 AM EAT: Monitoring alerts flagged a significant increase in response times for the checkout API and failure to complete checkout.
- 10:30 AM EAT: The engineering team investigated and identified slow queries impacting the checkout database and service response times.
- 10 :30 AM EAT - 10:45 AM EAT: The Initial investigation focused on potential database server request overload. The team began to check the database server resources such as CPU, memory and data flows(both egress and ingress) appeared abnormal.
- 10:45 AM EAT - 10:50 AM EAT: Investigation shifted towards analyzing slow queries in the checkout database. A recent code update optimizing a specific product search query was identified as a potential culprit.
- 11:00 AM EAT: The engineering team reverted the recent product search query optimization and also provided a database scale in and out procedure to increase database capacity depending on the level of user requests.
- 11:05 AM EAT: Systems monitoring confirmed an immediate response from the web app where they noted a decrease in the amount of time to check out on product catalogue response times and a return to normal functionality.
- 11:30 AM EAT: Post-mortem meeting convened to discuss this incident after it was monitored and established as working ok and any potential issues that may arise to provide automated preventative measures.

#### **Root Cause and Resolution**

The root cause of the slowdown was a recently deployed code update that optimized a product search query within the checkout database. This eventually led to the master database being overwhelmed with multiple user requests on the product catalogue. While the optimization improved search performance on product listing pages, it resulted in more complex querying that overloaded the database connection during the checkout process. Reversing the code back to the previous working state managed to temporarily resolve the issue and restored normal checkout functionality.

**Corrective and Preventative Measures**

1. _Improve Code Review Process_: The code review process will be updated to include a focus on potential database performance impacts for all code changes.
2. _Database scale in and out_: The team decided to design read replica databases to handle frequent user catalogue requests to provide only for upsurge user requests during peak usage times. This would allow for scale out or scale in depending on peak usage times during business hours or holidays.

3. _Automated Testing_: Develop automated tests that simulate checkout workflows and monitor performance metrics to catch regressions before deployment.
4. _Performance Profiling_: Perform continuous testing on all critical database queries to identify opportunities for optimization without compromising overall system stability. This will be automated and done during business hours or times when low traffic is present. The automation will provide reports that can be analyzed and then implemented with future planning.

This postmortem gives a clear picture of the importance of a thorough code review process and proactive monitoring for critical systems. By implementing the corrective and preventative measures outlined above, we can minimize the risk of similar incidents in the future.
