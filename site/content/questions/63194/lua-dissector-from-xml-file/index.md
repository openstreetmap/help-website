+++
type = "question"
title = "lua dissector from XML file"
description = '''Is there some way to create a dissector from XML file? I have few messages which are defined in XML files. I&#x27;d like to use some generic dissector so that one will have to use only the XML file in order to define the packet (all messages are based on UDP), the dissector will read all the XML files an...'''
date = "2017-07-27T22:24:00Z"
lastmod = "2017-07-28T03:07:00Z"
weight = 63194
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/63194" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [lua dissector from XML file](/questions/63194/lua-dissector-from-xml-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63194-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there some way to create a dissector from XML file?</p><p>I have few messages which are defined in XML files. I'd like to use some generic dissector so that one will have to use only the XML file in order to define the packet (all messages are based on UDP), the dissector will read all the XML files and will parse the data based on it.</p></div><div id="question-tags" class="tags-container tags">lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '17, 22:24</strong></p><img src="https://secure.gravatar.com/avatar/b02c5dfff2049bed61dbced93bf455d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BMWE&#39;s gravatar image" /><p>BMWE<br />
<span class="score" title="46 reputation points">46</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BMWE has one accepted answer">100%</span></p></div></div><div id="comments-container-63194" class="comments-container"></div><div id="comment-tools-63194" class="comment-tools"></div><div class="clear"></div><div id="comment-63194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63206"></span>

<div id="answer-container-63206" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63206-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You may want to have a look at <a href="http://wsgd.free.fr/index.html">this project</a>. It is not fed by xml directly but you may use a script to convert your xml descriptions into the syntax required by this project.</p><p>Other approach would be to somewhat duplicate that project by using Lua to read your xml description of the protocol and create protocol fields at startup, but I am not really sure you can read from a file during the initialisation phase. In Lua, you can use constructs like</p><p><code>all_my_fields = {} local n=0</code></p><p>and then, for each protocol field description extracted from XML:</p><p><code>all_my_fields[n] = ProtoField.uint8(field_abbr_from_XML,field_name_from_XML,base.HEX,     all_my_field_values_table_from_XML[n],field_bit_mask_from_XML) n=n+1</code></p><p>choosing the right ProtoField type (uint8 in this case) and base (base.HEX in this case) which I suspect must be literals, and then <strong>probably</strong> (I've never tested it so a different syntax may be necessary) you can use</p><p><code>my_proto.fields = all_my_fields</code></p><p>The tables for translation of numeric values to text strings must be complete before you use them to create a ProtoField as for some reason they are copied, not referred to.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '17, 03:07</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-63206" class="comments-container"><span id="63228"></span><div id="comment-63228" class="comment"><div id="post-63228-score" class="comment-score"></div><div class="comment-text"><p>This project seems to be very useful. Thank you</p></div><div id="comment-63228-info" class="comment-info"><span class="comment-age">(28 Jul '17, 22:29)</span> BMWE</div></div></div><div id="comment-tools-63206" class="comment-tools"></div><div class="clear"></div><div id="comment-63206-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

