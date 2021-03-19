+++
type = "question"
title = "How to change lua io.output (custom log file) every 5 minutes"
description = '''Hi, I&#x27;m using tshark and lua to extract datafields from diameter protocol in endless loop and saving them into log file. It works great. But now I need to create new logfile every 5 minutes. I can change io.output inside tap.packet functions but it&#x27;s not accurate since it&#x27;s called only when there is...'''
date = "2012-12-04T08:59:00Z"
lastmod = "2012-12-06T01:02:00Z"
weight = 16550
keywords = [ "lua", "io.write", "interval", "tshark", "log" ]
aliases = [ "/questions/16550" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to change lua io.output (custom log file) every 5 minutes](/questions/16550/how-to-change-lua-iooutput-custom-log-file-every-5-minutes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16550-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16550-score" class="post-score" title="current number of votes">0</div><span id="post-16550-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm using tshark and lua to extract datafields from diameter protocol in endless loop and saving them into log file. It works great. But now I need to create new logfile every 5 minutes. I can change io.output inside tap.packet functions but it's not accurate since it's called only when there is a packet. I check <a href="http://stackoverflow.com/questions/9393693/how-to-use-a-timer-in-lua">How to use a timer in lua</a>, but I'm not able to combine it with my code. Please, can you help me? Thanks. btw To create 5min pcaps and process them it's not a option for me.</p><p>My code (very simplified):</p><pre><code>local tap = Listener.new(nil, &quot;diameter&quot;)
local sid_field = Field.new(&quot;diameter.Session-Id&quot;)
local logfile = &quot;diameter_log_&quot;..os.date(&quot;%Y%m%d%H%M%S&quot;)
io.output(logfile)

function tap.packet(pinfo, tvb)
    local sid_field_ = sid_field()
    io.write(tostring(sid_field_))
end</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-io.write" rel="tag" title="see questions tagged &#39;io.write&#39;">io.write</span> <span class="post-tag tag-link-interval" rel="tag" title="see questions tagged &#39;interval&#39;">interval</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-log" rel="tag" title="see questions tagged &#39;log&#39;">log</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '12, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/0061f9bd5384a544637692774a6e108f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lojza&#39;s gravatar image" /><p><span>lojza</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lojza has no accepted answers">0%</span></p></div></div><div id="comments-container-16550" class="comments-container"><span id="16587"></span><div id="comment-16587" class="comment"><div id="post-16587-score" class="comment-score"></div><div class="comment-text"><p>Hello everybody, thank you for your help. Let me redefine my question: <strong>Only possibility to check the time (with <code>os.clock()</code>) is when <code>tap.packet()</code> is called. Right?</strong></p><p><em>Just remark:</em> I'm running under Linux and what stated helloworld is right, but I prefer new logfile exactly every 5 minutes (even empty) rather then non-empty files randomly generated (as packets arrive)</p><p><strong><em>New idea:</em></strong> I'm thinking about definition of new "more busy" (tcp) tap and check time inside it. E.g.:</p><pre><code>local tap_busy = Listener.new(nil, &quot;tcp&quot;)
function tap_busy.packet(pinfo, tvb)
    ---- check time &amp; change io.write here ----
end</code></pre><p>But maybe it brings more trouble then benefits. Thank you :-)</p></div><div id="comment-16587-info" class="comment-info"><span class="comment-age">(05 Dec '12, 05:00)</span> <span class="comment-user userinfo">lojza</span></div></div><span id="16588"></span><div id="comment-16588" class="comment"><div id="post-16588-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Only possibility to check the time (with os.clock()) is when tap.packet() is called. Right?</p></blockquote><p>If you run on linux: Yes.<br />
If you run on Windows: No (see winapi).<br />
</p><blockquote><p>New idea: I'm thinking about definition of new "more busy" (tcp) tap and check time inside it. E.g.:</p></blockquote><p>Yes, that's possible, but as you said, it will possibly cause other problems (resource consumption).</p></div><div id="comment-16588-info" class="comment-info"><span class="comment-age">(05 Dec '12, 05:10)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="16595"></span><div id="comment-16595" class="comment"><div id="post-16595-score" class="comment-score"></div><div class="comment-text"><p>Ok. But I have to ask: how are empty files useful? If you need to track quiet time periods, there are simpler and more elegant ways of handling that (e.g., logging this fact in a file).</p><p>Your "new" idea's code snippet looks like the same idea suggested in StackOverflow (in that it just checks the time inside <code>tap.packet()</code>).</p></div><div id="comment-16595-info" class="comment-info"><span class="comment-age">(05 Dec '12, 07:44)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="16625"></span><div id="comment-16625" class="comment"><div id="post-16625-score" class="comment-score"></div><div class="comment-text"><p>It's just my approach (obsession) :-) Idea is same, but applied on tcp which occurs more frequently than diameter.</p></div><div id="comment-16625-info" class="comment-info"><span class="comment-age">(06 Dec '12, 01:02)</span> <span class="comment-user userinfo">lojza</span></div></div></div><div id="comment-tools-16550" class="comment-tools"></div><div class="clear"></div><div id="comment-16550-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16552"></span>

<div id="answer-container-16552" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16552-score" class="post-score" title="current number of votes">0</div><span id="post-16552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>as it's said in the <a href="http://stackoverflow.com/questions/9393693/how-to-use-a-timer-in-lua">stackoverflow question</a>, there are <strong>no real timers in Lua</strong> itself. So, the only way to implement it, is to call os.clock() within the tap.packet function and then change the file descriptor after 5 minutes. However: You said, that this is not accurate enough, so I guess it's not an option for you.</p><p>There is a Lua module called <strong>winapi</strong> which allows you to create a real timer in Lua, by using the Win32 API.</p><blockquote><p><code>https://github.com/stevedonovan/winapi/downloads</code><br />
<code>http://stevedonovan.github.com/winapi/examples/test-timer.lua.html</code><br />
</p></blockquote><p>The <strong>bad news</strong>: You can't use that module with Wireshark, as it's compiled with a different compiler version. And even if you compile it yourself, I'm not sure if the integration of Lua into Wireshark would allow to use that module!</p><p>So, I'm sorry, but your options are kind of limited. You could use an external program to monitor your logfile. That program runs independently of tshark and checks the log file for modifications every second. If there is a change, it will extract the delta since the last change. Now, that external tool can write a new consolidated log file at every interval you need.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '12, 13:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-16552" class="comments-container"><span id="16560"></span><div id="comment-16560" class="comment"><div id="post-16560-score" class="comment-score"></div><div class="comment-text"><p>Actually, you <em>can</em> use the <code>winapi</code> module and the <code>test-timer.lua</code> script in Wireshark/Tshark (I've confirmed with <a href="https://github.com/downloads/stevedonovan/winapi/winapi-1.4.1-51gcc.zip"><code>winapi-1.4.1-51gcc.zip</code></a>, in Windows 7, and <code>tshark</code> 1.9.0 SVN Rev 45747).</p><p>And yes, Wireshark Lua let you use practically any library as long as it's for the same version of Lua. The current Windows releases of Wireshark officially support Lua 5.1.</p></div><div id="comment-16560-info" class="comment-info"><span class="comment-age">(04 Dec '12, 17:40)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="16561"></span><div id="comment-16561" class="comment"><div id="post-16561-score" class="comment-score"></div><div class="comment-text"><p>nice! I did not test the gcc version of the library.</p><p><span></span><span>@lojza</span>: Now you have a solution. Use the test-timer.lua script as a starting point. Set a timer to 5 minutes. If the timer fires, change the file descriptor and you should get a new file every 5 minutes.</p></div><div id="comment-16561-info" class="comment-info"><span class="comment-age">(04 Dec '12, 18:21)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-16552" class="comment-tools"></div><div class="clear"></div><div id="comment-16552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16562"></span>

<div id="answer-container-16562" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16562-score" class="post-score" title="current number of votes">0</div><span id="post-16562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think a timer (or a concurrent task) is truly necessary here. If I understand correctly, you need the log to rollover every 5 minutes, but a rollover should only occur if you indeed have something to log (so checking the time in <code>tap.packet()</code> would be correct). Otherwise, you would rollover blank files if, for example, you didn't see a packet for several 5-minute periods. Let's consider an example:</p><ol><li>You don't know what time it is until you get a packet (i.e., you can only check the time (with <code>os.clock()</code>) when <code>tap.packet()</code> is called).</li><li>For exactly 5 minutes, a packet arrives every 27 seconds, which fits 11.111 periods in 5 minutes (which means you'll get 11 packets per file). On the 11th packet, the duration you calculated was still less than 5 minutes, so you don't rollover.</li><li>No packets arrive for the next 10 minutes. No rollover occurs because you need another packet to determine that you've passed the 5-minute mark.</li><li>A packet arrives. You calculate the duration to be at least 5 minutes, so you rollover to a new file.</li></ol><p>In that timespan, you have 2 useful <strong>non-empty</strong> files. So, I think the answer from StackOverflow is the right one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '12, 18:33</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span> </br></br></p></div></div><div id="comments-container-16562" class="comments-container"></div><div id="comment-tools-16562" class="comment-tools"></div><div class="clear"></div><div id="comment-16562-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

