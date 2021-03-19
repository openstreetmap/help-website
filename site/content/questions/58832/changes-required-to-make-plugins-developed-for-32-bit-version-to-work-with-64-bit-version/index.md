+++
type = "question"
title = "Changes required to make plugins developed for 32-bit version to work with 64-bit version?"
description = '''I have developed plugins for Wireshark 2.2.3 32-bit version. But when I use the same .dll files in the 64-bit version of Wireshark-2.2.3 it doesn&#x27;t work. Please help me with this.'''
date = "2017-01-17T05:17:00Z"
lastmod = "2017-01-17T05:17:00Z"
weight = 58832
keywords = [ "libwireshark", "64bit", "plugins", "version", "wireshark" ]
aliases = [ "/questions/58832" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Changes required to make plugins developed for 32-bit version to work with 64-bit version?](/questions/58832/changes-required-to-make-plugins-developed-for-32-bit-version-to-work-with-64-bit-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58832-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have developed plugins for Wireshark 2.2.3 32-bit version. But when I use the same .dll files in the 64-bit version of Wireshark-2.2.3 it doesn't work. Please help me with this.</p></div><div id="question-tags" class="tags-container tags">libwireshark 64bit plugins version wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '17, 05:17</strong></p><img src="https://secure.gravatar.com/avatar/54b13e716c5802540b3b28701372e876?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chirag&#39;s gravatar image" /><p>chirag<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chirag has no accepted answers">0%</span></p></div></div><div id="comments-container-58832" class="comments-container"><span id="58833"></span><div id="comment-58833" class="comment"><div id="post-58833-score" class="comment-score"></div><div class="comment-text"><p>Recompile the code?</p></div><div id="comment-58833-info" class="comment-info"><span class="comment-age">(17 Jan '17, 05:36)</span> Jaap ♦</div></div><span id="58835"></span><div id="comment-58835" class="comment"><div id="post-58835-score" class="comment-score"></div><div class="comment-text"><p>Are there any additional changes to the code required?, other than recompiling?</p></div><div id="comment-58835-info" class="comment-info"><span class="comment-age">(17 Jan '17, 05:51)</span> chirag</div></div><span id="58836"></span><div id="comment-58836" class="comment"><div id="post-58836-score" class="comment-score"></div><div class="comment-text"><p>If you programmed it clean there should not be. The compilation will tell you.</p></div><div id="comment-58836-info" class="comment-info"><span class="comment-age">(17 Jan '17, 06:24)</span> Jaap ♦</div></div><span id="58853"></span><div id="comment-58853" class="comment"><div id="post-58853-score" class="comment-score"></div><div class="comment-text"><p>Don't assume that a pointer will fit into an <code>int</code> or an <code>unsigned int</code> (or any types that are equivalent, such as <code>gint</code> or <code>guint</code>).</p><p>Don't assume it will fit into a <code>long</code> or an <code>unsigned long</code> (or any types that are equivalent, such as <code>glong</code> or <code>gulong</code>), either. It won't, on Windows.</p></div><div id="comment-58853-info" class="comment-info"><span class="comment-age">(17 Jan '17, 13:18)</span> Guy Harris ♦♦</div></div><span id="58855"></span><div id="comment-58855" class="comment"><div id="post-58855-score" class="comment-score"></div><div class="comment-text"><p>... and all other advice as found in <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=doc/README.developer;hb=HEAD">README.developer</a></p></div><div id="comment-58855-info" class="comment-info"><span class="comment-age">(17 Jan '17, 13:55)</span> Jaap ♦</div></div><span id="58864"></span><div id="comment-58864" class="comment not_top_scorer"><div id="post-58864-score" class="comment-score"></div><div class="comment-text"><p>Thanks Guy and Jaap for the comments. I will compile and make changes accordingly.</p></div><div id="comment-58864-info" class="comment-info"><span class="comment-age">(17 Jan '17, 22:44)</span> chirag</div></div></div><div id="comment-tools-58832" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-58832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

