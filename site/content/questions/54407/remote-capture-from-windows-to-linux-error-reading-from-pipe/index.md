+++
type = "question"
title = "Remote capture from Windows to Linux - &#x27;Error reading from pipe&#x27;"
description = '''I&#x27;m trying to capture using tshark on a remote Debian system. My local machine is Windows 10, running Wireshark 2.0.5.  I&#x27;m using plink to setup the connection with the remote system, with the following command:  plink -l username 192.168.10.10 &quot;tshark -i eth0 -w -&quot; | wireshark.exe -k -i - The conne...'''
date = "2016-07-28T10:09:00Z"
lastmod = "2016-07-28T10:09:00Z"
weight = 54407
keywords = [ "windows", "remote-capture", "pipe", "linux" ]
aliases = [ "/questions/54407" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Remote capture from Windows to Linux - 'Error reading from pipe'](/questions/54407/remote-capture-from-windows-to-linux-error-reading-from-pipe)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54407-score" class="post-score" title="current number of votes">0</div><span id="post-54407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to capture using tshark on a remote Debian system. My local machine is Windows 10, running Wireshark 2.0.5.</p><p>I'm using plink to setup the connection with the remote system, with the following command: plink -l username 192.168.10.10 "tshark -i eth0 -w -" | wireshark.exe -k -i -</p><p>The connection gets established, the terminal prints "Capturing on 'eth0'", and Wireshark opens on my local system.</p><p>After Wireshark finishes loading, an error pops up and says Error reading from pipe: The operation completed successfully. (error 0)</p><p>The user I'm logging in to the remote system as can run tshark. When I SSH in to the remote system and run tshark within the shell on that system, everything looks fine.</p><p>I'm not sure where the pipe is failing. Any suggestions?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-remote-capture" rel="tag" title="see questions tagged &#39;remote-capture&#39;">remote-capture</span> <span class="post-tag tag-link-pipe" rel="tag" title="see questions tagged &#39;pipe&#39;">pipe</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '16, 10:09</strong></p><img src="https://secure.gravatar.com/avatar/727be926d93451d403f0b249d0315b0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunnyside&#39;s gravatar image" /><p><span>sunnyside</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunnyside has no accepted answers">0%</span></p></div></div><div id="comments-container-54407" class="comments-container"></div><div id="comment-tools-54407" class="comment-tools"></div><div class="clear"></div><div id="comment-54407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

