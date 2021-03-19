+++
type = "question"
title = "tap functions in Lua script"
description = '''Hi. I want to ask about the tap.packet functions. I have two listeners one for outbound traffic and the other for the inbound. Unfortunately, the examples of using Lua with wireshark are limited and I didn&#x27;t find documentation talks about the scope of tap functions and why they are written like that...'''
date = "2012-12-05T11:01:00Z"
lastmod = "2012-12-05T19:13:00Z"
weight = 16604
keywords = [ "lua", "tap" ]
aliases = [ "/questions/16604" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [tap functions in Lua script](/questions/16604/tap-functions-in-lua-script)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16604-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I want to ask about the tap.packet functions. I have two listeners one for outbound traffic and the other for the inbound. Unfortunately, the examples of using Lua with wireshark are limited and I didn't find documentation talks about the scope of tap functions and why they are written like that; I mean the use of local init_listener()function or any other function the script start with, and why it is local and functions like: tap.packet and tap.draw as example are global inside these functions, does this mean something I should care about ? I tried to process online data using directly the tap.packet function without inserting it inside a local function as the examples I saw, <em>is it just as convention or it has an effect on the performance of the program in some views</em>? What is the benefit of writing the lua program with wireshark like this?? and I need any advice about using two listeners if there are any points I should care about, especially when I use data from one of the tap.packet function to be benefited from by the other tap.packet functions, Is there any advice about these listeners? Thanks alot.</p></div><div id="question-tags" class="tags-container tags">lua tap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '12, 11:01</strong></p><img src="https://secure.gravatar.com/avatar/912ebc145cb38ec3da99be6003d7d9b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leena&#39;s gravatar image" /><p>Leena<br />
<span class="score" title="51 reputation points">51</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leena has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Dec '12, 19:26</p></div></div><div id="comments-container-16604" class="comments-container"><span id="16609"></span><div id="comment-16609" class="comment"><div id="post-16609-score" class="comment-score"></div><div class="comment-text"><p>Is it enough and safe to use the tap functions and functions use their outputs inside a "do..end" since I'm working online, without putting them inside a local function and call it at the end of the script??</p></div><div id="comment-16609-info" class="comment-info"><span class="comment-age">(05 Dec '12, 11:48)</span> Leena</div></div></div><div id="comment-tools-16604" class="comment-tools"></div><div class="clear"></div><div id="comment-16604-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16619"></span>

<div id="answer-container-16619" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16619-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are several reasons to prefer <code>local</code> scope over <code>global</code> scope, including a performance improvement of the variable lookup. Locals are referenced via registers on the stack while globals are stored in a table [on the heap] (applies only to Lua 5.1 -- which is the currently supported version in Wireshark). Read up on more reasons <a href="http://lua-users.org/wiki/LocalsVsGlobals">here</a>.</p><p>In addition, <code>globals</code> should be avoided for the same reasons in most other languages (one of which is that it's normally easier to maintain). Google/StackOverflow will fill you in on that.</p><p>The tap definitions don't <em>need</em> to be <code>local</code>, but if it's run in an environment where other scripts are also run, then you want to limit your variable scopes to avoid name collisions (where another script that is also using globals inadvertently overwrites your global of the same name, or vice-versa). I recommend using <code>local</code> as much as possible.</p><p>A <code>do..end</code> block creates an isolated scope where variables can live (<code>local</code>s within the block are not seen outside the block). When used with <code>local</code>s, the <code>do..end</code> block is useful to prevent colliding with variables in an outer scope with the same name. Note that you can still [accidentally] declare/overwrite globals from within a <code>do..end</code>.</p><pre><code>local i = 10
local j = 22
do
     print(i) -- &quot;10&quot;
     i = 1
     local j = 5
     k = &quot;hello&quot; -- declare global string
end
print(i) -- &quot;1&quot;
print(j) -- &quot;22&quot;
print(k) -- &quot;hello&quot;</code></pre><p>In the Lua example (from the <a href="http://wiki.wireshark.org/Lua/Examples">Wiki</a>), <code>tap.packet</code> is <strong>not</strong> a global function. That happens to be the syntax in Lua to declare a <strong>function member</strong>. In this case, it's declaring a function member named <code>packet</code> for <code>tap</code> (a <code>local</code> variable). Since the function member can only be accessed through the parent object (<code>tap</code>), the function member effectively has the same scope as the parent (<code>local</code> in this case).</p><p>Note that it's a syntax error to write:</p><pre><code>local function tap.packet()
    -- ...
end</code></pre><p>(but the <code>local</code> declaration actually doesn't make sense here).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '12, 19:13</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-16619" class="comments-container"><span id="16620"></span><div id="comment-16620" class="comment"><div id="post-16620-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot helloworld, you really helped, May God bless you.</p></div><div id="comment-16620-info" class="comment-info"><span class="comment-age">(05 Dec '12, 21:31)</span> Leena</div></div><span id="16623"></span><div id="comment-16623" class="comment"><div id="post-16623-score" class="comment-score"></div><div class="comment-text"><p>Can I skip the step of making a function contains all the funcions inside like init_Listener() and just write the functions inside the "do..end" and declare the tap as a local inside the "do..end", I want to know exactly what is the job of this main function since "do..end" wrap the variables, is it just the style of writing a program or there is a benefit from programming view??</p></div><div id="comment-16623-info" class="comment-info"><span class="comment-age">(05 Dec '12, 21:37)</span> Leena</div></div><span id="16664"></span><div id="comment-16664" class="comment"><div id="post-16664-score" class="comment-score">1</div><div class="comment-text"><p>Yes, you can declare your tap outside of a function. It really comes down to your specific requirements and what works best for you.</p></div><div id="comment-16664-info" class="comment-info"><span class="comment-age">(06 Dec '12, 17:52)</span> helloworld</div></div><span id="16666"></span><div id="comment-16666" class="comment"><div id="post-16666-score" class="comment-score">1</div><div class="comment-text"><p>Declaring your tap inside a function doesn't look very useful, especially in the Wiki example, but there are some advantages to this:</p><ul><li>It limits the scope of <code>tap</code> since nobody else in the script should care about it, and thus provides for better modularity (which is a best practice -- not a requirement).</li><li>You can call this tap-creating function multiple times, each call creating a new instance of the tap or a variation of the tap, based on some passed-in parameter (such as a filter string).</li></ul></div><div id="comment-16666-info" class="comment-info"><span class="comment-age">(06 Dec '12, 17:53)</span> helloworld</div></div><span id="16667"></span><div id="comment-16667" class="comment"><div id="post-16667-score" class="comment-score">1</div><div class="comment-text"><ul><li>The function allows you to abstract the [gory] details of setting up a tap, and listening for specific fields, etc.</li></ul></div><div id="comment-16667-info" class="comment-info"><span class="comment-age">(06 Dec '12, 17:53)</span> helloworld</div></div><span id="16668"></span><div id="comment-16668" class="comment not_top_scorer"><div id="post-16668-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot.Your explanation is clear and rich.</p></div><div id="comment-16668-info" class="comment-info"><span class="comment-age">(06 Dec '12, 19:10)</span> Leena</div></div></div><div id="comment-tools-16619" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-16619-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

