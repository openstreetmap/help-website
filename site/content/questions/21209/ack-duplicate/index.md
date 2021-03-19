+++
type = "question"
title = "ACK Duplicate"
description = '''We have two servers which are used for data replication between them. Issues 1.During replication the connectivity is getting down/slow regularly and packet is getting lost.Please find the below logs for your kind![alt text][1] reference. 8954069.0: ethernet0/1(i) len=70:002451aefc00-&amp;gt;00239c82b80...'''
date = "2013-05-17T01:01:00Z"
lastmod = "2013-05-17T07:29:00Z"
weight = 21209
keywords = [ "error" ]
aliases = [ "/questions/21209" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ACK Duplicate](/questions/21209/ack-duplicate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21209-score" class="post-score" title="current number of votes">0</div><span id="post-21209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have two servers which are used for data replication between them.</p><p>Issues</p><p>1.During replication the connectivity is getting down/slow regularly and packet is getting lost.Please find the below logs for your kind![alt text][1] reference.</p><pre><code>8954069.0: ethernet0/1(i) len=70:002451aefc00-&gt;00239c82b805/8100/0800, tag 635
              10.1.1.1 -&gt; 192.1.1.1/6
              vhl=45, tos=00, id=47907, frag=4000, ttl=63 tlen=52
              tcp:ports 57105-&gt;10560, seq=2650136876, ack=314843383, flag=8010/ACK
              00 23 9c 82 b8 05 00 24 51 ae fc 00 81 00 02 7b     .#.....$Q......{
              08 00 45 00 00 34 bb 23 40 00 3f 06 98 ab 0a 0b     ..E..4.#@.?.....
              10 b6 c0 a8 0c 8c df 11 29 40 9d f5 e1 2c 12 c4     ........)@...,..
              20 f7 80 10 00 26 5e 24 00 00 01 01 08 0a 86 a9     .....&amp;^$........
              57 7c 65 0d 32 1b                                   W|e.2.

8954069.0: ethernet0/2(o) len=66:00239c82b806-&gt;002283a4d989/0800
              10.1.1.1 -&gt; 192.1.1.1/6
              vhl=45, tos=00, id=47907, frag=4000, ttl=62 tlen=52
              tcp:ports 57105-&gt;10560, seq=2650136876, ack=314843383, flag=8010/ACK
              00 22 83 a4 d9 89 00 23 9c 82 b8 06 08 00 45 00     .&quot;.....#......E.
              00 34 bb 23 40 00 3e 06 99 ab 0a 0b 10 b6 c0 a8     .4.#@.&gt;.........
              0c 8c df 11 29 40 9d f5 e1 2c 12 c4 20 f7 80 10     ....)@...,......
              00 26 5e 24 00 00 01 01 08 0a 86 a9 57 7c 65 0d     .&amp;^$........W|e.
              32 1b                                               2.

8954069.0: ethernet0/2(i) len=66:002283a4d989-&gt;00239c82b806/0800
              192.1.1.1 -&gt; 10.1.1.1/6
              vhl=45, tos=00, id=10758, frag=4000, ttl=61 tlen=52
              tcp:ports 10560-&gt;57105, seq=314843383, ack=2650136877, flag=8010/ACK
              00 23 9c 82 b8 06 00 22 83 a4 d9 89 08 00 45 00     .#.....&quot;......E.
              00 34 2a 06 40 00 3d 06 2b c9 c0 a8 0c 8c 0a 0b     .4*[email protected]=.+.......
              10 b6 29 40 df 11 12 c4 20 f7 9d f5 e1 2d 80 10     ..)@.........-..
              00 23 5d ed 00 00 01 01 08 0a 65 0f 06 f6 86 a7     .#].......e.....
              82 da                                               ..

8954069.0: ethernet0/1(o) len=70:00239c82b805-&gt;002451aefc00/8100/0800, tag 635
              192.1.1.1 -&gt; 10.1.1.1/6
              vhl=45, tos=00, id=10758, frag=4000, ttl=60 tlen=52
              tcp:ports 10560-&gt;57105, seq=314843383, ack=2650136877, flag=8010/ACK
              00 24 51 ae fc 00 00 23 9c 82 b8 05 81 00 02 7b     .$Q....#.......{
              08 00 45 00 00 34 2a 06 40 00 3c 06 2c c9 c0 a8     ..E..4*[email protected]&lt;.,...
              0c 8c 0a 0b 10 b6 29 40 df 11 12 c4 20 f7 9d f5     ......)@........
              e1 2d 80 10 00 23 5d ed 00 00 01 01 08 0a 65 0f     .-...#].......e.
              06 f6 86 a7 82 da                                   ......

