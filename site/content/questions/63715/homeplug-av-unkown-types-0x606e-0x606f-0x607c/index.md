+++
type = "question"
title = "HomePlug AV Unkown Types 0x606e , 0x606f, 0X607c ..."
description = '''Is there anyway I can add names to these fields in the types or modify the info column object of the homeplug av protocol by accessing these fields?  I want to know if it is possible to write a post dissector which only modifies the unknown types and other required fields by keeping all other fields...'''
date = "2017-10-06T12:32:00Z"
lastmod = "2017-10-08T01:38:00Z"
weight = 63715
keywords = [ "homeplug-av", "unkown" ]
aliases = [ "/questions/63715" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [HomePlug AV Unkown Types 0x606e , 0x606f, 0X607c ...](/questions/63715/homeplug-av-unkown-types-0x606e-0x606f-0x607c)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63715-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there anyway I can add names to these fields in the types or modify the info column object of the homeplug av protocol by accessing these fields?</p><p>I want to know if it is possible to write a post dissector which only modifies the unknown types and other required fields by keeping all other fields of homeplug AV.</p></div><div id="question-tags" class="tags-container tags">homeplug-av unkown</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '17, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/bf8a8cb9da533bbc7b744c1ba0003458?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="golthitatun&#39;s gravatar image" /><p>golthitatun<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="golthitatun has no accepted answers">0%</span></p></div></div><div id="comments-container-63715" class="comments-container"></div><div id="comment-tools-63715" class="comment-tools"></div><div class="clear"></div><div id="comment-63715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63734"></span>

<div id="answer-container-63734" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63734-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A <strong>post</strong>-dissector cannot modify any fields of the dissection tree already contributed by standard dissectors, but it can append text to the <code>pinfo.cols.info</code> (and most likely even rewrite it completely).</p><p>Unlike some other dissectors, the HomePlug-AV one does not seem to be plugin-ready in terms that it would use a dissector table with <code>homeplug_av.mmhdr.mmtype</code> values as keys to refer to sub-dissectors.</p><p>However, if just appending/replacing text in the info column is not sufficient for you and you don't want to touch the existing homeplug_av dissector, you may create your own dissector, handling only your additional mmtypes, and invoke the standard dissector for all the other ones. This approach requires that you duplicate the header parsing part of the standard dissector (MAC Management Header, Vendor MME) but that's not a big deal. I've seen this approach to be called "chained dissectors".</p><p>To insert your own dissector in front of the standard one:</p><ul><li>in the initialization part of it, you would copy the link to the standard dissector from the <code>ethertype</code> dissection table into your dissector's local variable and replace it with a link to your own dissector's executive part</li><li>the executive part of your dissector would first check the mmtype, and if it wouldn't be one of those it can handle, it would call the standard one stored in the variable, forwarding all its input parameters unchanged and returning the return value unchanged as well.</li></ul><p>In your own dissector you can use exactly the same field names which the standard dissector uses, so the display filters on fields like <code>homeplug_av.vendor.oui</code> or <code>homeplug_av.mmhdr.mmver</code> will work also on frames dissected by your custom dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '17, 01:38</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Oct '17, 11:00</p></div></div><div id="comments-container-63734" class="comments-container"><span id="63761"></span><div id="comment-63761" class="comment"><div id="post-63761-score" class="comment-score"></div><div class="comment-text"><p>Hi thank you, I am new to writing dissectors, can you please share any example code if you have anything related to this.</p></div><div id="comment-63761-info" class="comment-info"><span class="comment-age">(09 Oct '17, 06:39)</span> golthitatun</div></div><span id="63762"></span><div id="comment-63762" class="comment"><div id="post-63762-score" class="comment-score"></div><div class="comment-text"><p>The first question here is: Lua or C++? I never took the effort to roll out a C++ development environment so cannot give any relevant advice.</p></div><div id="comment-63762-info" class="comment-info"><span class="comment-age">(09 Oct '17, 06:41)</span> sindy</div></div><span id="63763"></span><div id="comment-63763" class="comment"><div id="post-63763-score" class="comment-score"></div><div class="comment-text"><p>I am writing in Lua.</p></div><div id="comment-63763-info" class="comment-info"><span class="comment-age">(09 Oct '17, 06:52)</span> golthitatun</div></div><span id="63764"></span><div id="comment-63764" class="comment"><div id="post-63764-score" class="comment-score"></div><div class="comment-text"><p>As you say "I am writing", I suppose you only need help with some particular moment (like how to create the dissector chain)? Or you write in Lua in general but never wrote a dissector before? Have you already been <a href="https://www.wireshark.org/docs/wsdg_html_chunked/wslua_dissector_example.html">here</a>?</p></div><div id="comment-63764-info" class="comment-info"><span class="comment-age">(09 Oct '17, 07:11)</span> sindy</div></div></div><div id="comment-tools-63734" class="comment-tools"></div><div class="clear"></div><div id="comment-63734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

