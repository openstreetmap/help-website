+++
type = "question"
title = "How to export http.data with tshark?"
description = '''Hi, I want to read tcpdump capture file and export just http request body as individual byte array. How to do that? I tried this  tshark -r mycapture.cap -R &#x27;http.request and (http contains &quot;customheader:&quot;)&#x27; -T fields -e data -w data.cap  But it save all the requests with headers (I just want the ht...'''
date = "2013-02-18T10:07:00Z"
lastmod = "2013-02-18T10:07:00Z"
weight = 18710
keywords = [ "tshark" ]
aliases = [ "/questions/18710" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to export http.data with tshark?](/questions/18710/how-to-export-httpdata-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18710-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to read tcpdump capture file and export just http request body as individual byte array. How to do that? I tried this</p><pre><code>tshark -r mycapture.cap -R &#39;http.request and (http contains &quot;customheader:&quot;)&#39; -T fields -e data -w data.cap</code></pre><p>But it save all the requests with headers (I just want the http body only). Also it doesn't save http body as individual file.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '13, 10:07</strong></p><img src="https://secure.gravatar.com/avatar/7656adad2ef7c5ac31f6a55fcdb1734d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seannguyen&#39;s gravatar image" /><p>seannguyen<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seannguyen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Feb '13, 11:16</p></div></div><div id="comments-container-18710" class="comments-container"></div><div id="comment-tools-18710" class="comment-tools"></div><div class="clear"></div><div id="comment-18710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