8954069.0: ethernet0/2(i) len=66:002283a4d989-&gt;00239c82b806/0800
              192.1.1.1 -&gt; 10.1.1.1/6
              vhl=45, tos=00, id=10759, frag=4000, ttl=61 tlen=52
              tcp:ports 10560-&gt;57105, seq=314843382, ack=2650136877, flag=8010/ACK
              00 23 9c 82 b8 06 00 22 83 a4 d9 89 08 00 45 00     .#.....&quot;......E.
              00 34 2a 07 40 00 3d 06 2b c8 c0 a8 0c 8c 0a 0b     .4*[email protected]=.+.......
              10 b6 29 40 df 11 12 c4 20 f6 9d f5 e1 2d 80 10     ..)@.........-..
              00 23 5d cf 00 00 01 01 08 0a 65 0f 07 15 86 a7     .#].......e.....
              82 da                                               ..

8954069.0: ethernet0/1(o) len=70:00239c82b805-&gt;002451aefc00/8100/0800, tag 635
              192.1.1.1 -&gt; 10.1.1.1/6
              vhl=45, tos=00, id=10759, frag=4000, ttl=60 tlen=52
              tcp:ports 10560-&gt;57105, seq=314843382, ack=2650136877, flag=8010/ACK
              00 24 51 ae fc 00 00 23 9c 82 b8 05 81 00 02 7b     .$Q....#.......{
              08 00 45 00 00 34 2a 07 40 00 3c 06 2c c8 c0 a8     ..E..4*[email protected]&lt;.,...
              0c 8c 0a 0b 10 b6 29 40 df 11 12 c4 20 f6 9d f5     ......)@........
              e1 2d 80 10 00 23 5d cf 00 00 01 01 08 0a 65 0f     .-...#].......e.
              07 15 86 a7 82 da                                   ......

8954069.0: ethernet0/1(i) len=70:002451aefc00-&gt;00239c82b805/8100/0800, tag 635
              10.1.1.1 -&gt; 192.1.1.1/6
              vhl=45, tos=00, id=47908, frag=4000, ttl=63 tlen=52
              tcp:ports 57105-&gt;10560, seq=2650136877, ack=314843383, flag=8010/ACK
              00 23 9c 82 b8 05 00 24 51 ae fc 00 81 00 02 7b     .#.....$Q......{
              08 00 45 00 00 34 bb 24 40 00 3f 06 98 aa 0a 0b     [email protected]?.....
              10 b6 c0 a8 0c 8c df 11 29 40 9d f5 e1 2d 12 c4     ........)@...-..
              20 f7 80 10 00 26 89 0c 00 00 01 01 08 0a 86 a9     .....&amp;..........
              57 b6 65 0f 06 f6                                   W.e...

8954069.0: ethernet0/2(o) len=66:00239c82b806-&gt;002283a4d989/0800
              10.1.1.1 -&gt; 192.1.1.1/6
              vhl=45, tos=00, id=47908, frag=4000, ttl=62 tlen=52
              tcp:ports 57105-&gt;10560, seq=2650136877, ack=314843383, flag=8010/ACK
              00 22 83 a4 d9 89 00 23 9c 82 b8 06 08 00 45 00     .&quot;.....#......E.
              00 34 bb 24 40 00 3e 06 99 aa 0a 0b 10 b6 c0 a8     [email protected]&gt;.........
              0c 8c df 11 29 40 9d f5 e1 2d 12 c4 20 f7 80 10     ....)@...-......
              00 26 89 0c 00 00 01 01 08 0a 86 a9 57 b6 65 0f     .&amp;..........W.e.
              06 f6                                               ..

