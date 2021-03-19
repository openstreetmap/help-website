+++
type = "question"
title = "Getter for ProtoField in Lua"
description = '''Hi, I&#x27;m a newbie in Lua and I work on a dissector plugin. At the beginning, I created a ProtoField with a certain type : local var1 = ProtoField.uint8 ( &quot;my.ID1&quot; , &quot;my interesting string&quot; , base.HEX )  However, for some reason, I would like to change the type of ProtoField sometimes. I don&#x27;t think i...'''
date = "2017-07-06T06:04:00Z"
lastmod = "2017-07-06T06:21:00Z"
weight = 62570
keywords = [ "lua", "getter", "protofield" ]
aliases = [ "/questions/62570" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getter for ProtoField in Lua](/questions/62570/getter-for-protofield-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62570-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm a newbie in Lua and I work on a dissector plugin. At the beginning, I created a ProtoField with a certain type :</p><pre><code>local var1 = ProtoField.uint8 ( &quot;my.ID1&quot; , &quot;my interesting string&quot; , base.HEX )</code></pre><p>However, for some reason, I would like to change the type of ProtoField sometimes. I don't think it's possible to change the type of var1 so my idea is to create a new one, using the string from the first one :</p><pre><code>local var2 = ProtoField.string ( &quot;my.ID2&quot; , var1.getMyInterestingString())</code></pre><p>Unfortunately, I didn't find anywhere how to reach attributes of the first Protofield. Do you know if it is possible ?</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags">lua getter protofield</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '17, 06:04</strong></p><img src="https://secure.gravatar.com/avatar/bd2aa9f8bc1b7271efcc67eab4613190?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MattJuillet&#39;s gravatar image" /><p>MattJuillet<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MattJuillet has no accepted answers">0%</span></p></div></div><div id="comments-container-62570" class="comments-container"></div><div id="comment-tools-62570" class="comment-tools"></div><div class="clear"></div><div id="comment-62570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62571"></span>

<div id="answer-container-62571" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62571-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Incidentally, <a href="https://ask.wireshark.org/users/655/jeffmorriss">@JeffMorriss</a>' answer to <a href="https://ask.wireshark.org/questions/62100/is-the-possibility-to-overload-fields-definitions-a-controlled-property-which-can-be-relied-on">my question</a> should solve your ultimate goal, although not exactly your question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '17, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-62571" class="comments-container"><span id="62572"></span><div id="comment-62572" class="comment"><div id="post-62572-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the link. It means I can "override" an existing ProtoField with another type, which is interesting to me !</p><p>However, to do that, I need to know the string in the first object, what I don't. With your help, now I know I can do that : local var1 = ProtoField.uint8 ( "my.ID1" , "my interesting string") ... local var2 = ProtoField.string( "my.ID1" , ??? )</p><p>But, how can I get the string from the first object ?</p></div><div id="comment-62572-info" class="comment-info"><span class="comment-age">(06 Jul '17, 06:43)</span> MattJuillet</div></div><span id="62573"></span><div id="comment-62573" class="comment"><div id="post-62573-score" class="comment-score"></div><div class="comment-text"><p>I am not sure I understand why would you want to extract the string (the "abbr" in this case) from the definition of the first ProtoField if it was you who has put it there, so you can just use the same string for both ProtoFields?</p></div><div id="comment-62573-info" class="comment-info"><span class="comment-age">(06 Jul '17, 06:48)</span> sindy</div></div><span id="62574"></span><div id="comment-62574" class="comment"><div id="post-62574-score" class="comment-score"></div><div class="comment-text"><p>The hypothesis is that I don't know the description of the protofield, and I want to get it to create a new one (or update the first one). That's why I try to find a "getter" to do that, or a way to change the type without knowing the description.</p><p>Sorry if I wasn't clear at the beginning.</p></div><div id="comment-62574-info" class="comment-info"><span class="comment-age">(06 Jul '17, 06:57)</span> MattJuillet</div></div><span id="62575"></span><div id="comment-62575" class="comment"><div id="post-62575-score" class="comment-score">1</div><div class="comment-text"><p>By defning another <code>ProtoField</code> with same <code>name</code> and <code>abbr</code> and different <code>type</code> you do not affect the previous one in any way, it still exists. What you can do afterwards is that, depending on the type you need, you choose the appropriate one of your ProtoFields to add to the dissection tree. So they share the name as seen from outside (when writing display filters), but they remain distinct in terms of handling in your dissector. I've never tried how a display filter evaluation handles fields with same name but different type e.g. in comparison (e.g. how <code>my_elem == "12"</code> is evaluated when the actual type of <code>my_elem</code> in the dissection tree is <code>uint8</code>).</p><p>There is the <code>Field</code> function which you may use to access value and other attributes, including <code>name</code> and <code>type</code>, of a <code>ProtoField</code> contributed by another dissector (even an embedded one), but you have to know its <code>abbr</code> (i.e. the sring used to refer to it in display filter syntax).</p></div><div id="comment-62575-info" class="comment-info"><span class="comment-age">(06 Jul '17, 07:24)</span> sindy</div></div><span id="62577"></span><div id="comment-62577" class="comment not_top_scorer"><div id="post-62577-score" class="comment-score"></div><div class="comment-text"><p>Thank you for all these explanations, it's very useful to me!</p><p>I'm going to try it and I'll tell you if it works ;)</p></div><div id="comment-62577-info" class="comment-info"><span class="comment-age">(06 Jul '17, 08:05)</span> MattJuillet</div></div><span id="62588"></span><div id="comment-62588" class="comment"><div id="post-62588-score" class="comment-score">1</div><div class="comment-text"><p>BTW, if you have trouble to find out how to use <code>Field.new</code>, a short code which uses extraction of already dissected protocol fields is in my answer to <a href="https://ask.wireshark.org/questions/49130/wireless-partial-virtual-bitmap">this question</a>.</p></div><div id="comment-62588-info" class="comment-info"><span class="comment-age">(06 Jul '17, 10:18)</span> sindy</div></div><span id="62603"></span><div id="comment-62603" class="comment not_top_scorer"><div id="post-62603-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your help! Unfortunately, I can't use Field because, as you said earlier, we need to know the abbr, and I don't in my case. The only thing I have is the first ProtoField object, without knowing anything inside.</p><p>I'll find another way, no problem!</p></div><div id="comment-62603-info" class="comment-info"><span class="comment-age">(07 Jul '17, 05:23)</span> MattJuillet</div></div></div><div id="comment-tools-62571" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-62571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

