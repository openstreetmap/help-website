+++
type = "question"
title = "How do I trigger an alert on specific frame captured during live scan?"
description = '''Hello, I&#x27;m new here. I&#x27;ve been using wireshark more and more recently to help with diagnose industrial automation protocol issues.  Currently, I&#x27;m running dumpcamp on a ring keeping 30days worth of data in 50M files. What I really need to do is find a way to trigger a notification if a certain type ...'''
date = "2017-03-29T09:31:00Z"
lastmod = "2017-03-30T14:56:00Z"
weight = 60412
keywords = [ "trigger", "lua", "script", "alert", "profinet" ]
aliases = [ "/questions/60412" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I trigger an alert on specific frame captured during live scan?](/questions/60412/how-do-i-trigger-an-alert-on-specific-frame-captured-during-live-scan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60412-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm new here. I've been using wireshark more and more recently to help with diagnose industrial automation protocol issues.</p><p>Currently, I'm running dumpcamp on a ring keeping 30days worth of data in 50M files. What I really need to do is find a way to trigger a notification if a certain type of packet is found during the live scan. This specific network is using Profinet. I'm looking for a precursor that tends to indicate the network is having issues. I find these precursor events with the PN_DCP filter in Wireshark.</p><p>How could I use some variation of the script above to alert upon seeing one of these frames? Would it be possible to create some sort of counter to indicate the amount of times a pn_dcp frame has been seen? Of course, I don't want to really launch notepad, but some other application that could be used as an alert to the problem. I tried run this script, but it doesn't seem to work. Am I doing something wrong?</p><pre><code>    -- use display-filter syntax here
local _filter = &#39;(pn_dcp) &#39;

-- command to be executed for each packet
local _cmd = &#39;start C:\Users\Shawn\Desktop\test.bat&#39;
local _run = io.popen

local function make_tap(filter)
    local tap = Listener.new(nil, filter)

    function tap.packet()
        _run(_cmd)
    end

    return tap
end

-- If not running from Wireshark, enable the tap immediately, then
-- abort, or else we&#39;ll get an error below for trying to do GUI 
-- stuff from the command line.
if not gui_enabled() then
    make_tap(_filter)
    return
end

local function make_win()
    local tap = nil
    local win = TextWindow.new(&quot;Watcher&quot;)

    local function remove_tap()
    if tap then tap:remove() end
        tap = nil
    end

    win:set(&quot;Press Start to begin watching&quot;)
    win:set_atclose(remove_tap)

    win:add_button(&quot;Start&quot;, function()
        if tap then
            report_failure(&quot;Already started&quot;)
            return
        end

        win:set(&quot;Watching for:\\n&quot; .. _filter)
        tap = make_tap(_filter)
    end)

    win:add_button(&quot;Stop&quot;, function()
        if not tap then
            report_failure(&quot;Not started&quot;)
            return
        end

        remove_tap()
        win:set(&quot;Press Start to begin watching&quot;)
    end)

    return win
end

register_menu(&quot;Lua/Test&quot;, make_win, MENU_TOOLS_UNSORTED or 8)</code></pre><p>The test.bat file is the following:</p><pre><code>    @echo off
:: Ghost typer
setlocal enableextensions enabledelayedexpansion

set lines=6

set &quot;line1=A re-establishment of&quot;
set &quot;line2=communications has been&quot;
set &quot;line3=detected by Wireshark.&quot;
set &quot;line4=Please check the trace&quot;
set &quot;line5=files for any problems.&quot;
set &quot;line6=Use the filter &#39;pn_dcp&#39;&quot;

for /f %%a in (&#39;&quot;prompt $H&amp;for %%b in (1) do rem&quot;&#39;) do set &quot;BS=%%a&quot;

for /L %%a in (1,1,%lines%) do set num=0&amp;set &quot;line=!line%%a!&quot;&amp;call :type

pause&gt;nul
goto :EOF

:type
set &quot;letter=!line:~%num%,1!&quot;
set &quot;delay=%random%%random%%random%%random%%random%%random%%random%&quot;
set &quot;delay=%delay:~-6%&quot;
if not &quot;%letter%&quot;==&quot;&quot; set /p &quot;=a%bs%%letter%&quot; &lt;nul

:: adjust the 3 in the line below: higher is faster typing speed

for /L %%b in (1,5,%delay%) do rem
if &quot;%letter%&quot;==&quot;&quot; echo.&amp;goto :EOF
set /a num+=1
goto :type</code></pre><p>Any help you may be able to offer would be greatly appreciated!</p></div><div id="question-tags" class="tags-container tags">trigger lua script alert profinet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '17, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/227017211e0730ebab8facb3b68278a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="profiteam&#39;s gravatar image" /><p>profiteam<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="profiteam has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Mar '17, 10:11</p></div></div><div id="comments-container-60412" class="comments-container"><span id="60441"></span><div id="comment-60441" class="comment"><div id="post-60441-score" class="comment-score"></div><div class="comment-text"><p>If you can figure out how to convert the "pn_dcp" display filter into a capture filter, then you might be able to make use of the <code>dumpcap.bat</code> file available for download on the Wireshark <a href="https://wiki.wireshark.org/Tools">Tools</a> wiki page. The batch file uses mailsend to send an e-mail notification when a particular event occurs (or when a certain number of those events occur). It does not work with display filters though, only capture filters.</p></div><div id="comment-60441-info" class="comment-info"><span class="comment-age">(30 Mar '17, 07:12)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-60412" class="comment-tools"></div><div class="clear"></div><div id="comment-60412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60457"></span>

<div id="answer-container-60457" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60457-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Alerting is usually best done with a deep packet inspection tool, e.g. an IDS. You can use <a href="https://snort.org/">Snort</a> or <a href="https://suricata-ids.org/">Suricata</a> to create a rule that triggers an alert an whatever pattern you need to look for. In your situation I'd probably go and install a capture PC with the <a href="https://securityonion.net/">SecurityOnion</a> live distribution, which can capture full packet data while also matching Snort rules. That way you can check alerts for your custom pattern and then grab the relevant packets from the PCAPs. The only problem would be to define the pattern you are looking for, but depending on how complex it is, a Snort filter is probably not that hard to create.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '17, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-60457" class="comments-container"></div><div id="comment-tools-60457" class="comment-tools"></div><div class="clear"></div><div id="comment-60457-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

