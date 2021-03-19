+++
type = "question"
title = "error when running wireshark on Ubuntu as non root user"
description = '''hi all, When I issue &quot;sudo wireshark -i eth0&quot; on my ubuntu 12.04, a error window occur said &quot;Lua: Error during loading: [string &quot;/usr/share/wireshark/init.lua&quot;]: 45:dofile has been disabled.&quot; What does it mean and how to resolve this issue? thanks!'''
date = "2013-03-20T06:26:00Z"
lastmod = "2013-03-20T09:17:00Z"
weight = 19675
keywords = [ "privileges", "root", "setcap", "linux" ]
aliases = [ "/questions/19675" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [error when running wireshark on Ubuntu as non root user](/questions/19675/error-when-running-wireshark-on-ubuntu-as-non-root-user)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19675-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi all,</p><p>When I issue <strong>"sudo wireshark -i eth0" on my ubuntu 12.04, a error window occur said "Lua: Error during loading: [string "/usr/share/wireshark/init.lua"]: 45:dofile has been disabled."</strong></p><p>What does it mean and how to resolve this issue?</p><p>thanks!</p></div><div id="question-tags" class="tags-container tags">privileges root setcap linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '13, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p>SteveZhou<br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Sep '13, 04:58</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-19675" class="comments-container"></div><div id="comment-tools-19675" class="comment-tools"></div><div class="clear"></div><div id="comment-19675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19684"></span>

<div id="answer-container-19684" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19684-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What does it mean and how to resolve this issue?</p></blockquote><p>it means, you shall <strong>not run</strong> Wireshark <strong>as root</strong> (for security reasons). See here:</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/CapturePrivileges</code><br />
<code>http://wiki.wireshark.org/Development/PrivilegeSeparation</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '13, 09:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-19684" class="comments-container"><span id="24502"></span><div id="comment-24502" class="comment"><div id="post-24502-score" class="comment-score"></div><div class="comment-text"><p>So with the default installation, I can capture packets as root? I need to reinstall wireshark to allow non-root users to capture packets? But I didn't find a installation process for this.</p></div><div id="comment-24502-info" class="comment-info"><span class="comment-age">(09 Sep '13, 23:06)</span> SteveZhou</div></div><span id="24503"></span><div id="comment-24503" class="comment"><div id="post-24503-score" class="comment-score"></div><div class="comment-text"><p>What is you OS?</p></div><div id="comment-24503-info" class="comment-info"><span class="comment-age">(09 Sep '13, 23:27)</span> Kurt Knochner ♦</div></div><span id="24516"></span><div id="comment-24516" class="comment"><div id="post-24516-score" class="comment-score"></div><div class="comment-text"><p>From the question: Ubuntu 12.04</p><p>So the user should follow the Debian install guidelines <a href="http://anonscm.debian.org/viewvc/collab-maint/ext-maint/wireshark/trunk/debian/README.Debian?view=markup">here</a></p></div><div id="comment-24516-info" class="comment-info"><span class="comment-age">(10 Sep '13, 02:07)</span> grahamb ♦</div></div><span id="24519"></span><div id="comment-24519" class="comment"><div id="post-24519-score" class="comment-score"></div><div class="comment-text"><p>ah, it's the same user. I did not check, as my answer was so old :-))</p></div><div id="comment-24519-info" class="comment-info"><span class="comment-age">(10 Sep '13, 03:55)</span> Kurt Knochner ♦</div></div><span id="24520"></span><div id="comment-24520" class="comment"><div id="post-24520-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I need to reinstall wireshark to allow non-root users to capture packets?</p></blockquote><p>No. Just run the following command (as documented in the link I posted in my answer):</p><blockquote><p>sudo setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap</p></blockquote><p>Then run Wireshark as a non root user and you should see the interfaces.</p><p>The same is true for dumpcap.</p><blockquote><p>dumpcap -D -M</p></blockquote><p>will show interfaces, if run as non root user, <strong>only after</strong> the setcap command.</p></div><div id="comment-24520-info" class="comment-info"><span class="comment-age">(10 Sep '13, 04:08)</span> Kurt Knochner ♦</div></div><span id="24636"></span><div id="comment-24636" class="comment not_top_scorer"><div id="post-24636-score" class="comment-score"></div><div class="comment-text"><p>really helpful, it's working! thank you so much!</p></div><div id="comment-24636-info" class="comment-info"><span class="comment-age">(13 Sep '13, 02:55)</span> SteveZhou</div></div></div><div id="comment-tools-19684" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-19684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

