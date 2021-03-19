+++
type = "question"
title = "Braces [] inside abbreviated name FIELDABBREV of header_field_info"
description = '''I need to have braces for abbreviated field names. For example, let&#x27;s say I have an array of structures like the following: typedef struct _person { int height; int age; } person; typedef struct _people { int number; person[10]; int dummy; } people;  When I dissect the people structure, I&#x27;d like to ...'''
date = "2016-02-23T10:16:00Z"
lastmod = "2016-02-23T15:10:00Z"
weight = 50444
keywords = [ "fields", "abbreviated", "crash" ]
aliases = [ "/questions/50444" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Braces \[\] inside abbreviated name FIELDABBREV of header\_field\_info](/questions/50444/braces-inside-abbreviated-name-fieldabbrev-of-header_field_info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50444-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to have braces for abbreviated field names. For example, let's say I have an array of structures like the following:</p><pre><code>typedef struct _person { int height; int age; } person;
typedef struct _people { int number; person[10]; int dummy; } people;</code></pre><p>When I dissect the people structure, I'd like to be able to use the following filters in wireshark:</p><pre><code>&quot;people.person[0].height&quot;
&quot;people.person[1].height&quot;
...
&quot;people.person[9].height&quot;</code></pre><p>When I declare the <strong>hf_register_info</strong>, If I use brackets for the abbreviated names, Wireshark crashes.</p><p>The documentation <em>README.dissector</em> only talks about spaces:</p><pre><code>FIELDABBREV     The abbreviated name for the header field. (NO SPACES)</code></pre></div><div id="question-tags" class="tags-container tags">fields abbreviated crash</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '16, 10:16</strong></p><img src="https://secure.gravatar.com/avatar/46ef36ddea155cb13d6344c0c1731b7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_michel&#39;s gravatar image" /><p>_michel<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_michel has no accepted answers">0%</span></p></div></div><div id="comments-container-50444" class="comments-container"></div><div id="comment-tools-50444" class="comment-tools"></div><div class="clear"></div><div id="comment-50444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50448"></span>

<div id="answer-container-50448" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50448-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark does not allow that character in field abbreviations. If you're running Wireshark from the command line (on UNIX-like systems; I think on Windows you need to enable console or something) you'd see Wireshark's complaint which would look like:</p><pre><code>Invalid character &#39;[&#39; in filter name &#39;&lt;your abbrevation&gt;&#39;</code></pre><p>The doc you quoted is incomplete: the allowed characters are alphanumerics, '-', '_', and '." (see the <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/proto.c;h=696831f7c03575ad8c8a8ab9375f5e68ea4242bd;hb=HEAD#l6763">proto.c source</a>). I'll try to push a change to fix that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '16, 13:21</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-50448" class="comments-container"><span id="50449"></span><div id="comment-50449" class="comment"><div id="post-50449-score" class="comment-score"></div><div class="comment-text"><p>Submitted the documentation <a href="https://code.wireshark.org/review/14107">change</a>.</p></div><div id="comment-50449-info" class="comment-info"><span class="comment-age">(23 Feb '16, 14:24)</span> JeffMorriss ♦</div></div><span id="50456"></span><div id="comment-50456" class="comment"><div id="post-50456-score" class="comment-score"></div><div class="comment-text"><p>OK, I'm quite new to Wireshark so I trusted the documentation with my life ! :D</p></div><div id="comment-50456-info" class="comment-info"><span class="comment-age">(23 Feb '16, 23:46)</span> _michel</div></div><span id="50524"></span><div id="comment-50524" class="comment"><div id="post-50524-score" class="comment-score"></div><div class="comment-text"><blockquote><p>OK, I'm quite new to Wireshark so I trusted the documentation with my life ! :D</p></blockquote><p>Don't do that. :-) If you're going to trust something with your life, use the <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=tree">source</a>, Luke. :-)</p></div><div id="comment-50524-info" class="comment-info"><span class="comment-age">(25 Feb '16, 16:13)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-50448" class="comment-tools"></div><div class="clear"></div><div id="comment-50448-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50450"></span>

<div id="answer-container-50450" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50450-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'd like to be able to use the following filters in wireshark</p></blockquote><p>The right way to do that would be to have Wireshark support the notion of a field being an array; you might want to submit an enhancement request on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a> .</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '16, 15:10</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-50450" class="comments-container"><span id="50452"></span><div id="comment-50452" class="comment"><div id="post-50452-score" class="comment-score"></div><div class="comment-text"><p>Well, before going that route, is there really a need to know that people.person[1].height has a particular value? Typically in this type of scenario Wireshark would have one field: people.person.height. But it would have multiple instances of that field in a given PDU (in your case, up to 10 of them).</p><p>IOW, do you need to be able to use a filter that says that person #1 has height of X (as opposed to a filter that asks if <em>any</em> person has a height of X)?</p></div><div id="comment-50452-info" class="comment-info"><span class="comment-age">(23 Feb '16, 16:44)</span> JeffMorriss ♦</div></div><span id="50457"></span><div id="comment-50457" class="comment"><div id="post-50457-score" class="comment-score"></div><div class="comment-text"><p>can you give an example of the filter <em>"that asks if any person has a height of X"</em> ?</p></div><div id="comment-50457-info" class="comment-info"><span class="comment-age">(23 Feb '16, 23:47)</span> _michel</div></div><span id="50458"></span><div id="comment-50458" class="comment"><div id="post-50458-score" class="comment-score"></div><div class="comment-text"><p><code>people.person.height == X</code></p></div><div id="comment-50458-info" class="comment-info"><span class="comment-age">(24 Feb '16, 00:04)</span> Guy Harris ♦♦</div></div><span id="50459"></span><div id="comment-50459" class="comment"><div id="post-50459-score" class="comment-score"></div><div class="comment-text"><p>oh ok, ... but nope :D I'm interested in being able to filter each field individually. I am also interested in plotting specific numeric fields against time (or against another field), but I guess it's not available right now. I think this could be a great feature. Imagine that you are monitoring a (or many) motors controller and this/these controller/s send periodically/or not a timestamp and rotation speed over the network. Wouldn't be great to have graphs for this ? But well, this is another subject.</p></div><div id="comment-50459-info" class="comment-info"><span class="comment-age">(24 Feb '16, 01:06)</span> _michel</div></div><span id="50523"></span><div id="comment-50523" class="comment"><div id="post-50523-score" class="comment-score"></div><div class="comment-text"><p>For completeness (I know it's obvious but...) today this is done by creating 10 filters per object (person): <code>people.person0.height</code>, etc. The enhancement Guy suggests would (possibly significantly) reduce this number.</p></div><div id="comment-50523-info" class="comment-info"><span class="comment-age">(25 Feb '16, 16:11)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-50450" class="comment-tools"></div><div class="clear"></div><div id="comment-50450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