8954085.0: ethernet0/1(i) len=70:002451aefc00-&gt;00239c82b805/8100/0800, tag 635
              10.1.1.1 -&gt; 192.1.1.1/6
              vhl=45, tos=00, id=38820, frag=4000, ttl=63 tlen=52
              tcp:ports 59983-&gt;10560, seq=3297725813, ack=966268089, flag=8010/ACK
              00 23 9c 82 b8 05 00 24 51 ae fc 00 81 00 02 7b     .#.....$Q......{
              08 00 45 00 00 34 97 a4 40 00 3f 06 bc 2a 0a 0b     [email protected]?..*..
              10 b6 c0 a8 0c 8c ea 4f 29 40 c4 8f 4d 75 39 98     .......O)@..Mu9.
              14 b9 80 10 00 26 25 c2 00 00 01 01 08 0a 86 a9     .....&amp;%.........
              97 36 65 0d 72 0c                                   .6e.r.

8954085.0: ethernet0/2(o) len=66:00239c82b806-&gt;002283a4d989/0800
              10.1.1.1 -&gt; 192.1.1.1/6
              vhl=45, tos=00, id=38820, frag=4000, ttl=62 tlen=52
              tcp:ports 59983-&gt;10560, seq=3297725813, ack=966268089, flag=8010/ACK
              00 22 83 a4 d9 89 00 23 9c 82 b8 06 08 00 45 00     .&quot;.....#......E.
              00 34 97 a4 40 00 3e 06 bd 2a 0a 0b 10 b6 c0 a8     [email protected]&gt;..*......
              0c 8c ea 4f 29 40 c4 8f 4d 75 39 98 14 b9 80 10     ...O)@..Mu9.....
              00 26 25 c2 00 00 01 01 08 0a 86 a9 97 36 65 0d     .&amp;%..........6e.
              72 0c                                               r.

8954085.0: ethernet0/2(i) len=66:002283a4d989-&gt;00239c82b806/0800
              192.1.1.1 -&gt; 10.1.1.1/6
              vhl=45, tos=00, id=31902, frag=4000, ttl=61 tlen=52
              tcp:ports 10560-&gt;59983, seq=966268089, ack=3297725814, flag=8010/ACK
              00 23 9c 82 b8 06 00 22 83 a4 d9 89 08 00 45 00     .#.....&quot;......E.
              00 34 7c 9e 40 00 3d 06 d9 30 c0 a8 0c 8c 0a 0b     .4|[email protected]=..0......
              10 b6 29 40 ea 4f 39 98 14 b9 c4 8f 4d 76 80 10     ..)@.O9.....Mv..
              00 47 25 86 00 00 01 01 08 0a 65 0f 46 b0 86 a7     .G%.......e.F...
              c2 ac                                               ..

8954085.0: ethernet0/1(o) len=70:00239c82b805-&gt;002451aefc00/8100/0800, tag 635
              192.1.1.1 -&gt; 10.1.1.1/6
              vhl=45, tos=00, id=31902, frag=4000, ttl=60 tlen=52
              tcp:ports 10560-&gt;59983, seq=966268089, ack=3297725814, flag=8010/ACK
              00 24 51 ae fc 00 00 23 9c 82 b8 05 81 00 02 7b     .$Q....#.......{
              08 00 45 00 00 34 7c 9e 40 00 3c 06 da 30 c0 a8     ..E..4|[email protected]&lt;..0..
              0c 8c 0a 0b 10 b6 29 40 ea 4f 39 98 14 b9 c4 8f     ......)@.O9.....
              4d 76 80 10 00 47 25 86 00 00 01 01 08 0a 65 0f     Mv...G%.......e.
              46 b0 86 a7 c2 ac                                   F.....

8954085.0: ethernet0/2(i) len=66:002283a4d989-&gt;00239c82b806/0800
              192.1.1.1 -&gt; 10.1.1.1/6
              vhl=45, tos=00, id=31903, frag=4000, ttl=61 tlen=52
              tcp:ports 10560-&gt;59983, seq=966268088, ack=3297725814, flag=8010/ACK
              00 23 9c 82 b8 06 00 22 83 a4 d9 89 08 00 45 00     .#.....&quot;......E.
              00 34 7c 9f 40 00 3d 06 d9 2f c0 a8 0c 8c 0a 0b     .4|[email protected]=../......
              10 b6 29 40 ea 4f 39 98 14 b8 c4 8f 4d 76 80 10     ..)@.O9.....Mv..
              00 47 25 50 00 00 01 01 08 0a 65 0f 46 e7 86 a7     .G%P......e.F...
              c2 ac                                               ..

