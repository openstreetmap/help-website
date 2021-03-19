+++
type = "question"
title = "tshark conversation statistic not resolving hostnames"
description = '''Executing the -z conv,ip command does not display the hostnames (like in wireshark). This happens on Fedora 17 and Windows 7. I execute the command, and after a bit of traffic was monitored, I stop tshark with Ctrl-C. After this the conversation table is printed. Linux:  command: tshark -i 1 -N n -f...'''
date = "2013-01-16T12:33:00Z"
lastmod = "2013-02-01T06:39:00Z"
weight = 17724
keywords = [ "conversation", "hostname", "tshark", "dns", "ip" ]
aliases = [ "/questions/17724" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark conversation statistic not resolving hostnames](/questions/17724/tshark-conversation-statistic-not-resolving-hostnames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17724-score" class="post-score" title="current number of votes">0</div><span id="post-17724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Executing the <code>-z conv,ip</code> command does not display the hostnames (like in wireshark). This happens on Fedora 17 and Windows 7. I execute the command, and after a bit of traffic was monitored, I stop tshark with Ctrl-C. After this the conversation table is printed.</p><p><strong>Linux:</strong></p><ul><li>command: <code>tshark -i 1 -N n -f "tcp or udp" -z conv,ip</code></li><li>OS: Fedora 17 x86</li><li>tshark version: 1.6.12</li><li>Solutions tried:</li><li>Ommiting <code>-N</code></li><li>Using <code>-N C</code></li></ul><p><strong>Windows:</strong></p><ul><li>command: <code>tshark -i 2 -f "tcp or udp" -z conv,ip</code></li><li>OS: Windows 7 x64</li><li>tshark version: 1.8.4</li><li>Solutions tried:</li><li>Ommiting <code>-N</code></li><li>Using <code>-N C</code></li><li>Using <code>-N n</code> causes tshark error out: (tshark.exe:9692): CaptureChild-WARNING **: signal_pipe_capquit_to_child: 4 header: error Invalid argument</li></ul><p><strong>How do I make tshark -z conv,ip display resolve hostnames?</strong></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span> <span class="post-tag tag-link-hostname" rel="tag" title="see questions tagged &#39;hostname&#39;">hostname</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '13, 12:33</strong></p><img src="https://secure.gravatar.com/avatar/a43ad570008569dcc3dbb8f36f1ee5af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Daniel%20K&#39;s gravatar image" /><p><span>Daniel K</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Daniel K has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Jan '13, 12:35</strong> </span></p></div></div><div id="comments-container-17724" class="comments-container"></div><div id="comment-tools-17724" class="comment-tools"></div><div class="clear"></div><div id="comment-17724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18224"></span>

<div id="answer-container-18224" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18224-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18224-score" class="post-score" title="current number of votes">0</div><span id="post-18224-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Daniel K has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Having tshark showing resolved hostnames in the conversation statistic does not appear possible.</p><p>An alternative is to execute the following commands:</p><pre><code>tshark -i 1 -N n -e ip.host -E separator=, -f &quot;tcp or udp&quot; -l &gt; tshark_buffer

sort -u tshark_buffer -o tshark_buffer</code></pre><p>Where the first command dumps packet information into a file named <code>tshark_buffer</code>, and the second command eliminates duplicate entries. The packet information is stored in the form <code>host1,host2</code> on each line. However, the duplicate elimination will not catch entries with the hosts reversed (i.e. <code>host2,host1</code>).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '13, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/a43ad570008569dcc3dbb8f36f1ee5af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Daniel%20K&#39;s gravatar image" /><p><span>Daniel K</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Daniel K has one accepted answer">100%</span></p></div></div><div id="comments-container-18224" class="comments-container"></div><div id="comment-tools-18224" class="comment-tools"></div><div class="clear"></div><div id="comment-18224-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

