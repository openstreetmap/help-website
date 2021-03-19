+++
type = "question"
title = "g_close not being recognized as available function in plugin dissector"
description = '''I&#x27;m writing a plugin dissector that upon initialization reads a file with a 64bit key and a string to be stored in a hash table. This gets used to identify messages. I&#x27;ve written code in the dissector that uses g_close and strtoll to close the file and read the 64 bit key. The code has the following...'''
date = "2013-08-29T14:21:00Z"
lastmod = "2013-08-29T16:05:00Z"
weight = 24176
keywords = [ "glib", "dissector", "plugin" ]
aliases = [ "/questions/24176" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [g\_close not being recognized as available function in plugin dissector](/questions/24176/g_close-not-being-recognized-as-available-function-in-plugin-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24176-score" class="post-score" title="current number of votes">0</div><span id="post-24176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing a plugin dissector that upon initialization reads a file with a 64bit key and a string to be stored in a hash table. This gets used to identify messages.</p><p>I've written code in the dissector that uses g_close and strtoll to close the file and read the 64 bit key. The code has the following includes.</p><pre><code>#include &lt;glib.h&gt;
#include &lt;glib/gstdio.h&gt;</code></pre><p>I'm getting the build error message warning C4013: 'g_close' undefined; assuming extern returning int</p><p>As well as the following linker error</p><p>tomato.obj : error LNK2019: unresolved external symbol _g_close referenced in function _loadTheOM</p><p>Tomato_v1.0.0-603_ws1_8.dll : fatal error LNK1120: 1 unresolved externals</p><p>The error leads me to believe that I'm not including the correct files. But the <a href="https://developer.gnome.org/glib/stable/glib-File-Utilities.html#g-close">GLib reference</a> leads me to believe that I'm including the correct file. Other glib functions such as g_ascii_strtoll seem to build and link correctly.<br />
</p><p>I'm on Win7 and use VS2010. Is there some sort of Makefile line I need to edit?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-glib" rel="tag" title="see questions tagged &#39;glib&#39;">glib</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '13, 14:21</strong></p><img src="https://secure.gravatar.com/avatar/0b4ddeb095ff16e8a84fe92d03bbdef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlann&#39;s gravatar image" /><p><span>tlann</span><br />
<span class="score" title="76 reputation points">76</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlann has 4 accepted answers">100%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Aug '13, 15:08</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-24176" class="comments-container"></div><div id="comment-tools-24176" class="comment-tools"></div><div class="clear"></div><div id="comment-24176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24178"></span>

<div id="answer-container-24178" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24178-score" class="post-score" title="current number of votes">1</div><span id="post-24178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tlann has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The GLib reference, with its lack of a "since 2.<em>x</em>" item for <code>g_close()</code>, also can lead one to believe, not inappropriately, that it's available in all versions of GLib 2.x; however, a quick look at the GLib 2.34.3 source seems to indicate that it's <em>not</em> available in that version. It appears to have been introduced somewhere in the 2.35 or 2.36 version; the header file seems to say it's only available in 2.36.</p><p>I've filed <a href="https://bugzilla.gnome.org/show_bug.cgi?id=707092">bug 707092</a> in the GNOME bug database for the documentation's apparent lack of an indication of <code>g_close()</code>'s availability.</p><p>I don't know what GLib version the Wireshark Windows build process installs by default, but if it's before 2.35, and possibly even if it <em>is</em> 2.35.x, that might not make <code>g_close()</code> available.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '13, 15:52</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Aug '13, 15:59</strong> </span></p></div></div><div id="comments-container-24178" class="comments-container"><span id="24179"></span><div id="comment-24179" class="comment"><div id="post-24179-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your help and editing my question. I thought the 4 spaces should of made my code display correctly. After looking at it again I guess I could of selected it and used control k.</p></div><div id="comment-24179-info" class="comment-info"><span class="comment-age">(29 Aug '13, 15:59)</span> <span class="comment-user userinfo">tlann</span></div></div><span id="24180"></span><div id="comment-24180" class="comment"><div id="post-24180-score" class="comment-score">1</div><div class="comment-text"><p>It <em>did</em> make it display correctly once I edited the question to put them in, and probably would have made it display correctly <em>once you posted your question</em>. However, <em>while I was editing it</em>, the preview display didn't show anything after <code>#include</code>, and you would have seen the same thing, which could have led you to believe that it wouldn't work when you posted the question. (As I said in my edit comment, previewing in the version of the OSQA that this site uses doesn't always work correctly; I don't know whether a later version of OSQA fixes it or not. I suspect that the server-side code that generates the formatted version of questions, comments, and answers isn't JavaScript and that the previewing code is JavaScript; if so, the previewing isn't being done by the same code that will actually generate the formatted version, so, unless the authors are careful, the two versions of the code could generate different results.)</p></div><div id="comment-24180-info" class="comment-info"><span class="comment-age">(29 Aug '13, 16:05)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-24178" class="comment-tools"></div><div class="clear"></div><div id="comment-24178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

