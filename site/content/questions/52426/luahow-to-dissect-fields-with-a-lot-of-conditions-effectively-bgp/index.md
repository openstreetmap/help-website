+++
type = "question"
title = "LUA:How to dissect fields with a lot of conditions effectively  (BGP) ?"
description = '''I am making Lua script to dissect BGP protocol. It has many path attributes and within each other values...:   I can dissect all writing if conditions, but I think there is a easier and effectively way to dissect all values. BGP reference: https://tools.ietf.org/html/rfc4271'''
date = "2016-05-11T03:53:00Z"
lastmod = "2016-05-12T14:24:00Z"
weight = 52426
keywords = [ "lua", "fields" ]
aliases = [ "/questions/52426" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [LUA:How to dissect fields with a lot of conditions effectively (BGP) ?](/questions/52426/luahow-to-dissect-fields-with-a-lot-of-conditions-effectively-bgp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52426-score" class="post-score" title="current number of votes">0</div><span id="post-52426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am making Lua script to dissect BGP protocol. It has many path attributes and within each other values...:</p><p><img src="https://2.bp.blogspot.com/-UdXNtfK9ERw/TyJAHgHS5YI/AAAAAAAAAlM/D4at2KGkhOU/s1600/bgp+attributes.PNG" alt="alt text" /></p><p>I can dissect all writing if conditions, but I think there is a easier and effectively way to dissect all values.</p><p>BGP reference: <a href="https://tools.ietf.org/html/rfc4271">https://tools.ietf.org/html/rfc4271</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-fields" rel="tag" title="see questions tagged &#39;fields&#39;">fields</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '16, 03:53</strong></p><img src="https://secure.gravatar.com/avatar/0164b3a0b6fca8e2931eb42defb1ebfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="javiguembe&#39;s gravatar image" /><p><span>javiguembe</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="javiguembe has no accepted answers">0%</span></p></img></div></div><div id="comments-container-52426" class="comments-container"><span id="52432"></span><div id="comment-52432" class="comment"><div id="post-52432-score" class="comment-score"></div><div class="comment-text"><p>Is there an issue with the existing c-based BGP dissector?</p></div><div id="comment-52432-info" class="comment-info"><span class="comment-age">(11 May '16, 07:30)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="52434"></span><div id="comment-52434" class="comment"><div id="post-52434-score" class="comment-score"></div><div class="comment-text"><p>No, but I want to do it to practice.</p></div><div id="comment-52434-info" class="comment-info"><span class="comment-age">(11 May '16, 09:01)</span> <span class="comment-user userinfo">javiguembe</span></div></div></div><div id="comment-tools-52426" class="comment-tools"></div><div class="clear"></div><div id="comment-52426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52437"></span>

<div id="answer-container-52437" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52437-score" class="post-score" title="current number of votes">1</div><span id="post-52437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="javiguembe has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You may want to read <a href="https://www.lua.org/pil/2.5.html">the part of Lua manual which deals with data types named Tables</a>, and make use of the Wireshark's Lua API's ability to use Lua tables as number to string translation vocabularies. An example from one of my ad hoc Lua dissectors:</p><pre><code>-- first, we define translation tables for individual items
prec_level_values = {}
prec_level_values[0] = &quot;flashOverride&quot;
prec_level_values[1] = &quot;flash&quot;
prec_level_values[2] = &quot;immediate&quot;
prec_level_values[3] = &quot;priority&quot;
prec_level_values[4] = &quot;routine&quot;

lfb_indictn_values = {}
lfb_indictn_values[0] = &quot;lfbAllowed&quot;
lfb_indictn_values[1] = &quot;lfbNotAllowed&quot;
lfb_indictn_values[2] = &quot;pathReserved&quot;

-- later, we define the Protocol fields&#39; properties, referring to the conversion tables above
-- as a way to translate the individual numeric values to corresponding strings
MLPP_Prec_level = ProtoField.uint8(&quot;mlpp.Prec_level&quot;,&quot;Prec_level&quot;,base.DEC,prec_level_values)
MLPP_LFB_Indictn = ProtoField.uint8(&quot;mlpp.LFB_Indictn&quot;,&quot;LFB_Indictn&quot;,base.DEC,lfb_indictn_values)

-- then, we tell Wireshark that these fields belong to this protocol
MLPP_proto.fields = {MLPP_Prec_level, MLPP_LFB_Indictn, ...}

-- and in the body of the dissector, we just extract the portions of tvb which contain those numeric values and pass them as arguments to tree:add
    local prec = buffer:range(4,1)
    local lfb_ind = buffer:range(7,1)
    subtree:add(MLPP_Prec_level,prec)
    subtree:add(MLPP_LFB_Indictn,lfb_ind)

-- instead, if you don&#39;t need the buffer ranges for any other purpose, you could just write
    subtree:add(MLPP_Prec_level,buffer:range(4,1))
    subtree:add(MLPP_LFB_Indictn,buffer:range(7,1))</code></pre><p>As for dealing with the higher 4 bits of the MSB, a forged example of what you could do for two bits, X and Y, where each value of each bit has to be translated to a string and the values of the bits do not affect each other, you can translate all four numeric combinations to concatenations of strings which you then split using a separator character:</p><pre><code>my_values = {}
my_values[0] = &quot;[email protected]_is_0&quot;
my_values[1] = &quot;[email protected]_is_1&quot;
my_values[2] = &quot;[email protected]_is_0&quot;
my_values[3] = &quot;[email protected]_is_1&quot;

local aux_number = buffer:range(5,1):uint8
local aux_text = my_values[aux_number]
local X_text_value,Y_text_value = aux_text:match(&quot;(.*)@(.*)&quot;)

-- or you can do the same on a single line
local X_text_value,Y_text_value = my_values[buffer:range(5,1):uint8]:match(&quot;(.*)@(.*)&quot;)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '16, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-52437" class="comments-container"><span id="52460"></span><div id="comment-52460" class="comment"><div id="post-52460-score" class="comment-score"></div><div class="comment-text"><p>Thanks for answer !! Is a god answer, but I know that I can make tables to dissect a lot of posible values. In fact, I use it to dissect Attribute types using Attribute type codes (see picture above).</p><p>Althougth, my question is; How to dissect Attribute Values (the last column) effectively. I said that because Attribute Values depends on fields before it: Attribute type, class and attribute value code. So I have to make if conditionals like:</p><p>if(attribute_type_cod ==1 &amp;&amp; flag_o ==0) then subtree:add (attr_values1_withtable,buf(x,x)) end</p><p>I need to do 10 conditionals like this, other there is another way to do?</p></div><div id="comment-52460-info" class="comment-info"><span class="comment-age">(12 May '16, 02:00)</span> <span class="comment-user userinfo">javiguembe</span></div></div><span id="52477"></span><div id="comment-52477" class="comment"><div id="post-52477-score" class="comment-score"></div><div class="comment-text"><blockquote><p>It is a good answer, but...</p></blockquote><p>Well, the quality of the question has a large impact on the quality of the answer :-) So rather than pasting the screenshot of a table (which seems inconsistent until you look into the RFC you've given a link to), it would have been better to write that you need to translate numeric values of protocol field A to text ones in several different ways, choosing the appropriate way up to the numeric value of protocol field B.</p><p>For Lua in general, there is <a href="http://lua-users.org/wiki/SwitchStatement">a page suggesting several possible implementations of "case" (Pascal) or "switch" (C, Java) replacement of a bunch of "if" statements to choose a branch of algorithm to be executed</a>.</p><p>But as we talk about Wireshark's Lua API here, we'd like to have the possibility to use Lua tables to translate the numeric values of parameters to text names so that they could be used for filtering, printing using tshark etc.</p><p>I haven't tested that yet, but as the "values" in a Lua table may be variables (of any type, even other tables), it should be possible to do the following (example simplified to illustrative minimum):</p><pre><code>my_value_table_1 = {}
my_value_table_1[0] = &quot;IGP&quot;
my_value_table_1[1] = &quot;EGP&quot;
my_value_table_1[2] = &quot;INCOMPLETE&quot;

my_value_table_2 = {}
my_value_table_2[1] = &quot;AS_SET&quot;
my_value_table_2[2] = &quot;AS_SEQUENCE&quot;

my_type_names_table = {}
my_type_names_table[1] = &quot;ORIGIN&quot;
my_type_names_table[2] = &quot;AS_PATH&quot;

BGP_attr_type_code = ProtoField.uint8(&quot;bgp.attr_type_code&quot;,&quot;Attr_type_code&quot;,base.DEC,my_type_names_table)

BGP_origin_value = ProtoField.uint8(&quot;bgp.attr_type.origin&quot;,&quot;Attr_origin_value&quot;,base.DEC,my_value_table_1)

BGP_as_path_value = ProtoField.uint8(&quot;bgp.attr_type.as_path&quot;,&quot;Attr_as_path_value&quot;,base.DEC,my_value_table_2)

BGP_proto.fields = {BGP_attr_type_code, BGP_origin_value, BGP_as_path_value, ...}

my_type_fields_table = {}
my_type_fields_table[1] = BGP_origin_value
my_type_fields_table[2] = BGP_as_path_value

local attr_type_code = buffer:range(4,1)
local attr_len = buffer:range(5,1)
subtree:add(BGP_attr_type_code,buffer:range(4,1))
subtree:add(my_type_fields_table[attr_type_code],buffer:range(6,attr_len))</code></pre></div><div id="comment-52477-info" class="comment-info"><span class="comment-age">(12 May '16, 12:31)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="52482"></span><div id="comment-52482" class="comment"><div id="post-52482-score" class="comment-score"></div><div class="comment-text"><p>...continuation:</p><p>As a Lua table may contain another table, you can also individually extract the values of bits O, T, P, E and use them as additional key values as shown below, provided that you create a corresponding hierarchy of tables.</p><pre><code>subtree:add(my_type_fields_table[attr_type_code][O_value][T_value][P_value][E_value],buffer:range(6,attr_len))</code></pre><p>While you can define tables (of tables) using a compact notation, like</p><pre><code>topmost_table = {
   {
       {&quot;x111&quot;,&quot;x112&quot;}, {&quot;x121&quot;,&quot;x122&quot;}
   }, {
       {&quot;x211&quot;,&quot;x212&quot;}, {&quot;x221&quot;,&quot;x222&quot;}
   }
}</code></pre><p>, doing so will automatically generate the keys as monotonous sequences of numeric values starting from of 1, so you'll get the following values:</p><pre><code>topmost_table[1][1][1]: &quot;x111&quot;
topmost_table[1][1][2]: &quot;x112&quot;
...
topmost_table[2][2][2]: &quot;x222&quot;</code></pre><p>Therefore, you have to construct the individual levels of the tables "manually", which will allow you to specify the keys as necessary (O,T,P,E values chosen randomly):</p><pre><code>attr_type_table[2][0][1][0][1] = BGP_as_path_value</code></pre><p>While the Wireshark's Lua API will handle translation of a key for which no value is given in the table referred to in the protocol field specification very simply, by displaying "Unknown" in the packet dissection pane, things won't go that easy if you ask TreeItem:add to add a non-existent protocol field. Therefore, you'll likely want to check first whether attr_type_table[TypeCode][O][T][P][E] returns a value (a variable holding a reference to a protocol field descriptor), and only execute the TreeItem:add if it does.</p></div><div id="comment-52482-info" class="comment-info"><span class="comment-age">(12 May '16, 14:24)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-52437" class="comment-tools"></div><div class="clear"></div><div id="comment-52437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

