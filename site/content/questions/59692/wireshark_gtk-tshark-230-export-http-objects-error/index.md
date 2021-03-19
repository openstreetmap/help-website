+++
type = "question"
title = "wireshark_gtk / tshark 2.3.0 export http objects error"
description = '''Hi,  I build wireshark from git yesterday. When I try to export http objects by command tshark -r &quot;file.pcapng&quot; --export-objects &quot;http,folder&quot; -Q  I get this error (process:18690): GLib-CRITICAL **: g_path_get_basename: assertion &#x27;file_name != NULL&#x27; failed  Export object from gui interface wireshark...'''
date = "2017-02-26T06:16:00Z"
lastmod = "2017-02-27T09:15:00Z"
weight = 59692
keywords = [ "glib", "objects", "export", "tshark" ]
aliases = [ "/questions/59692" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [wireshark\_gtk / tshark 2.3.0 export http objects error](/questions/59692/wireshark_gtk-tshark-230-export-http-objects-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59692-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I build wireshark from git yesterday. When I try to export http objects by command</p><pre><code>tshark -r &quot;file.pcapng&quot; --export-objects &quot;http,folder&quot; -Q</code></pre><p>I get this error</p><pre><code>(process:18690): GLib-CRITICAL **: g_path_get_basename: assertion &#39;file_name != NULL&#39; failed</code></pre><p>Export object from gui interface wireshark_gtk have this issue as well.</p><p>My environment: GLib version v2.42.1, GTK+ v3.14.5, Raspbian Jessie.</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags">glib objects export tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '17, 06:16</strong></p><img src="https://secure.gravatar.com/avatar/92c67351c97fa19bb5dbe0023841a0b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zacklin&#39;s gravatar image" /><p>zacklin<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zacklin has no accepted answers">0%</span></p></div></div><div id="comments-container-59692" class="comments-container"></div><div id="comment-tools-59692" class="comment-tools"></div><div class="clear"></div><div id="comment-59692-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59713"></span>

<div id="answer-container-59713" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59713-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It seems that this problem was reported as <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13441">bug 13441</a> and has now been fixed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '17, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59713" class="comments-container"><span id="59714"></span><div id="comment-59714" class="comment"><div id="post-59714-score" class="comment-score"></div><div class="comment-text"><p>Yep, actually it was me XD.</p></div><div id="comment-59714-info" class="comment-info"><span class="comment-age">(27 Feb '17, 10:44)</span> zacklin</div></div></div><div id="comment-tools-59713" class="comment-tools"></div><div class="clear"></div><div id="comment-59713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

