+++
type = "question"
title = "measuring/graphing DHCP response times"
description = '''Hi, We have been tracking through issues with our dhcp server and we need to measure dhcp response times, but all my google-fu seems to be failing me... I&#x27;ve looked though the wireshark bootp/dhcp sections and nothing seems to specifically measure dhcp response times but you&#x27;d think surely it&#x27;s some...'''
date = "2016-06-30T19:26:00Z"
lastmod = "2016-06-30T19:26:00Z"
weight = 53757
keywords = [ "dhcp" ]
aliases = [ "/questions/53757" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [measuring/graphing DHCP response times](/questions/53757/measuringgraphing-dhcp-response-times)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53757-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We have been tracking through issues with our dhcp server and we need to measure dhcp response times, but all my google-fu seems to be failing me...</p><p>I've looked though the wireshark bootp/dhcp sections and nothing seems to specifically measure dhcp response times but you'd think surely it's something not uncommon to want to perform. Ideally I'd want to graph it as part of an IO graph.</p><p>Has anyone done this? Is there a wireshark lua plugin I can add?</p><p>Thanks,</p><p>Glen.</p></div><div id="question-tags" class="tags-container tags">dhcp</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '16, 19:26</strong></p><img src="https://secure.gravatar.com/avatar/f7e5d56de2cfeed8699b6a3be21bcbcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="glenp42&#39;s gravatar image" /><p>glenp42<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="glenp42 has no accepted answers">0%</span></p></div></div><div id="comments-container-53757" class="comments-container"><span id="53765"></span><div id="comment-53765" class="comment"><div id="post-53765-score" class="comment-score"></div><div class="comment-text"><p>I can't help you directly, but this post from years ago is basically the same request:</p><p><a href="https://ask.wireshark.org/questions/241/tcp-and-others-response-times">https://ask.wireshark.org/questions/241/tcp-and-others-response-times</a></p><p>Someone with Lua expertise can probably help you to do it within Wireshark, but here is another link where someone developed a tool in Perl to do it:</p><p><a href="http://indcontrolproto.blogspot.com/search?updated-min=2013-01-01T00:00:00-08:00&amp;updated-max=2014-01-01T00:00:00-08:00&amp;max-results=3">http://indcontrolproto.blogspot.com/search?updated-min=2013-01-01T00:00:00-08:00&amp;updated-max=2014-01-01T00:00:00-08:00&amp;max-results=3</a></p><p>I know this method and it uses Excel or another graphing package to create the charts. Not exactly what you want, and this execution is for ModbusTCP but it is a view of how others have solved your same issue starting from a packet capture.</p></div><div id="comment-53765-info" class="comment-info"><span class="comment-age">(01 Jul '16, 03:25)</span> Bob Jones</div></div><span id="53769"></span><div id="comment-53769" class="comment"><div id="post-53769-score" class="comment-score"></div><div class="comment-text"><p>Another hint, rather than an Answer, would be to use <a href="https://wiki.wireshark.org/Mate/Manual">MATE</a> to group the DHCP requests (discovers etc.) with corresponding responses (offers, acknowledges etc.) and to let the graph show the MATE GoP durations. As compared to @Bob Jones' suggestion, mine requires to learn a quite niche feature of Wireshark, but it allows the whole solution including drawing the graph to remain within Wireshark.</p></div><div id="comment-53769-info" class="comment-info"><span class="comment-age">(01 Jul '16, 07:27)</span> sindy</div></div></div><div id="comment-tools-53757" class="comment-tools"></div><div class="clear"></div><div id="comment-53757-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

