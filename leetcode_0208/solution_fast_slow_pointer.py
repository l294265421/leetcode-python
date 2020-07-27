# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 Baidu.com, Inc. All Rights Reserved
#
"""

这个问题你可以用数学归纳法来思考。首先，由于链表是个环，所以相遇的过程可以看作是快指针从后边追
赶慢指针的过程。那么做如下思考：
1：快指针与慢指针之间差一步。此时继续往后走，慢指针前进一步，快指针
前进两步，两者相遇。
2：快指针与慢指针之间差两步。此时唏嘘往后走，慢指针前进一步，快指针前进两步，两者之间相差一步，
转化为第一种情况。3：快指针与慢指针之间差N步。此时继续往后走，慢指针前进一步，快指针前进两步，
两者之间相差(N+1-2)-> N-1步。
因此，此题得证。所以快指针必然与慢指针相遇。又因为快指针速度是慢指针
的两倍，所以相遇时慢指针必然只绕了一圈。




Authors: liyuncong(liyuncong@baidu.com)
Date:    2020/7/27 11:23
"""