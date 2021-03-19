+++
type = "question"
title = "Run a C DLL from LUA in Wireshark"
description = '''I was wondering if it would be possible to run a C dll from LUA in wireshark. Let me explain. I already have the code in C that can take a string of the data that comes over the network and returns a string in XML. I would like to write a LUA script that takes that XML string returned by the C DLL a...'''
date = "2011-07-05T09:58:00Z"
lastmod = "2011-09-07T07:43:00Z"
weight = 4909
keywords = [ "cpp", "lua", "c", "c++", "dll" ]
aliases = [ "/questions/4909" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Run a C DLL from LUA in Wireshark](/questions/4909/run-a-c-dll-from-lua-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4909-score" class="post-score" title="current number of votes">0</div><span id="post-4909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was wondering if it would be possible to run a C dll from LUA in wireshark. Let me explain.</p><p>I already have the code in C that can take a string of the data that comes over the network and returns a string in XML.</p><p>I would like to write a LUA script that takes that XML string returned by the C DLL and translate it directly to the tree structure in Wireshark.</p><p>I know it is possible to run C DLLs in LUA, but is it possible to do that using LUA in Wireshark?</p><p>Are there any premade LUA scripts out there that will take an XML string and convert it directly to the Tree View in wireshark?</p><p>Are there any resources you can point me to that do just this?</p><p>I realize this is probably not the prefered way to acomplish my task, but it seems like it is probably the easiest solution since I know nothing about LUA or Wireshark. This task is for work, and due to the nature of the client I cannot reveal any specifics or source code.</p><p>Thank you for your time, Brandon</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cpp" rel="tag" title="see questions tagged &#39;cpp&#39;">cpp</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-c" rel="tag" title="see questions tagged &#39;c&#39;">c</span> <span class="post-tag tag-link-c++" rel="tag" title="see questions tagged &#39;c++&#39;">c++</span> <span class="post-tag tag-link-dll" rel="tag" title="see questions tagged &#39;dll&#39;">dll</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '11, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/b65eb296474b8a4c664c8f7bc0ba2234?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="officialhopsof&#39;s gravatar image" /><p><span>officialhopsof</span><br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="officialhopsof has 2 accepted answers">100%</span></p></div></div><div id="comments-container-4909" class="comments-container"><span id="6184"></span><div id="comment-6184" class="comment"><div id="post-6184-score" class="comment-score"></div><div class="comment-text"><p>@officialhopsof - Can you post the code you use to run the C DLL in Lua?</p></div><div id="comment-6184-info" class="comment-info"><span class="comment-age">(07 Sep '11, 07:18)</span> <span class="comment-user userinfo">SwDevMan81</span></div></div></div><div id="comment-tools-4909" class="comment-tools"></div><div class="clear"></div><div id="comment-4909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6187"></span>

<div id="answer-container-6187" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6187-score" class="post-score" title="current number of votes">1</div><span id="post-6187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>One way will be to create a wrapper for your dll --either by making a separate dll which makes calls into your current one, or by adding a Lua interface to your current library. I have successfully created a Lua-based dissector using this method, so the idea is sound. You will need the following --at a minimum --in your dll to expose functionality to Lua:</p><pre><code>#define LUA_LIB /* Do this early. Preferably first */
#include &lt;lua.h&gt;
#include &lt;lualib.h&gt;
#include &lt;lauxlib.h&gt; /* You may be able to get away without this one */
/* Forward declare your Lua-exposed functions as so*/
static int your_function(lua_State *L);

static const luaL_reg your_libnamelib[] = /* You could call this anything you want */
{
    {&quot;your_functions_lua_name&quot;, your_function},
    {NULL, NULL}
}

LUALIB_API int luaopen_your_libname(lua_State *L)
{
    luaL_register(L, &quot;your_libname&quot;, your_libnamelib);
    return 1;
}

static int your_function(lua_State *L)
{
    /* Do your work/call other C functions, etc. */
    return 0; /* return the number of items returned to Lua */
}</code></pre><p>You can find more information in <a href="http://www.lua.org/pil/24.html" title="24 - An Overview of the C API">Programming in Lua</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '11, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-6187" class="comments-container"></div><div id="comment-tools-6187" class="comment-tools"></div><div class="clear"></div><div id="comment-6187-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

