+++
type = "question"
title = "Merkaartor v0.18 Crashes on Mac 10.7.4"
description = '''Merkaartor v0.18 crashes on my MacMini running OS 10.7.4 as soon as it tries to contact OSM servers. For example:    If I try to download map data,  Merkaartor instantly crashes.   If I try to enter my OSM user name  and password into Merkaartor&#x27;s  preferences, it instantly crashes.   I mailed crash...'''
date = "2012-06-10T01:20:00Z"
lastmod = "2012-06-12T23:59:00Z"
weight = 13394
keywords = [ "merkaartor", "crash", "mac" ]
aliases = [ "/questions/13394" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Merkaartor v0.18 Crashes on Mac 10.7.4](/questions/13394/merkaartor-v018-crashes-on-mac-1074)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13394-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Merkaartor v0.18 crashes on my MacMini running OS 10.7.4 as soon as it tries to contact OSM servers. For example:</p>
<ul>
<li><p>If I try to download map data, Merkaartor instantly crashes.</p></li>
<li><p>If I try to enter my OSM user name and password into Merkaartor's preferences, it instantly crashes.</p></li>
</ul>
<p>I mailed crash logs to the developer, but he seemed uninterested in dealing with the issue.</p>
<p>I have no problem with JOSM or Potlatch.</p>
<p>Since this seems to be a problem exclusive with me, it must be something with my machine.</p>
<p>Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-merkaartor" rel="tag" title="see questions tagged &#39;merkaartor&#39;">merkaartor</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jun '12, 01:20</strong></p>
<img src="https://secure.gravatar.com/avatar/4b379e6b8654d3932e9d74e80a630c48?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Buadhai&#39;s gravatar image" />
<p><span>Buadhai</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Buadhai has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jun '12, 10:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-13394" class="comments-container">
<span id="13412"></span>
<div id="comment-13412" class="comment">
<div id="post-13412-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm not sure how many OSM users have psychic powers, but without them we're unlikely to know how exactly Merkaartor crashes on your Mac. Could you perhaps post a little more information - does the program just exit, does it display an error message, or something else?</p>
</div>
<div id="comment-13412-info" class="comment-info">
<span class="comment-age">(10 Jun '12, 18:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="13418"></span>
<div id="comment-13418" class="comment">
<div id="post-13418-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No error message. The program simply exits, but the OS does display as a Problem Report the crash log which starts out like this:</p>
<blockquote>
<p>Crashed Thread: 0 Dispatch queue: com.apple.main-thread</p>
<p>Exception Type: EXC_BREAKPOINT (SIGTRAP) Exception Codes: 0x0000000000000002, 0x0000000000000000</p>
<p>Application Specific Information:</p>
<p>objc[47884]: garbage collection is OFF</p>
<p>Dyld Error Message: Symbol not found: _EVP_idea_cbc</p>
<p>Referenced from: /usr/local/lib/libssl.0.9.8.dylib</p>
<p>Expected in: /usr/lib/libcrypto.0.9.8.dylib</p>
</blockquote>
<p>Entire crash log is here: <a href="http://pastebin.com/ncim3EZ9">Pastebin Merkaartor Crash Log</a></p>
</div>
<div id="comment-13418-info" class="comment-info">
<span class="comment-age">(10 Jun '12, 23:21)</span> <span class="comment-user userinfo">Buadhai</span>
</div>
</div>
</div>
<div id="comment-tools-13394" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13394-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13419"></span>

<div id="answer-container-13419" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13419-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-13419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Buadhai has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks to be a generic OS X problem referenced here:</p>
<ul>
<li><a href="http://musescore.org/en/node/16030">http://musescore.org/en/node/16030</a></li>
<li><a href="http://fritzing.org/forum/thread/332/">http://fritzing.org/forum/thread/332/</a></li>
</ul>
<p>Suggest you follow the advice there to fix libssl.0.9.8.dylib and see if that works better.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jun '12, 08:46</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-13419" class="comments-container">
<span id="13443"></span>
<div id="comment-13443" class="comment">
<div id="post-13443-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. On the road now so no chance to check until tomorrow.</p>
<p>Odd that the developer was unaware of this and no mention on the Merkaartor web site.</p>
</div>
<div id="comment-13443-info" class="comment-info">
<span class="comment-age">(12 Jun '12, 05:22)</span> <span class="comment-user userinfo">Buadhai</span>
</div>
</div>
<span id="13444"></span>
<div id="comment-13444" class="comment">
<div id="post-13444-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Logged in remotely and now I see the problem. Looks like a typo in the symlink:</p>
<p>lrwxr-xr-x 1 root wheel 32 Sep 13 2011 libssl.dylib -&gt; /usr/local/liblibssl.0.9.8.dylib</p>
<p>Easy to fix. Many thanks.</p>
</div>
<div id="comment-13444-info" class="comment-info">
<span class="comment-age">(12 Jun '12, 05:33)</span> <span class="comment-user userinfo">Buadhai</span>
</div>
</div>
</div>
<div id="comment-tools-13419" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13419-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13454"></span>

<div id="answer-container-13454" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13454-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Apparently it's not easy for me to fix. Too dumb, I guess.</p>
<p>In what directory should the symlink libssl.dylib be and to what file should it point?</p>
<p>Now I have this, but I get the same crash</p>
<pre><code>bleach:lib boss$ pwd
/usr/lib
bleach:lib boss$ ls -la libss*
-rwxr-xr-x  1 root  wheel  428848 Jan 28 14:02 libssl.0.9.7.dylib
-rwxr-xr-x  1 root  wheel  614832 Jan 28 14:02 libssl.0.9.8.dylib
lrwxr-xr-x  1 root  wheel      18 Jan 28 14:03 libssl.dylib -&gt; libssl.0.9.8.dylib
bleach:lib boss$ cd /usr/local/lib
bleach:lib boss$ pwd
/usr/local/lib
bleach:lib boss$ ls -la libss*
-r-xr-xr-x@ 1 root  wheel  604608 Mar  6  2010 libssl.0.9.8.dylib
lrwxr-xr-x  1 root  wheel      27 Jun 12 17:30 libssl.dylib -&gt; /usr/lib/libssl.0.9.8.dylib</code></pre>
<p>I assumed that the March 2010 version of libssl.0.9.8.dylib was out of date, so I pointed both symlinks to the Jan 2012 version which is in /usr/lib</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jun '12, 11:36</strong></p>
<img src="https://secure.gravatar.com/avatar/4b379e6b8654d3932e9d74e80a630c48?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Buadhai&#39;s gravatar image" />
<p><span>Buadhai</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Buadhai has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13454" class="comments-container">
<span id="13480"></span>
<div id="comment-13480" class="comment">
<div id="post-13480-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I finally got it. The key was to remove this file:</p>
<p>/usr/local/lib/libssl.0.9.8.dylib (the March 6, 2010 version).</p>
<p>For reasons I don't understand it was not enough to simply fix the symlink.</p>
</div>
<div id="comment-13480-info" class="comment-info">
<span class="comment-age">(12 Jun '12, 23:59)</span> <span class="comment-user userinfo">Buadhai</span>
</div>
</div>
</div>
<div id="comment-tools-13454" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13454-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

