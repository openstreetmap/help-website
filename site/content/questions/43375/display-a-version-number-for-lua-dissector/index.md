+++
type = "question"
title = "Display a version number for Lua dissector?"
description = '''Is it possible to set the version number for a Lua dissector so that is will show up in the Help | About on the Plugins page?  Is there a different mechanism that can be used for Lua dissectors? Thanks, Frank'''
date = "2015-06-19T09:00:00Z"
lastmod = "2016-05-03T15:48:00Z"
weight = 43375
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/43375" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Display a version number for Lua dissector?](/questions/43375/display-a-version-number-for-lua-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43375-score" class="post-score" title="current number of votes">0</div><span id="post-43375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to set the version number for a Lua dissector so that is will show up in the Help | About on the Plugins page?<br />
</p><p>Is there a different mechanism that can be used for Lua dissectors?</p><p>Thanks, Frank</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '15, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/1f9965ec0a514fe5b45320abd193b6a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flomby&#39;s gravatar image" /><p><span>flomby</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flomby has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-43375" class="comments-container"><span id="43615"></span><div id="comment-43615" class="comment"><div id="post-43615-score" class="comment-score"></div><div class="comment-text"><p>There is no such thing available right now (though you can make your own as izopizo points out in the answer), but it's not a bad idea to add such functionality in a future Wireshark. So I've added it to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11315">bugs.wireshark.org</a>.</p></div><div id="comment-43615-info" class="comment-info"><span class="comment-age">(27 Jun '15, 18:04)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-43375" class="comment-tools"></div><div class="clear"></div><div id="comment-43375-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52170"></span>

<div id="answer-container-52170" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52170-score" class="post-score" title="current number of votes">1</div><span id="post-52170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>example in Lua-script:</p><pre><code>local my_info = 
{
    version = &quot;1.0.1&quot;,
    author = &quot;Jane Doe&quot;,
    description = &quot;this plugin parses rainbows&quot;,
    repository = &quot;https://github.com/octocat/Spoon-Knife&quot;
}

set_plugin_info(my_info)</code></pre><p>C-code from wirshark source:</p><pre><code>WSLUA_FUNCTION wslua_set_plugin_info(lua_State* L) {
  55     /*  Set a Lua table with meta-data about the plugin, such as version.
  56 
  57         The passed-in Lua table entries need to be keyed/indexed by the following:
  58          * &quot;version&quot; with a string value identifying the plugin version (required)
  59          * &quot;description&quot; with a string value describing the plugin (optional)
  60          * &quot;author&quot; with a string value of the author&#39;s name(s) (optional)
  61          * &quot;repository&quot; with a string value of a URL to a repository (optional)
  62 
  63         Not all of the above key entries need to be in the table. The &#39;version&#39;
  64         entry is required, however. The others are not currently used for anything, but
  65         might be in the future and thus using them might be useful. Table entries keyed
  66         by other strings are ignored, and do not cause an error.</code></pre><p>Copy-pasted from: <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/wslua/wslua_util.c;h=4175c0f170fd3ed87392e0dc6a9df200803f610a;hb=23163520ad2a96aa9c22ebae8f3fcc91e93d2461">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/wslua/wslua_util.c;h=4175c0f170fd3ed87392e0dc6a9df200803f610a;hb=23163520ad2a96aa9c22ebae8f3fcc91e93d2461</a></p><p>which in turn is from: <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=23163520ad2a96aa9c22ebae8f3fcc91e93d2461">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=23163520ad2a96aa9c22ebae8f3fcc91e93d2461</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '16, 03:44</strong></p><img src="https://secure.gravatar.com/avatar/28d0f2e999fefc0514aee9223bc9fa83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KamratKalasson&#39;s gravatar image" /><p><span>KamratKalasson</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KamratKalasson has no accepted answers">0%</span></p></div></div><div id="comments-container-52170" class="comments-container"></div><div id="comment-tools-52170" class="comment-tools"></div><div class="clear"></div><div id="comment-52170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43376"></span>

<div id="answer-container-43376" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43376-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43376-score" class="post-score" title="current number of votes">0</div><span id="post-43376-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'd suggest installing and checking out cloudshark wireshark plugin (written in lua)</p><p><a href="https://support.cloudshark.org/wireshark-plugin/using-the-wireshark-plugin.html">https://support.cloudshark.org/wireshark-plugin/using-the-wireshark-plugin.html</a></p><p>And then when you have it installed have a look at their source code.</p><p>They've added their own menu, preferences settings and their own about window.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '15, 09:04</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p><span>izopizo</span><br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Jun '15, 09:04</strong> </span></p></div></div><div id="comments-container-43376" class="comments-container"><span id="52206"></span><div id="comment-52206" class="comment"><div id="post-52206-score" class="comment-score"></div><div class="comment-text"><blockquote><p>and their own about window</p></blockquote><p>But they should also do what <span>@KamratKalasson</span> suggested, so that the plugin's version number etc. show up in <em>Wireshark's</em> About window. I'll look at fixing that and making a pull request.</p></div><div id="comment-52206-info" class="comment-info"><span class="comment-age">(03 May '16, 15:48)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-43376" class="comment-tools"></div><div class="clear"></div><div id="comment-43376-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

