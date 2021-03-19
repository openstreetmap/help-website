+++
type = "question"
title = "How to calculate the difference between two NSTime values in LUA"
description = '''I&#x27;ve been writing a lua dissector and would like to display the time interval between the arrival of two different packets. I have created some NSTime variables like so: first_nstime = NSTime(pinfo.abs_ts)  I then put all of these values (from all of the packets in the capture) into a table which ge...'''
date = "2013-05-22T20:54:00Z"
lastmod = "2013-05-23T02:44:00Z"
weight = 21389
keywords = [ "nstime", "lua", "dissector" ]
aliases = [ "/questions/21389" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to calculate the difference between two NSTime values in LUA](/questions/21389/how-to-calculate-the-difference-between-two-nstime-values-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21389-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been writing a lua dissector and would like to display the time interval between the arrival of two different packets.</p><p>I have created some NSTime variables like so:</p><pre><code>first_nstime = NSTime(pinfo.abs_ts)</code></pre><p>I then put all of these values (from all of the packets in the capture) into a table which gets referenced later when I want to get the interval between the last packet and the current packet.</p><p>However, I am having some issues when calculating the difference.</p><p>I have seen many dissectors in C that use the function:</p><pre><code>nstime_delta()</code></pre><p>However, I cannot seem to call that directly in a LUA dissector.</p><p>I also noticed the following LUA function from a doc here: <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Pinfo.html">http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Pinfo.html</a></p><p>That is defined as follows:</p><pre><code>11.9.4.4. nstime:__sub()
Calculates the diff of two NSTimes</code></pre><p>But whenever I attempt to call __sub() on an NSTime object like this:</p><pre><code>NSTime(pinfo.abs_ts):__sub(first_nstime)</code></pre><p>Or like this:</p><pre><code>NSTime(pinfo.abs_ts):__sub(current_nstime, first_nstime)</code></pre><p>Or even with no arguments (like the doc states):</p><pre><code>NSTime(pinfo.abs_ts):__sub()</code></pre><p>I get an error that looks like this:</p><pre><code>A protocol doesn&#39;t have a `__sub&#39; nstime</code></pre><p>Is this function even meant to be used? Is it locally defined or something?</p><p>If this isn't the right way of getting the difference between two NSTime objects, what would that be?</p><p>I have noticed that I do have access to the nstime.secs and nstime.nsecs values of my NSTime objects, so I guess I could grab the seconds and nanoseconds of the two NSTime objects, perform some arithmetic on the regular lua numbers to get the result then use the result in the creation of a new NSTime object? That seems like a bit of a roundabout way of doing it if there are already functions defined for getting the difference.</p></div><div id="question-tags" class="tags-container tags">nstime lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '13, 20:54</strong></p><img src="https://secure.gravatar.com/avatar/7bf9d39d8f0960ce3e5dc74ba1c9a68a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ballistic%20Buddha&#39;s gravatar image" /><p>Ballistic Bu...<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ballistic Buddha has no accepted answers">0%</span></p></div></div><div id="comments-container-21389" class="comments-container"></div><div id="comment-tools-21389" class="comment-tools"></div><div class="clear"></div><div id="comment-21389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21402"></span>

<div id="answer-container-21402" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21402-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not very clueful about Lua, but based on other scripting languages (Python), the double underscore prefix usually means the method is internal to the type, aka operator overloading. I suspect the method implements the subtraction operation for the nstime type, so given two values of type nstime you should be able to simply use the subtract operator, e.g. <code>current_nstime - first_nstime</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '13, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-21402" class="comments-container"><span id="21419"></span><div id="comment-21419" class="comment"><div id="post-21419-score" class="comment-score"></div><div class="comment-text"><p>Wow, now I feel ridiculous. I can't believe I didn't just try using the - operator on the two objects.</p><p>I had a feeling that the function was defined as local given that it was prefixed with two underscores. The underscores don't always do anything in lua, but you are correct that it is usually an indication of a function used for internal use only (like a local function). However It didn't occur to me for some reason that they used the local method in the subtract operation that gets called when you use the arithmetic operators on the object.</p><p>In fact, I also learned from <a href="http://lua-users.org/wiki/MetatableEvents">here</a> today that a lua function with the name of</p><pre><code>__sub()</code></pre><p>defined for an object will always override the metamethod to implement the subtraction operation between itself and another object. Same goes for</p><pre><code>__add(), __mul(), __div(), __tostring(), etc.</code></pre><p>Cool stuff!</p><p>Thanks for the help.</p></div><div id="comment-21419-info" class="comment-info"><span class="comment-age">(23 May '13, 10:51)</span> Ballistic Bu...</div></div></div><div id="comment-tools-21402" class="comment-tools"></div><div class="clear"></div><div id="comment-21402-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

