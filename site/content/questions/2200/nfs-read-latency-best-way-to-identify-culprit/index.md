+++
type = "question"
title = "NFS Read latency - best way to identify culprit"
description = '''Hi, I have a repeatable event with a specific job run on SLES10 box acessing an EMC celerra. I see very high READ latency (Max RTT). How can I see which file(s) is responsible for this latency. Here are two examples:  I used the following filter with tshark: -q -z rpc,rtt,100003,3,&#x27;nfs.nfsstat3!=70&#x27;...'''
date = "2011-02-07T09:53:00Z"
lastmod = "2011-02-07T18:36:00Z"
weight = 2200
keywords = [ "latency", "nfs", "emc" ]
aliases = [ "/questions/2200" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [NFS Read latency - best way to identify culprit](/questions/2200/nfs-read-latency-best-way-to-identify-culprit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2200-score" class="post-score" title="current number of votes">0</div><span id="post-2200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a repeatable event with a specific job run on SLES10 box acessing an EMC celerra. I see very high READ latency (Max RTT). How can I see which file(s) is responsible for this latency. Here are two examples: I used the following filter with <code>tshark:  -q -z rpc,rtt,100003,3,'nfs.nfsstat3!=70'</code> Note the very high Max RTT for READ procedure.</p><pre><code>NFS Version 3 RTT Statistics:
Filter: nfs.nfsstat3!=70
Procedure        Calls   Min RTT   Max RTT   Avg RTT
NULL                 0   0.00000   0.00000   0.00000
GETATTR         1517132   0.00000   0.58692   0.00105
SETATTR             21   0.00088   0.00954   0.00155
LOOKUP          11581651   0.00001   0.98236   0.00036
ACCESS          887419   0.00000   0.18176   0.00024
READLINK         11462   0.00013   0.43970   0.00689
READ            376117   0.00009 8854.46070   0.46602
WRITE              748   0.00033   0.08924   0.01823
CREATE               8   0.00111   0.02262   0.00607
MKDIR                1   0.00633   0.00633   0.00633
SYMLINK              0   0.00000   0.00000   0.00000
MKNOD                0   0.00000   0.00000   0.00000
REMOVE               7   0.00021   0.00865   0.00342
RMDIR                1   0.00117   0.00117   0.00117
RENAME               2   0.00112   0.00113   0.00112
LINK                 0   0.00000   0.00000   0.00000
READDIR            601   0.00016   0.03231   0.00037
READDIRPLUS       8254   0.00015   0.21962   0.00372
FSSTAT               0   0.00000   0.00000   0.00000
FSINFO              27   0.00013   0.00383   0.00071
PATHCONF             0   0.00000   0.00000   0.00000
COMMIT               3   0.00393   0.01380   0.00765

NFS Version 3 RTT Statistics:
Filter: nfs.nfsstat3!=70
Procedure        Calls   Min RTT   Max RTT   Avg RTT
NULL                 0   0.00000   0.00000   0.00000
GETATTR         1425693   0.00000   0.59928   0.00099
SETATTR             21   0.00038   0.00070   0.00056
LOOKUP          11613451   0.00001   0.68981   0.00029
ACCESS          814987   0.00000   0.04566   0.00022
READLINK         11505   0.00003   0.37694   0.00704
READ            364942   0.00011 7943.28530   2.72942
WRITE              845   0.00029   0.57347   0.01104
CREATE               8   0.00053   0.01336   0.00282
MKDIR                1   0.00073   0.00073   0.00073
SYMLINK              0   0.00000   0.00000   0.00000
MKNOD                0   0.00000   0.00000   0.00000
REMOVE               5   0.00077   0.01270   0.00509
RMDIR                1   0.00067   0.00067   0.00067
RENAME               2   0.00044   0.00051   0.00048
LINK                 0   0.00000   0.00000   0.00000
READDIR            601   0.00016   0.10647   0.00156
READDIRPLUS       8254   0.00014   0.11047   0.00389
FSSTAT               0   0.00000   0.00000   0.00000
FSINFO               3   0.00026   0.00032   0.00028
PATHCONF             0   0.00000   0.00000   0.00000
COMMIT               3   0.00241   0.00939   0.00486</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-latency" rel="tag" title="see questions tagged &#39;latency&#39;">latency</span> <span class="post-tag tag-link-nfs" rel="tag" title="see questions tagged &#39;nfs&#39;">nfs</span> <span class="post-tag tag-link-emc" rel="tag" title="see questions tagged &#39;emc&#39;">emc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Feb '11, 09:53</strong></p><img src="https://secure.gravatar.com/avatar/80ec40e1e7b5c00d1bdfa2f15021dc3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="debugme&#39;s gravatar image" /><p><span>debugme</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="debugme has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Feb '11, 10:22</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-2200" class="comments-container"></div><div id="comment-tools-2200" class="comment-tools"></div><div class="clear"></div><div id="comment-2200-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2202"></span>

<div id="answer-container-2202" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2202-score" class="post-score" title="current number of votes">0</div><span id="post-2202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use <code>tshark -r &lt;file&gt; -R "rpc.time&gt;3600"</code> to find all responses that took more than an hour.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '11, 10:26</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2202" class="comments-container"><span id="2206"></span><div id="comment-2206" class="comment"><div id="post-2206-score" class="comment-score"></div><div class="comment-text"><p>Thank you SYNbit. rpc.time &gt; 3600 returns a number of frames with NFS [Illegal Segments], i'm not sure what that means ... reassembly issues, lock / permission issues. Are there doc's out there which explain what NFS [Illegal Segments] means?</p><p>thanks</p></div><div id="comment-2206-info" class="comment-info"><span class="comment-age">(07 Feb '11, 13:02)</span> <span class="comment-user userinfo">debugme</span></div></div><span id="2207"></span><div id="comment-2207" class="comment"><div id="post-2207-score" class="comment-score"></div><div class="comment-text"><p>There are no docs available on each and every field. As this is Wireshark generated (because of the square brackets around Illegal Segments), it is probably a problem in the re-assembly. Maybe because of a problem with the packets themselves (which might coincide with the problems you are facing) or maybe a bug in Wireshark.</p><p>Are you able to share the trace-file? If so, I can have a look if I can pinpoint it. See my profile for my e-mail address...</p></div><div id="comment-2207-info" class="comment-info"><span class="comment-age">(07 Feb '11, 14:40)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="2208"></span><div id="comment-2208" class="comment"><div id="post-2208-score" class="comment-score"></div><div class="comment-text"><p>If there is a pcap file available we can take a look at it for you. The biggest issues with NFS is that v3 (pretty common) has a read block limit of 32KB. So per RTT, you can only transfer 32KB.<br />
</p><p>If the problem is CPU or IO issues within EMC, the trace file can point it out. If it's an intermittent problem, I would look at the usual suspects as a start (pkt loss, CPU, AntiVirus locking up files)</p></div><div id="comment-2208-info" class="comment-info"><span class="comment-age">(07 Feb '11, 18:36)</span> <span class="comment-user userinfo">hansangb</span></div></div></div><div id="comment-tools-2202" class="comment-tools"></div><div class="clear"></div><div id="comment-2202-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

