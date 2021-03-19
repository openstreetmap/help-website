+++
type = "question"
title = "Looking up NFS errors"
description = '''I would like to know how can I find some specific NFS server error using tcpdump analysis with wireshark. I am specifically interested in finding if the NFS server is returning NFS3ERR_BADHANDLE = 10001 or NFS3ERR_IO = 5 when issuing a read request.  I am also unable to &quot;follow tcp stream&quot; for a NFS...'''
date = "2014-02-15T07:01:00Z"
lastmod = "2014-02-15T09:34:00Z"
weight = 29888
keywords = [ "nfs" ]
aliases = [ "/questions/29888" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Looking up NFS errors](/questions/29888/looking-up-nfs-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29888-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to know how can I find some specific NFS server error using tcpdump analysis with wireshark. I am specifically interested in finding if the NFS server is returning NFS3ERR_BADHANDLE = 10001 or NFS3ERR_IO = 5 when issuing a read request.</p><p>I am also unable to "follow tcp stream" for a NFS READ request to see what the server returned for that request. Sorry, for a newbie kind of question.</p></div><div id="question-tags" class="tags-container tags">nfs</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '14, 07:01</strong></p><img src="https://secure.gravatar.com/avatar/4ddaa59201e213ee3a414fe09a91d024?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sumit&#39;s gravatar image" /><p>sumit<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sumit has no accepted answers">0%</span></p></div></div><div id="comments-container-29888" class="comments-container"></div><div id="comment-tools-29888" class="comment-tools"></div><div class="clear"></div><div id="comment-29888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29891"></span>

<div id="answer-container-29891" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29891-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Did you try this filter: <code>nfs.status == 10001 or nfs.status == 5</code> ?</p><p>You can also add nfs.status / nfs.nfsstat3 as a column and sort on the column ... <img src="https://osqa-ask.wireshark.org/upfiles/NFSError.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '14, 09:34</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 15 Feb '14, 09:35</p></div></div><div id="comments-container-29891" class="comments-container"><span id="29919"></span><div id="comment-29919" class="comment"><div id="post-29919-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your help. I had tried looking up using the filter nfs.status == 10001 or nfs.status == 5, but not got any results. So I deduced that there is no such error being reported back.</p><p>Following your suggestion I also added nfs.status, nfs.status2 and nfs.status3 columns to the display. However, those columns report nothing.</p></div><div id="comment-29919-info" class="comment-info"><span class="comment-age">(16 Feb '14, 19:51)</span> sumit</div></div><span id="29920"></span><div id="comment-29920" class="comment"><div id="post-29920-score" class="comment-score"></div><div class="comment-text"><p>Assuming that your capture actually contains nfs frames, if you get "nothing" (i.e., blank ?) for nfs.status, then I'd say something is not right since I would expect that there would almost always be an nfs.status field for "server replies".</p><p>Do you see "status" fields in the dissection detail pane for any of the replies from the server ?</p></div><div id="comment-29920-info" class="comment-info"><span class="comment-age">(16 Feb '14, 20:36)</span> Bill Meier ♦♦</div></div><span id="29922"></span><div id="comment-29922" class="comment"><div id="post-29922-score" class="comment-score"></div><div class="comment-text"><p>The issue turned out to be that network admin did not capture tcpdump correctly with "host" option but did so, with only dst option :-)</p><p>As soon as I followed your advice on adding status to display fields and saw it blank, I figured that. Thanks a ton!</p></div><div id="comment-29922-info" class="comment-info"><span class="comment-age">(16 Feb '14, 22:01)</span> sumit</div></div></div><div id="comment-tools-29891" class="comment-tools"></div><div class="clear"></div><div id="comment-29891-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

