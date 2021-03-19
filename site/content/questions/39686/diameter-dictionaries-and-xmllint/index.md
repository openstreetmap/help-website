+++
type = "question"
title = "diameter dictionaries and xmllint"
description = '''Update: small dtd tweak - change avp name from IDREF to ID will eliminate one set of issues related to missing reference, but it will generate hundred of errors for every reuse of names like &quot;Unassigned&quot;, &quot;Reserved&quot; etc. ====================================================================== I am add...'''
date = "2015-02-06T08:35:00Z"
lastmod = "2015-02-19T20:02:00Z"
weight = 39686
keywords = [ "xml", "diameter" ]
aliases = [ "/questions/39686" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [diameter dictionaries and xmllint](/questions/39686/diameter-dictionaries-and-xmllint)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39686-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Update: small dtd tweak - change avp name from IDREF to ID will eliminate one set of issues related to missing reference, but it will generate hundred of errors for every reuse of names like "Unassigned", "Reserved" etc.</p><p>======================================================================</p><p>I am adding diameter dictionary to wireshark Version 1.8.4 (SVN Rev 46250 from /trunk-1.8).</p><p>I would like to run xmllint validation. I tried unchanged directory first and I see that it could not find types and vendor-ids, defined in base. I suppose I am missing something.</p><p>Example failures from running command: 'xmllint --dtdvalid dictionary.dtd dictionary.xml sip.xml'</p><p>sip.xml:39: element type: validity error : IDREF attribute type-name references an unknown ID "Unsigned32" sip.xml:42: element type: validity error : IDREF attribute type-name references an unknown ID "Unsigned32"</p></div><div id="question-tags" class="tags-container tags">xml diameter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '15, 08:35</strong></p><img src="https://secure.gravatar.com/avatar/1bea25433dd75445237bc5c42a225287?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alex4747&#39;s gravatar image" /><p>alex4747<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alex4747 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Feb '15, 06:42</p></div></div><div id="comments-container-39686" class="comments-container"></div><div id="comment-tools-39686" class="comment-tools"></div><div class="clear"></div><div id="comment-39686-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39930"></span>

<div id="answer-container-39930" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39930-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, my only thought would be: the Diameter dictionary is more XML-like than proper XML. Wireshark has its own custom parser for reading the Diameter dictionaries so I'm not sure xmllint is going to help you much anyway.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '15, 07:29</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-39930" class="comments-container"><span id="39931"></span><div id="comment-39931" class="comment"><div id="post-39931-score" class="comment-score"></div><div class="comment-text"><p>Perhaps you should tell us what problem you are trying to fix by running xmllint - like your custom .xml not beeing loaded or something like that...</p></div><div id="comment-39931-info" class="comment-info"><span class="comment-age">(18 Feb '15, 08:25)</span> Anders ♦</div></div><span id="39942"></span><div id="comment-39942" class="comment"><div id="post-39942-score" class="comment-score"></div><div class="comment-text"><p>Custom xml is being loaded but one would never know whether all the parts were loaded or not - I could not find a way to get wireshark diagnostic on dictionary loads.</p><p>It seems that I am very naive to assume dictionary.dtd file implied compliance check.</p></div><div id="comment-39942-info" class="comment-info"><span class="comment-age">(19 Feb '15, 03:41)</span> alex4747</div></div></div><div id="comment-tools-39930" class="comment-tools"></div><div class="clear"></div><div id="comment-39930-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39967"></span>

<div id="answer-container-39967" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39967-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Make three small tweaks in dictionary.dtd:</p><ol><li>Avp name should be CDATA (we cannot use avp name as ID because there are too many duplicates)</li><li>Gavp name should be CDATA (we cannot use gavp name as IDREF for the same reason)</li><li>Gavp set could be empty (Failed-AVP definition has empty gavp set and it is correct)</li></ol><p>Add missing types (Float32, Flag64, Address) to dictionary.xml</p><p>And you will see xmllint validation pass.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '15, 20:02</strong></p><img src="https://secure.gravatar.com/avatar/1bea25433dd75445237bc5c42a225287?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alex4747&#39;s gravatar image" /><p>alex4747<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alex4747 has no accepted answers">0%</span></p></div></div><div id="comments-container-39967" class="comments-container"></div><div id="comment-tools-39967" class="comment-tools"></div><div class="clear"></div><div id="comment-39967-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

