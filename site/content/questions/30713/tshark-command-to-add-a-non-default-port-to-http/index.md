+++
type = "question"
title = "tshark command to add a non-default port to HTTP"
description = '''i need to edit the preferences (i.e preferences-&amp;gt;protocols-&amp;gt;http in wireshark) to include a non default port in HTTP ports.What is the tshark command to change this preference.'''
date = "2014-03-12T02:47:00Z"
lastmod = "2014-03-12T03:07:00Z"
weight = 30713
keywords = [ "tshark" ]
aliases = [ "/questions/30713" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [tshark command to add a non-default port to HTTP](/questions/30713/tshark-command-to-add-a-non-default-port-to-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30713-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i need to edit the preferences (i.e preferences-&gt;protocols-&gt;http in wireshark) to include a non default port in HTTP ports.What is the tshark command to change this preference.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '14, 02:47</strong></p><img src="https://secure.gravatar.com/avatar/52aab48029e3c1ba2f253a47b3ed4145?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vmoar&#39;s gravatar image" /><p>vmoar<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vmoar has no accepted answers">0%</span></p></div></div><div id="comments-container-30713" class="comments-container"></div><div id="comment-tools-30713" class="comment-tools"></div><div class="clear"></div><div id="comment-30713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30715"></span>

<div id="answer-container-30715" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30715-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a>:</p><pre><code>-o &lt;preference&gt;:&lt;value&gt;    
    Set a preference value, overriding the default value and any value read from a preference file. The argument to the option is a string of the form prefname:value, where prefname is the name of the preference (which is the same name that would appear in the preference file), and value is the value to which it should be set.</code></pre><p>So, in your case you would use <code>-o http.tcp.port:80,8080,nnnn</code> where nnnn is your required port and you also list all other required http ports as the preference setting is a "range.".</p><p>Tip: The preference "name" is shown as a tooltip in the GUI when you hover over it (for protocol prefs).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '14, 03:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-30715" class="comments-container"><span id="30716"></span><div id="comment-30716" class="comment"><div id="post-30716-score" class="comment-score"></div><div class="comment-text"><p>Thank you.Its working:)</p></div><div id="comment-30716-info" class="comment-info"><span class="comment-age">(12 Mar '14, 03:17)</span> vmoar</div></div><span id="30717"></span><div id="comment-30717" class="comment"><div id="post-30717-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-30717-info" class="comment-info"><span class="comment-age">(12 Mar '14, 03:27)</span> grahamb ♦</div></div><span id="30718"></span><div id="comment-30718" class="comment"><div id="post-30718-score" class="comment-score"></div><div class="comment-text"><p>hi, if i need to change something that uses udp or any other protocol available in preferences(other than http) what would be the syntax</p></div><div id="comment-30718-info" class="comment-info"><span class="comment-age">(12 Mar '14, 03:36)</span> vmoar</div></div><span id="30719"></span><div id="comment-30719" class="comment"><div id="post-30719-score" class="comment-score"></div><div class="comment-text"><p>Very similar, just find the preference name and tack it on as another -o option, e.g. for DNS, use <code>-o dns.udp.ports:nnnn</code>.</p><p>You can also open the preference file in a text editor and scan though it looking for preference names.</p></div><div id="comment-30719-info" class="comment-info"><span class="comment-age">(12 Mar '14, 03:50)</span> grahamb ♦</div></div><span id="30720"></span><div id="comment-30720" class="comment"><div id="post-30720-score" class="comment-score"></div><div class="comment-text"><p>thank you.</p></div><div id="comment-30720-info" class="comment-info"><span class="comment-age">(12 Mar '14, 03:58)</span> vmoar</div></div><span id="30721"></span><div id="comment-30721" class="comment not_top_scorer"><div id="post-30721-score" class="comment-score"></div><div class="comment-text"><p>hi, is it possible to extract or view the value of these prefernces..i.e. the port numbers.</p></div><div id="comment-30721-info" class="comment-info"><span class="comment-age">(12 Mar '14, 04:20)</span> vmoar</div></div><span id="30723"></span><div id="comment-30723" class="comment not_top_scorer"><div id="post-30723-score" class="comment-score"></div><div class="comment-text"><p>We're on a roll here, they're all in the preferences file, <code>-G currentprefs</code> dumps them out.</p></div><div id="comment-30723-info" class="comment-info"><span class="comment-age">(12 Mar '14, 04:35)</span> grahamb ♦</div></div></div><div id="comment-tools-30715" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-30715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