8954085.0: ethernet0/1(o) len=70:00239c82b805-&gt;002451aefc00/8100/0800, tag 635
              192.1.1.1 -&gt; 10.1.1.1/6
              vhl=45, tos=00, id=31903, frag=4000, ttl=60 tlen=52
              tcp:ports 10560-&gt;59983, seq=966268088, ack=3297725814, flag=8010/ACK
              00 24 51 ae fc 00 00 23 9c 82 b8 05 81 00 02 7b     .$Q....#.......{
              08 00 45 00 00 34 7c 9f 40 00 3c 06 da 2f c0 a8     ..E..4|[email protected]&lt;../..
              0c 8c 0a 0b 10 b6 29 40 ea 4f 39 98 14 b8 c4 8f     ......)@.O9.....
              4d 76 80 10 00 47 25 50 00 00 01 01 08 0a 65 0f     Mv...G%P......e.
              46 e7 86 a7 c2 ac                                   F.....

8954085.0: ethernet0/1(i) len=70:002451aefc00-&gt;00239c82b805/8100/0800, tag 635
              10.1.1.1 -&gt; 192.1.1.1/6
              vhl=45, tos=00, id=38821, frag=4000, ttl=63 tlen=52
              tcp:ports 59983-&gt;10560, seq=3297725814, ack=966268089, flag=8010/ACK
              00 23 9c 82 b8 05 00 24 51 ae fc 00 81 00 02 7b     .#.....$Q......{
              08 00 45 00 00 34 97 a5 40 00 3f 06 bc 29 0a 0b     [email protected]?..)..
              10 b6 c0 a8 0c 8c ea 4f 29 40 c4 8f 4d 76 39 98     .......O)@..Mv9.
              14 b9 80 10 00 26 50 c9 00 00 01 01 08 0a 86 a9     .....&amp;P.........
              97 88 65 0f 46 b0                                   ..e.F.

8954085.0: ethernet0/2(o) len=66:00239c82b806-&gt;002283a4d989/0800
              10.1.1.1 -&gt; 192.1.1.1/6
              vhl=45, tos=00, id=38821, frag=4000, ttl=62 tlen=52
              tcp:ports 59983-&gt;10560, seq=3297725814, ack=966268089, flag=8010/ACK
              00 22 83 a4 d9 89 00 23 9c 82 b8 06 08 00 45 00     .&quot;.....#......E.
              00 34 97 a5 40 00 3e 06 bd 29 0a 0b 10 b6 c0 a8     [email protected]&gt;..)......
              0c 8c ea 4f 29 40 c4 8f 4d 76 39 98 14 b9 80 10     ...O)@..Mv9.....
              00 26 50 c9 00 00 01 01 08 0a 86 a9 97 88 65 0f     .&amp;P...........e.
              46 b0                                               F.</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '13, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/70cda262f034ebd66176928947ddf47c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sriram&#39;s gravatar image" /><p><span>sriram</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sriram has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 May '13, 01:08</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-21209" class="comments-container"></div><div id="comment-tools-21209" class="comment-tools"></div><div class="clear"></div><div id="comment-21209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21225"></span>

<div id="answer-container-21225" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21225-score" class="post-score" title="current number of votes">0</div><span id="post-21225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are the servers linux? If so look to iptables to help troubleshoot. Here is a good article to log the dropped packets:</p><p><a href="http://www.thegeekstuff.com/2012/08/iptables-log-packets/">http://www.thegeekstuff.com/2012/08/iptables-log-packets/</a></p><p>I have also in the past had issues with slow/drooped connections when one device is implementing 802.1Q VLAN tagging and the other is not but seeing that you are going from private class A to class C subnet I would think it may be with the masking either on one of the servers or a router inbetween.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '13, 07:29</strong></p><img src="https://secure.gravatar.com/avatar/0a095f587cc7884054c4edac3d197786?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Pando&#39;s gravatar image" /><p><span>Andy Pando</span><br />
<span class="score" title="12 reputation points">12</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Pando has no accepted answers">0%</span></p></div></div><div id="comments-container-21225" class="comments-container"></div><div id="comment-tools-21225" class="comment-tools"></div><div class="clear"></div><div id="comment-21225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

