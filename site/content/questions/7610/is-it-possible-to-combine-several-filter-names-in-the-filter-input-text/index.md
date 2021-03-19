+++
type = "question"
title = "is it possible to combine several filter names in the filter input text ?"
description = '''I think It would be very useful if you could use the name of the filter to create another filters. I&#x27;m not sure if you can do that. For instance you create the following filters: arp || smb &amp;lt;-- under the name of LAN rip || eigrp &amp;lt;--- under the name of WAN so you could search for: LAN OR WAN is...'''
date = "2011-11-24T09:21:00Z"
lastmod = "2011-11-25T13:56:00Z"
weight = 7610
keywords = [ "filters" ]
aliases = [ "/questions/7610" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [is it possible to combine several filter names in the filter input text ?](/questions/7610/is-it-possible-to-combine-several-filter-names-in-the-filter-input-text)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7610-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I think It would be very useful if you could use the name of the filter to create another filters. I'm not sure if you can do that. For instance you create the following filters: arp || smb &lt;-- under the name of LAN rip || eigrp &lt;--- under the name of WAN</p><p>so you could search for: LAN OR WAN</p><p>is there anything similar to this? thank you</p></div><div id="question-tags" class="tags-container tags">filters</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '11, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/57c8ddb7ed6ba271696a4631abf6dd9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BorjaMerino&#39;s gravatar image" /><p>BorjaMerino<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BorjaMerino has no accepted answers">0%</span></p></div></div><div id="comments-container-7610" class="comments-container"></div><div id="comment-tools-7610" class="comment-tools"></div><div class="clear"></div><div id="comment-7610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7617"></span>

<div id="answer-container-7617" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7617-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's not the exact way you want to do it, but you might want to take a look at display filter macros in the <strong>Analyze -&gt; Display Filter Macro</strong> menu option. You could add two new macros:</p><ol><li>Name = "wan" and Text = "rip or eigrp"</li><li>Name = "lan" and Text = "arp or smb"</li></ol><p>After that you can call the macros in the filter bar like this: <strong>${wan} or ${lan}</strong>. I agree that it is a bit awkward to enter the additional dollar signs and the curly brakets, but it might be faster than typing the long filters if they're really complex.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '11, 15:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-7617" class="comments-container"></div><div id="comment-tools-7617" class="comment-tools"></div><div class="clear"></div><div id="comment-7617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7636"></span>

<div id="answer-container-7636" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7636-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can also save your <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWorkDefineFilterSection.html">Display Filters</a>.<br />
Go to:<br />
Analyze | Display filters... or hit Filter at the left side of the Filter Toolbar<br />
Hit New<br />
Filter name: wan<br />
Filter string: rip or eigrip<br />
Hit Apply<br />
Repeat the steps to add the second filter.<br />
<br />
Apply your display filters:<br />
Open the Display Filter dialog box again.<br />
Select your filter.<br />
Hit OK to apply the filter.<br />
<br />
Or you can edit the dfilters file:<br />
C:Documents and SettingsUSERApplication DataWireshark<br />
Add your filters to the file.<br />
Make sure you end with an empty line, otherwise you won't see your filter.<br />
"wan" rip or eigrp<br />
"lan" arp or smb<br />
"test" http or smb and ip.addr==192.168.19.10</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '11, 13:56</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-7636" class="comments-container"></div><div id="comment-tools-7636" class="comment-tools"></div><div class="clear"></div><div id="comment-7636-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

