+++
type = "question"
title = "Citrix intermittent hang"
description = '''Hi Folks, Citrix issues again. We&#x27;re experiencing intermittent hangs and unresponsiveness I managed to get a capture taken from the client side and have analysed some basic details from it but I feel my experience is insufficient to truly know what I&#x27;m seeing or not seeing. I have anonymised the dat...'''
date = "2017-01-19T01:06:00Z"
lastmod = "2017-01-19T01:06:00Z"
weight = 58879
keywords = [ "autodesk", "citrix" ]
aliases = [ "/questions/58879" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Citrix intermittent hang](/questions/58879/citrix-intermittent-hang)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58879-score" class="post-score" title="current number of votes">0</div><span id="post-58879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Folks,</p><p>Citrix issues again. We're experiencing intermittent hangs and unresponsiveness I managed to get a capture taken from the client side and have analysed some basic details from it but I feel my experience is insufficient to truly know what I'm seeing or not seeing. I have anonymised the data in the capture using trace wrangler and it available a the link below</p><p><a href="https://www.dropbox.com/s/ljgff96uctvvn1c/Citrix%20PCap%201_anon.pcapng?dl=0">https://www.dropbox.com/s/ljgff96uctvvn1c/Citrix%20PCap%201_anon.pcapng?dl=0</a></p><p>The Stream of interest is 'TCP-Stream 0' 192.168.76.222 -&lt;&gt;- 192.168.159.242</p><p>I see batches of DUP ACKs but it's not clear to me what the cause of the DUP ACK are. I also see some points in time where the TCP delta time is high but this doesn't correspond with hangs or TCP errors which confuses me. Perhaps it's a simple case of latency on the network in between the client server. But I would really appreciate an expert opinion please?</p><p>One item to note is that while I was capturing the wireshark file I was remotely accessing the users client machine using team viewer. During the session I witnessed the Citrix session hang but the Teamviewer session never froze.</p><p>The IP's of the Teamviewer stream 192.168.251 -&lt;&gt;- 192.168.159.242</p><p>thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-autodesk" rel="tag" title="see questions tagged &#39;autodesk&#39;">autodesk</span> <span class="post-tag tag-link-citrix" rel="tag" title="see questions tagged &#39;citrix&#39;">citrix</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '17, 01:06</strong></p><img src="https://secure.gravatar.com/avatar/55af0207b10dbbd15ebb9f852822a294?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ciag&#39;s gravatar image" /><p><span>Ciag</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ciag has no accepted answers">0%</span></p></div></div><div id="comments-container-58879" class="comments-container"></div><div id="comment-tools-58879" class="comment-tools"></div><div class="clear"></div><div id="comment-58879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

