+++
type = "question"
title = "1.6.1 Display filter Expression Dialog Box Error and solution :-)"
description = '''Hello there, I&#x27;m glad to say that I &#x27;ve come up with a small contribution to Wireshark. Display Filter dialog box is created each time whenever the Expression button in the filter tool bar is pressed. Likewise it can create n times for n clicks.'''
date = "2011-10-18T22:09:00Z"
lastmod = "2011-10-20T01:17:00Z"
weight = 6978
keywords = [ "filter", "display-filter" ]
aliases = [ "/questions/6978" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [1.6.1 Display filter Expression Dialog Box Error and solution :-)](/questions/6978/161-display-filter-expression-dialog-box-error-and-solution-)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6978-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello there,</p><p>I'm glad to say that I 've come up with a small contribution to Wireshark. Display Filter dialog box is created each time whenever the Expression button in the filter tool bar is pressed. Likewise it can create n times for n clicks.</p></div><div id="question-tags" class="tags-container tags">filter display-filter</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '11, 22:09</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p>Terrestrial ...<br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Oct '11, 22:15</p></div></div><div id="comments-container-6978" class="comments-container"></div><div id="comment-tools-6978" class="comment-tools"></div><div class="clear"></div><div id="comment-6978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6979"></span>

<div id="answer-container-6979" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6979-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>//global section</p><p>static GtkWidget *window= NULL;</p><p>..........</p><p>..........</p><p>..........</p><pre><code>GtkWidget *</code></pre><p>dfilter_expr_dlg_new(GtkWidget *filter_te) { if (window != NULL) {</p><pre><code>    /* There&#39;s already an &quot;Expression&quot; dialog box; reactivate it. */
    reactivate_window(window);
    return window;
}
else
{ 
       //keep the code that is present inside dfilter_expr_dlg_new function in this else part
    }
}</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '11, 22:14</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p>Terrestrial ...<br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Oct '11, 22:22</p></div></div><div id="comments-container-6979" class="comments-container"></div><div id="comment-tools-6979" class="comment-tools"></div><div class="clear"></div><div id="comment-6979-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7005"></span>

<div id="answer-container-7005" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7005-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The way to contribute code to wireshark is to create a "bug"-report on <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/</a> and attach the output of "svn diff". This way we don't lose track of all submissions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '11, 01:17</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7005" class="comments-container"><span id="7007"></span><div id="comment-7007" class="comment"><div id="post-7007-score" class="comment-score"></div><div class="comment-text"><p>Thanks :-) bug 6472.</p></div><div id="comment-7007-info" class="comment-info"><span class="comment-age">(20 Oct '11, 02:22)</span> Terrestrial ...</div></div></div><div id="comment-tools-7005" class="comment-tools"></div><div class="clear"></div><div id="comment-7005-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

