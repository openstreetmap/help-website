+++
type = "question"
title = "Reasonable/acceptable use of OUI page from wireshark.org"
description = '''I note that the page at https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=manuf is released under the GPL. We have an operational need to keep a list of OUI&#x27;s reasonably up-to-date, and have found that getting such a list from IEEE&#x27;s site is so slow and unreliable that our upda...'''
date = "2015-10-30T06:03:00Z"
lastmod = "2015-10-30T12:42:00Z"
weight = 47090
keywords = [ "oui", "use", "list", "acceptable" ]
aliases = [ "/questions/47090" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Reasonable/acceptable use of OUI page from wireshark.org](/questions/47090/reasonableacceptable-use-of-oui-page-from-wiresharkorg)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47090-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I note that the page at</p><p><a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=manuf">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=manuf</a></p><p>is released under the GPL. We have an operational need to keep a list of OUI's reasonably up-to-date, and have found that getting such a list from IEEE's site is so slow and unreliable that our update process fails frequently.</p><p>Is it a reasonable proposition to download from the URL above once a day? Once a week? We have no desire to abuse the resource, and would like some guidance as to what makes sense and is acceptable.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">oui use list acceptable</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '15, 06:03</strong></p><img src="https://secure.gravatar.com/avatar/9eac17f193931b0cd7e5957d1ac6dbff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gl89-cornell&#39;s gravatar image" /><p>gl89-cornell<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gl89-cornell has no accepted answers">0%</span></p></div></div><div id="comments-container-47090" class="comments-container"></div><div id="comment-tools-47090" class="comment-tools"></div><div class="clear"></div><div id="comment-47090-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47096"></span>

<div id="answer-container-47096" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47096-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it a reasonable proposition to download from the URL above once a day?</p></blockquote><p>reasonable in terms of what?</p><p>I guess the frequency is up to you to decide. This file won't change on a daily basis.</p><blockquote><p>We have no desire to abuse the resource, and would like some guidance as to what makes sense and is acceptable.</p></blockquote><p>I'd say: Do whatever is <strong>reasonable</strong> for you. Wireshark is an open source tool and you can use whatever part of it you might need, as long as you ahdere to the GPL (Wiresharks license).</p><p>BTW: did you see the comment in the manuf file?</p><pre><code># The data below has been assembled from the following sources:
#
# The IEEE public OUI listing available from:
# &lt;http://standards.ieee.org/develop/regauth/oui/oui.txt&gt;
# &lt;http://standards.ieee.org/develop/regauth/iab/iab.txt&gt;
# &lt;http://standards.ieee.org/develop/regauth/oui36/oui36.txt&gt;
#
# Michael Patton&#39;s &quot;Ethernet Codes Master Page&quot; available from:
# &lt;http://www.cavebear.com/archive/cavebear/Ethernet/Ethernet.txt&gt;
#</code></pre><p>Maybe it would be more <strong>reasonable</strong> for you to get the files directly from those servers and assemble them yourself. Just for the situation where code.wireshark.org might be down for some reasons.</p><pre><code># You can get the latest version of this file from
# https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=manuf;hb=HEAD</code></pre><p>If you want the latest file, you should use that link.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '15, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-47096" class="comments-container"></div><div id="comment-tools-47096" class="comment-tools"></div><div class="clear"></div><div id="comment-47096-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

