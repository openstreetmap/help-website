+++
type = "question"
title = "Wireshark MATE: multiple combined Stop criterion for Gop"
description = '''Hi guys, didn&#x27;t do very much with MATE yet, so perhaps I&#x27;ve missed something. I need to define a Stop criterion with multiple dependencies. For instance: Stop if diameter.cmd.code=275 AND diameter.flags.request=0 The goal is to include not only the Session Termination Request but also the Answer wit...'''
date = "2015-08-06T02:28:00Z"
lastmod = "2016-02-20T09:55:00Z"
weight = 44903
keywords = [ "mate", "wireshark" ]
aliases = [ "/questions/44903" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark MATE: multiple combined Stop criterion for Gop](/questions/44903/wireshark-mate-multiple-combined-stop-criterion-for-gop)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44903-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>didn't do very much with MATE yet, so perhaps I've missed something.<br />
I need to define a Stop criterion with multiple dependencies.<br />
For instance:<br />
Stop if diameter.cmd.code=275 AND diameter.flags.request=0<br />
The goal is to include not only the Session Termination Request but also the Answer within the Gop.<br />
But any MATE example I found did only define a single Stop criterion.<br />
Has such kind of combined criterion been implemented at all? And if so, what's the syntax?<br />
And if not (that's what I'm afraid) could somebody provide an example how to handle such a multiple condition with MATE?</p><p>Thanks,<br />
Horst</p></div><div id="question-tags" class="tags-container tags">mate wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '15, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/576ba954bd7cdb8f84179da27546747c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Horst&#39;s gravatar image" /><p>Horst<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Horst has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-44903" class="comments-container"></div><div id="comment-tools-44903" class="comment-tools"></div><div class="clear"></div><div id="comment-44903-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50369"></span>

<div id="answer-container-50369" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50369-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The way to build complex <code>Start</code> and/or <code>Stop</code> conditions in MATE is <code>Transform</code>. <del>Unfortunately, LEGO has not (yet?) described the new syntax of <code>Transform</code> at <a href="https://wiki.wireshark.org/Mate/Manual">the MATE wiki page</a>.</del> I have updated <a href="https://wiki.wireshark.org/Mate/Manual">the MATE wiki page</a> with the new syntax of <code>Transform</code>; examples specifically relevant to the subject of this Question follow here.</p><p>So if you excuse my close-to-zero knowledge of Diameter, in the MATE configuration file, you would do the following:</p><p><strong>First</strong>, and maybe surprisingly <em>before</em> you describe the pdu from which you <code>Extract</code> the attributes to which you refer, you describe creation of a new AVP as a result of <code>Match</code> of other AVP(L)s:</p><pre><code>Transform stop_cond {
    Match (cmd_code=275, flags_request=0) Insert (my_attr = stop);
};</code></pre><p>The way above, the logical relationship between the two AVP matches is <code>and</code>. You could also define a logical <code>or</code> between them as in the following example, which is just an illustrative one, as for these particular attributes it would make little practical sense:</p><pre><code>Transform aggregate_stop_cond {
    Match (cmd_code=275) Insert (my_attr = stop);
    Match (flags_request=0) Insert (my_attr = stop);
};</code></pre><p>If you eventually need to use other <code>Match</code> mode than the default <code>Strict</code> in the <code>Transform</code>, you have to add the corresponding keyword right after the Match keyword itself, i.e. <code>Match Every</code> or <code>Match Loose</code>.</p><p><del>So you could write the above simple example (logical <em>or</em> between two individual conditions) the following way:</del></p><del></del><pre><code>Transform stop_cond {
    Match Loose (cmd_code=275, flags_request=0) Insert (my_attr = stop);
};</code></pre></s><p><del></del> Edit: as of current (2.0.1), Loose and Every matches behave different than expected, so the <del>example</del> above would insert the my_attr=stop AVP to all PDUs.</p><p>Similarly, you could omit the <code>Insert</code> keyword as it is only used for clarity since it is the default behaviour. The (dangerous) alternative is <code>Replace</code>, causing the whole AVPL you've used as a parameter to the <code>Match</code> to be replaced by the AVPL following the <code>Replace</code> keyword.</p><p><strong>Second</strong>, you have to "execute" the <code>Transform</code> in the pdu description <em>after</em> the <code>Extract</code> of all attributes to which it refers:</p><pre><code>Pdu my_diameter {
    Extract cmd_code From diameter.cmd.code ;
    Extract flags_request From diameter.flags.request ;
    Transform aggregate_stop_cond ;
};</code></pre><p><strong>Finally</strong>, you use the newly created "composite" AVP to define the stop condition:</p><pre><code>Gop diameter_conversation On my_diameter Match (..., ..., ...) {
    ...
    Stop (my_attr=stop);
    ...
};</code></pre><p>Note that you may even use a single <code>Transform</code></p><ul><li><p>to create several independent AVPs,</p></li><li><p>to assign different values to the same attribute, each using a different set of <code>Match</code> rules, of course provided that at most one such rule set defining a value can be matched for any given pdu.</p></li></ul><p>Example (of little practical use):</p><pre><code>Transform start_stop_cond {
    Match (flags_error=1) Insert (my_error = 1);
    Match (flags_request=1) Insert (my_attr = start);
    Match (flags_request=0) Insert (my_attr = stop);
};

...

Pdu ... {
    ...
    Transform start_stop_cond ;
    ...
};

...

Gop ... {
    ...
    Start (my_attr=start);
    Stop (my_attr=stop);
    Extra (my_error);
    ...
};</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '16, 09:55</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Mar '16, 00:59</p></div></div><div id="comments-container-50369" class="comments-container"><span id="50408"></span><div id="comment-50408" class="comment"><div id="post-50408-score" class="comment-score"></div><div class="comment-text"><p><em>"Unfortunately, LEGO has not (yet?) described the new syntax of Transform at the MATE wiki page."</em></p><p>Luis likely won't be updating anything; he's been quiet for some time now. Hopefully <em>someone</em> will take the time to update all the mate files though. For what it's worth, I've filed a bug report against the obsolete mate files. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12118">Wireshark Bug 12118</a>.</p></div><div id="comment-50408-info" class="comment-info"><span class="comment-age">(22 Feb '16, 08:17)</span> cmaynard ♦♦</div></div><span id="50695"></span><div id="comment-50695" class="comment"><div id="post-50695-score" class="comment-score"></div><div class="comment-text"><p>Hey sindy, many thanks for your answer. I'm quite busy at the moment but hopefully I'll find the time to dig into it.</p></div><div id="comment-50695-info" class="comment-info"><span class="comment-age">(02 Mar '16, 22:26)</span> Horst</div></div></div><div id="comment-tools-50369" class="comment-tools"></div><div class="clear"></div><div id="comment-50369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46367"></span>

<div id="answer-container-46367" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46367-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Actually I don't think it's really necessary to have this combination in the stop condition. MATE will include the Stop PDU (code=275) in the GOP but it will also include the Answer as being "After stop PDU." At least this shows up in the list of PDUs in the session.</p><p>I'm not sure if the fact that it's after the Stop PDU will matter but certainly the PDUs appear to be counted as part of the GOP.</p><p>(FWIW I don't think it's possible to actually have a complex stop condition like you listed. But I could always be wrong...)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '15, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span> </br></br></p></div></div><div id="comments-container-46367" class="comments-container"></div><div id="comment-tools-46367" class="comment-tools"></div><div class="clear"></div><div id="comment-46367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

