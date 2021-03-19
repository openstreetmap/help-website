+++
type = "question"
title = "What is wrong with the following tcp postdissector registration?"
description = '''My module is a postdissector for tcp packets that needs to be called sometime after the tcp dissector has done its bit. My proto_register_foo() and proto_reg_handoff_foo() functions are as given below: void proto_register_foo(void) { static hf_register_info hf[] = {  ...  };  static gint *ett[] = { ...'''
date = "2012-08-05T23:54:00Z"
lastmod = "2012-08-06T05:59:00Z"
weight = 13379
keywords = [ "proto_register", "postdissector", "tcp" ]
aliases = [ "/questions/13379" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [What is wrong with the following tcp postdissector registration?](/questions/13379/what-is-wrong-with-the-following-tcp-postdissector-registration)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13379-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My module is a postdissector for tcp packets that needs to be called sometime after the tcp dissector has done its bit. My <em>proto_register_foo()</em> and <em>proto_reg_handoff_foo()</em> functions are as given below:</p><p><em>void<br />
proto_register_foo(void)</em><br />
{<br />
<em>static hf_register_info hf[]</em> = {<br />
...<br />
};<br />
static gint *ett[] = { ...<br />
};<br />
</p><pre><code>proto_foo = proto_register_protocol(&quot;Foo Protocol&quot;,   
    &quot;FOO&quot;, &quot;foo&quot;);    
register_dissector(&quot;foo&quot;, dissect_foo, proto_foo);  
proto_register_field_array(proto_foo, hf, array_length(hf));  
proto_register_subtree_array(ett, array_length(ett));</code></pre><p>}</p><p><em>void<br />
proto_reg_handoff_tcp(void)</em> {<br />
<em>dissector_handle_t foo_handle</em>;<br />
</p><pre><code>tcp_orb_handle = find_dissector(&quot;foo&quot;);  
dissector_add_uint(&quot;ip.proto&quot;, IP_PROTO_TCP, foo_handle);  
register_postdissector(foo_handle);</code></pre><p>}<br />
</p><p>The dissector is being called, but instead of being called at the end, it's being called <em>before</em> the tcp dissector. Worse, the tcp dissector is not being called at all! What mistake have I made here?</p></div><div id="question-tags" class="tags-container tags">proto_register postdissector tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '12, 23:54</strong></p><img src="https://secure.gravatar.com/avatar/46196bc495ce51058590c4e4ae334d22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SidR&#39;s gravatar image" /><p>SidR<br />
<span class="score" title="245 reputation points">245</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SidR has 3 accepted answers">30%</span> </br></br></p></div></div><div id="comments-container-13379" class="comments-container"></div><div id="comment-tools-13379" class="comment-tools"></div><div class="clear"></div><div id="comment-13379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13391"></span>

<div id="answer-container-13391" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13391-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You've registered the dissector as both a postdissector (register_postdissector()) and as a regular dissector taking all traffic on ip.proto==IP_PROTO_TCP. The latter means that your dissector is pre-empting the TCP dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '12, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span> </br></br></p></div></div><div id="comments-container-13391" class="comments-container"><span id="13412"></span><div id="comment-13412" class="comment"><div id="post-13412-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jeff. That seems to be the case here.</p></div><div id="comment-13412-info" class="comment-info"><span class="comment-age">(06 Aug '12, 20:55)</span> SidR</div></div></div><div id="comment-tools-13391" class="comment-tools"></div><div class="clear"></div><div id="comment-13391-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

