+++
type = "question"
title = "Capture File Anonymization"
description = '''Are there any good capture Anonymization you would recommend ?'''
date = "2012-11-27T23:39:00Z"
lastmod = "2012-11-28T02:49:00Z"
weight = 16367
keywords = [ "anonimization", "scrubbing" ]
aliases = [ "/questions/16367" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Capture File Anonymization](/questions/16367/capture-file-anonymization)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16367-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Are there any good capture Anonymization you would recommend ?</p></div><div id="question-tags" class="tags-container tags">anonimization scrubbing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '12, 23:39</strong></p><img src="https://secure.gravatar.com/avatar/22baebd906c29ccfcb5b2aeb350b22fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bart80&#39;s gravatar image" /><p>bart80<br />
<span class="score" title="11 reputation points">11</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bart80 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted 27 Nov '12, 23:45</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-16367" class="comments-container"><span id="16369"></span><div id="comment-16369" class="comment"><div id="post-16369-score" class="comment-score"></div><div class="comment-text"><p>I converted your "comment" to a new "question" as more people might be interested and this way the answers can be found more easily.</p></div><div id="comment-16369-info" class="comment-info"><span class="comment-age">(27 Nov '12, 23:46)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-16367" class="comment-tools"></div><div class="clear"></div><div id="comment-16367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16373"></span>

<div id="answer-container-16373" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16373-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>I did a talk about that topic at Sharkfest 2011, for which you can find the presentations here (A-11): <a href="http://sharkfest.wireshark.org/sharkfest.11/index.html">http://sharkfest.wireshark.org/sharkfest.11/index.html</a></p><p>Since all the tools I examined do not work with pcapng files, and are mostly for packet replay preparation, I started creating a new tool that will hopefully be ready to present at Sharkfest 2013 :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Nov '12, 02:49</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-16373" class="comments-container"><span id="16377"></span><div id="comment-16377" class="comment"><div id="post-16377-score" class="comment-score"></div><div class="comment-text"><p>is just the fact that they cannot read pcapng or do you plan to use pcapng to store information about the anonymization process (what has been changed)?</p><p>BTW: Is that anontracer VM available for download?</p></div><div id="comment-16377-info" class="comment-info"><span class="comment-age">(28 Nov '12, 04:21)</span> Kurt Knochner ♦</div></div><span id="16378"></span><div id="comment-16378" class="comment"><div id="post-16378-score" class="comment-score"></div><div class="comment-text"><p>At the time of the preparation of the talk they could not read pcapng; I haven't checked if they added support for it in the meantime tbh.</p><p>The plan is that my tool will be able to anonymize every aspect of the pcapng file, including name resolution header blocks etc. There will be still the almost impossible task of anonymizing layers beyond layer 4, but I'll see what I can do.</p><p>I can provide a download link for the VM, yes. It can be found here: <a href="http://www.bongertz.com/download/anontracer.zip">http://www.bongertz.com/download/anontracer.zip</a></p></div><div id="comment-16378-info" class="comment-info"><span class="comment-age">(28 Nov '12, 04:51)</span> Jasper ♦♦</div></div><span id="16380"></span><div id="comment-16380" class="comment"><div id="post-16380-score" class="comment-score"></div><div class="comment-text"><p>Thank you!</p></div><div id="comment-16380-info" class="comment-info"><span class="comment-age">(28 Nov '12, 04:55)</span> Kurt Knochner ♦</div></div><span id="16405"></span><div id="comment-16405" class="comment"><div id="post-16405-score" class="comment-score"></div><div class="comment-text"><p>Tools that use libpcap can read some pcap-ng files if they're using libpcap 1.1.0 or later; they can't read files that have more than one link-layer header type or snapshot length (multiple interfaces are OK as long as they all have the same link-layer header type and snapshot length).</p><p>However, you can't <em>write</em> pcap-ng files with current versions of standard libpcap, so that probably won't help for anonymizing tools.</p></div><div id="comment-16405-info" class="comment-info"><span class="comment-age">(28 Nov '12, 14:54)</span> Guy Harris ♦♦</div></div><span id="16406"></span><div id="comment-16406" class="comment"><div id="post-16406-score" class="comment-score"></div><div class="comment-text"><p>Regarding pcap-ng... I'm not using libpcap or any other existing library out there, it is all written from scratch and mostly working already. So much to code... so little time :-)</p></div><div id="comment-16406-info" class="comment-info"><span class="comment-age">(28 Nov '12, 16:14)</span> Jasper ♦♦</div></div></div><div id="comment-tools-16373" class="comment-tools"></div><div class="clear"></div><div id="comment-16373-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

