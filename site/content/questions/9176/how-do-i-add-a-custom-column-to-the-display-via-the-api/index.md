+++
type = "question"
title = "How do I add a custom column to the display via the API?"
description = '''I know how to add user defined columns from the Wireshark GUI, but I want to know if there is any way to do this through code. EDITED: I tried adding user defined field to column_info.h but no help. It is not getting reflected in the GUI. I added the corresponding entry in slist[] and dlist[].'''
date = "2012-02-22T20:49:00Z"
lastmod = "2012-02-26T03:39:00Z"
weight = 9176
keywords = [ "development", "columns" ]
aliases = [ "/questions/9176" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I add a custom column to the display via the API?](/questions/9176/how-do-i-add-a-custom-column-to-the-display-via-the-api)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9176-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know how to add user defined columns from the Wireshark GUI, but I want to know if there is any way to do this through code.</p><p><strong>EDITED</strong>: I tried adding user defined field to column_info.h but no help. It is not getting reflected in the GUI. I added the corresponding entry in <code>slist[]</code> and <code>dlist[]</code>.</p></div><div id="question-tags" class="tags-container tags">development columns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '12, 20:49</strong></p><img src="https://secure.gravatar.com/avatar/d221d26845724614e25ab8e51887c4bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ashish_goel&#39;s gravatar image" /><p>ashish_goel<br />
<span class="score" title="15 reputation points">15</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ashish_goel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Feb '12, 10:37</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-9176" class="comments-container"><span id="9183"></span><div id="comment-9183" class="comment"><div id="post-9183-score" class="comment-score"></div><div class="comment-text"><p>any suggestions???</p></div><div id="comment-9183-info" class="comment-info"><span class="comment-age">(23 Feb '12, 07:15)</span> ashish_goel</div></div><span id="9214"></span><div id="comment-9214" class="comment"><div id="post-9214-score" class="comment-score"></div><div class="comment-text"><p>guys plz help.. Is it something nobody has ever tried before??</p></div><div id="comment-9214-info" class="comment-info"><span class="comment-age">(26 Feb '12, 03:04)</span> ashish_goel</div></div></div><div id="comment-tools-9176" class="comment-tools"></div><div class="clear"></div><div id="comment-9176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9215"></span>

<div id="answer-container-9215" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9215-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Columns are not added through the API, they are added through the preference file(s).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '12, 03:39</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9215" class="comments-container"><span id="9247"></span><div id="comment-9247" class="comment"><div id="post-9247-score" class="comment-score"></div><div class="comment-text"><p>thanx Sake Blok for the help :)..</p><p>which preference file you are talking in this case? I searched through internet and got a hint about preference file but I couldn't find such file in the code. maybe the now the code and file names are updated.</p><p>Can you plz guide me a little bit on where I should approach it??</p></div><div id="comment-9247-info" class="comment-info"><span class="comment-age">(27 Feb '12, 06:53)</span> ashish_goel</div></div><span id="9248"></span><div id="comment-9248" class="comment"><div id="post-9248-score" class="comment-score"></div><div class="comment-text"><p>I am talking about the preferences file in which all the users preferences are kept. It is generated by Wireshark and on linux resides in the users home-directory in the directory .wireshark.</p><p>If you want to create a custom version of Wireshark that creates a different column layout by default, you can change it in the function "init_prefs" in the file "epan/prefs.c".</p><p>Beware, changes made here will only be used by users that do not have a preferences file yet (i.e. only users that install Wireshark for the first time will be affected).</p></div><div id="comment-9248-info" class="comment-info"><span class="comment-age">(27 Feb '12, 07:13)</span> SYN-bit ♦♦</div></div><span id="9249"></span><div id="comment-9249" class="comment"><div id="post-9249-score" class="comment-score"></div><div class="comment-text"><p>I followed the procedure but how do i set data into this column through my dissector code. Because in dissector code it needs to know the COL_XXX constant for the column.</p><p>To define this COL_XXX constant I even added entry for my custom column in column.c, column_info.h and column-utils.c but nothing worked.</p></div><div id="comment-9249-info" class="comment-info"><span class="comment-age">(27 Feb '12, 08:01)</span> ashish_goel</div></div><span id="9250"></span><div id="comment-9250" class="comment"><div id="post-9250-score" class="comment-score"></div><div class="comment-text"><p>There are two ways to create column data:</p><p>1) Have your dissector create a field and use that field in a "custom column" like you would do in the GUI. This is the preferred way. You will need to add something like "%Cus:ip.ttl:0:R" to the init_prefs function.</p><p>2) You can manually construct a column. This is the old way and should be avoided. If you still want/need to use this method, see paragraph 1.5 in the file "doc/README.developer", which I'm sure you have already read ;-)</p></div><div id="comment-9250-info" class="comment-info"><span class="comment-age">(27 Feb '12, 08:17)</span> SYN-bit ♦♦</div></div><span id="9267"></span><div id="comment-9267" class="comment"><div id="post-9267-score" class="comment-score"></div><div class="comment-text"><p>sry but I didn't get your solution. Can you plz explain the point 1 clearly. specially the logic behind the string : "%Cus:ip.ttl:0:R"</p></div><div id="comment-9267-info" class="comment-info"><span class="comment-age">(28 Feb '12, 07:48)</span> ashish_goel</div></div><span id="9275"></span><div id="comment-9275" class="comment not_top_scorer"><div id="post-9275-score" class="comment-score"></div><div class="comment-text"><p>I was able to do it finally. I had to delete the local preferences file from hard disk for the changes to take effect.</p><p>I am also able to relate why do we need to add "%Cus"(it specifies that we are using a custom column) and "ip.ttl"(this specifies the protocol and its field whose value we want to use in the column display) which you mentioned in the string.</p><p>But the part "0:R" of the string is still not clear..</p></div><div id="comment-9275-info" class="comment-info"><span class="comment-age">(28 Feb '12, 20:57)</span> ashish_goel</div></div></div><div id="comment-tools-9215" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-9215-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

