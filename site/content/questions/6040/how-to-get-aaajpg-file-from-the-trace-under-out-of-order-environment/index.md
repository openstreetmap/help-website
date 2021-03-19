+++
type = "question"
title = "How to get AAA.jpg file from the trace under Out-of-Order environment"
description = ''' Currently, I&#x27;ve faced sme problem while uploading the file to ftp server. If I upload the file via ftp-put command, sometimes a few thousand bytes was changed from original file. But, it isn&#x27;t happen always... just once in a month... anyway, I&#x27;ve captured the trace from all possible points as attac...'''
date = "2011-08-31T19:22:00Z"
lastmod = "2011-09-01T08:17:00Z"
weight = 6040
keywords = [ "follow", "stream", "tcp" ]
aliases = [ "/questions/6040" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get AAA.jpg file from the trace under Out-of-Order environment](/questions/6040/how-to-get-aaajpg-file-from-the-trace-under-out-of-order-environment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6040-score" class="post-score" title="current number of votes">0</div><span id="post-6040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="http://www.protocolmaster.co.kr/download/ftp-data-topo.png" alt="alt text" /></p><p>Currently, I've faced sme problem while uploading the file to ftp server. If I upload the file via ftp-put command, sometimes a few thousand bytes was changed from original file. But, it isn't happen always... just once in a month... anyway, I've captured the trace from all possible points as attached points and tried to filter out(Follow TCP Stream &gt; RAW &gt; Save As) AAA.jpg from each point then, compare these /w origin file.</p><p>It was simple job but unexpected problem was occurred. Thru the network, many packets changed its' order set. For example, packets transfered /w sequence number 1,2,3,4,5,6 but receiver get the packets 1,2,4,5,6,3.</p><p>The biggest problem is... 'Follow TCP Stream' just re-assemble the trace as it is... packet orderset by 1,2,4,5,6,3. So, it cannot be compared /w origin file. Is there any solution to sort the packets by sequence number?</p><p>Thanks. -Sunny</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-follow" rel="tag" title="see questions tagged &#39;follow&#39;">follow</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Aug '11, 19:22</strong></p><img src="https://secure.gravatar.com/avatar/3e6308f1567aab76eb8e68c5e4a9b284?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sunny%20Hilliter&#39;s gravatar image" /><p><span>Sunny Hilliter</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sunny Hilliter has no accepted answers">0%</span></p></img></div></div><div id="comments-container-6040" class="comments-container"><span id="6046"></span><div id="comment-6046" class="comment"><div id="post-6046-score" class="comment-score"></div><div class="comment-text"><p>Getting back to your original problem: Are you sure you always transfer the file in binary mode?</p></div><div id="comment-6046-info" class="comment-info"><span class="comment-age">(01 Sep '11, 08:17)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-6040" class="comment-tools"></div><div class="clear"></div><div id="comment-6040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6042"></span>

<div id="answer-container-6042" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6042-score" class="post-score" title="current number of votes">0</div><span id="post-6042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Follow TCP Stream is supposed to reorder packets so that the stream is presented the same way as it is to the application. So in your case, all the RAW exports should be the same. If not, there might be any of these issues:</p><ul><li><p>The TCP sequence numbers of the packets are messed up, messing up the reassembly done by "Follow TCP stream", but this will also mess up the reception of the file.</p></li><li><p>There is a bug in the "Follow TCP Stream" code in Wireshark, if you think this is the case, could you file a bug at <a href="https://bugs.wireshark.org/">https://bugs.wireshark.org/</a> and attach the tracefile that is exhibiting this behavior?</p></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '11, 23:58</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6042" class="comments-container"></div><div id="comment-tools-6042" class="comment-tools"></div><div class="clear"></div><div id="comment-6042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

