+++
type = "question"
title = "why dfilter_apply_edt() returning false every time."
description = '''so I am trying to dissect diameter packets using wireshark library, when i apply filter &#x27;diameter&#x27;, and then call dfilter_apply_edt , it always returning false. what could be the reason behind this. thanks.'''
date = "2014-01-15T00:29:00Z"
lastmod = "2014-01-15T00:29:00Z"
weight = 28899
keywords = [ "code", "libwireshark", "dissection", "pcap", "diameter" ]
aliases = [ "/questions/28899" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [why dfilter\_apply\_edt() returning false every time.](/questions/28899/why-dfilter_apply_edt-returning-false-every-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28899-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>so I am trying to dissect diameter packets using wireshark library,</p><p>when i apply filter 'diameter', and then call dfilter_apply_edt , it always returning false.</p><p>what could be the reason behind this.</p><p>thanks.</p></div><div id="question-tags" class="tags-container tags">code libwireshark dissection pcap diameter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '14, 00:29</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p>Sanny_D<br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div></div><div id="comments-container-28899" class="comments-container"><span id="28904"></span><div id="comment-28904" class="comment"><div id="post-28904-score" class="comment-score"></div><div class="comment-text"><p>Perhaps the packets are not recognised as Diameter? what's in the frame you are trying to dissect? a full frame starting from ethernet? What happens if you let Wireshark dissect the frame?</p></div><div id="comment-28904-info" class="comment-info"><span class="comment-age">(15 Jan '14, 04:05)</span> Anders ♦</div></div><span id="28905"></span><div id="comment-28905" class="comment"><div id="post-28905-score" class="comment-score"></div><div class="comment-text"><p>actually, i was trying to dissect output of 'ngrep pcap dump', but it does not support packet reassembly, i guess that is why it is not dissecting ?</p></div><div id="comment-28905-info" class="comment-info"><span class="comment-age">(15 Jan '14, 04:14)</span> Sanny_D</div></div><span id="28908"></span><div id="comment-28908" class="comment"><div id="post-28908-score" class="comment-score"></div><div class="comment-text"><p>it depends on the output format of ngrep. What are the options you were using for ngrep?</p></div><div id="comment-28908-info" class="comment-info"><span class="comment-age">(15 Jan '14, 06:18)</span> Kurt Knochner ♦</div></div><span id="28945"></span><div id="comment-28945" class="comment"><div id="post-28945-score" class="comment-score"></div><div class="comment-text"><p>ngrep ".;5233184391;9999" -I /tmp/pcapd/santo.pcap -O sip:incredible_2.pcap -q -t -w 2&gt;&amp;1 &gt;&gt;/dev/null</p><p>".;5233184391;9999" is the matching expression. then i am trying to dissect the sip:incredible_2.pcap file, but surprisingly wireshark dissect it fine.</p></div><div id="comment-28945-info" class="comment-info"><span class="comment-age">(15 Jan '14, 21:29)</span> Sanny_D</div></div><span id="28953"></span><div id="comment-28953" class="comment"><div id="post-28953-score" class="comment-score"></div><div class="comment-text"><p>Which protocols do you see in Wireshark?</p></div><div id="comment-28953-info" class="comment-info"><span class="comment-age">(16 Jan '14, 01:07)</span> Kurt Knochner ♦</div></div><span id="28955"></span><div id="comment-28955" class="comment not_top_scorer"><div id="post-28955-score" class="comment-score"></div><div class="comment-text"><p>protocols ins frame-&gt;eth:ip:sctp:diameter:diameter</p></div><div id="comment-28955-info" class="comment-info"><span class="comment-age">(16 Jan '14, 02:00)</span> Sanny_D</div></div><span id="28958"></span><div id="comment-28958" class="comment not_top_scorer"><div id="post-28958-score" class="comment-score"></div><div class="comment-text"><p>well, then something in your code could be wrong. Is it available online?</p></div><div id="comment-28958-info" class="comment-info"><span class="comment-age">(16 Jan '14, 02:22)</span> Kurt Knochner ♦</div></div><span id="28982"></span><div id="comment-28982" class="comment not_top_scorer"><div id="post-28982-score" class="comment-score"></div><div class="comment-text"><p>its here, <a href="http://snipt.org/BRjj5">http://snipt.org/BRjj5</a></p><p>printf("\nfailed_passed\n");fflush(stdout); executed for some messages.</p></div><div id="comment-28982-info" class="comment-info"><span class="comment-age">(16 Jan '14, 21:50)</span> Sanny_D</div></div></div><div id="comment-tools-28899" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-28899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

