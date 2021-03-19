+++
type = "question"
title = "Trigger an executable file once wireshark finds a &quot;keyword&quot; on live capture"
description = '''Hi, I&#x27;m setting up a trap for hackers on my server, by putting an attractive file named: &quot;source-code.zip&quot; (as an example) so only hackers can see. (If the hacker is using a PHP shell trap or something) Once the hacker trys to open or access the &quot;source-code.zip&quot; file, I need wireshark to trigger an...'''
date = "2012-03-21T09:11:00Z"
lastmod = "2012-03-22T17:53:00Z"
weight = 9682
keywords = [ "udp", "executable", "tcp", "hackers", "wireshark" ]
aliases = [ "/questions/9682" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Trigger an executable file once wireshark finds a "keyword" on live capture](/questions/9682/trigger-an-executable-file-once-wireshark-finds-a-keyword-on-live-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9682-score" class="post-score" title="current number of votes">0</div><span id="post-9682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm setting up a trap for hackers on my server, by putting an attractive file named: "source-code.zip" (as an example) so only hackers can see. (If the hacker is using a PHP shell trap or something)</p><p>Once the hacker trys to open or access the "source-code.zip" file, I need wireshark to trigger an executable file that will shut down the network card on my server to prevent any other theft, just in case.</p><p>How can I do this using wireshark or tcpdump ? is it possible ? for example using a filter where if any packet (TCP/UDP/ETC..) contains the word "source-code.zip" it should trigger an executable.</p><p>Of course the file name "source-code.zip" will be changed to someting more unique and complex.</p><p>I need your help guys, is it possible to trigger files using filters on wireshark ? It also should not slow my network or CPU usage..</p><p>Thank you. (and sorry if my english is bad)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-executable" rel="tag" title="see questions tagged &#39;executable&#39;">executable</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-hackers" rel="tag" title="see questions tagged &#39;hackers&#39;">hackers</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '12, 09:11</strong></p><img src="https://secure.gravatar.com/avatar/75fb7fa17460e5c9b3db8508fe3c6232?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="reacen&#39;s gravatar image" /><p><span>reacen</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="reacen has no accepted answers">0%</span></p></div></div><div id="comments-container-9682" class="comments-container"><span id="9703"></span><div id="comment-9703" class="comment"><div id="post-9703-score" class="comment-score"></div><div class="comment-text"><p>Please help with anything.. ? I need this so bad.</p></div><div id="comment-9703-info" class="comment-info"><span class="comment-age">(22 Mar '12, 11:56)</span> <span class="comment-user userinfo">reacen</span></div></div></div><div id="comment-tools-9682" class="comment-tools"></div><div class="clear"></div><div id="comment-9682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="9715"></span>

<div id="answer-container-9715" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9715-score" class="post-score" title="current number of votes">5</div><span id="post-9715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="reacen has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you <strong>can</strong> do this through Wireshark Lua, but as the other answers indicate, there are better ways to accomplish your goal.</p><p>If you really wanted to use Wireshark, you could create a tap/listener that runs a specified program (using <a href="http://www.lua.org/manual/5.1/manual.html#pdf-os.execute"><code>os.execute</code></a>, which runs a shell command, or <a href="http://www.lua.org/manual/5.1/manual.html#pdf-io.popen">io.popen</a>, which starts a program in a separate process...you probably want the latter) upon detecting a packet of interest.</p><p>Here's an example Lua script (based on this <a href="http://www.wireshark.org/lists/wireshark-users/201201/msg00048.html">answer</a>) that opens iTunes whenever UDP packets, containing XML, arrive at port 2000. The script is put in <code>~/.wireshark/plugins/itunes_tap.lua</code>. (Note that the script automatically loads in <code>tshark</code>)</p><pre><code>-- use display-filter syntax here
local _filter = &#39;(udp.port == 2000) &amp;&amp; xml&#39;

-- command to be executed for each packet
local _cmd = &#39;open /Applications/iTunes.app&#39;
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

register_menu(&quot;Lua/Test&quot;, make_win, MENU_TOOLS_UNSORTED or 8)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '12, 17:23</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-9715" class="comments-container"><span id="9716"></span><div id="comment-9716" class="comment"><div id="post-9716-score" class="comment-score"></div><div class="comment-text"><p>I LOVE YOU you so much, you just saved my life ! C:\Program Files\Wireshark&gt;tshark -X lua_script:c:\test.lua work's great with the wireshark filter too. I didn't know about lua ! Thank you very much sir !</p></div><div id="comment-9716-info" class="comment-info"><span class="comment-age">(22 Mar '12, 17:53)</span> <span class="comment-user userinfo">reacen</span></div></div></div><div id="comment-tools-9715" class="comment-tools"></div><div class="clear"></div><div id="comment-9715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9706"></span>

<div id="answer-container-9706" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9706-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9706-score" class="post-score" title="current number of votes">1</div><span id="post-9706-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, Wireshark does not have any facility to trigger an executable based on filters. Also, you have no guarantee that the file name would be contained in a single packet. It could, for example, be spread over two TCP segments in two different IP packets.</p><p>I'm not clear on what you're trying to do, but it doesn't seem like Wireshark is the right tool.</p><p>If you're actually trying to attract a hacker for whatever reason, then build a real honey pot that is not a production server, so that it isn't a problem if it gets destroyed. A virtual machine would be an excellent choice. You could use a snapshot to restore the machine if it was compromised in an attack.</p><p>If this is a production server that you're really trying to protect, use the tried and tested tools that are available for that purpose, instead of trying to cobble together your own system. Make sure the server has a host-based firewall, or is behind a network firewall, or both. Deploy an intrusion detection system, like Snort. Make sure that the server is properly and frequently backed up and can be restored if it does get compromised. If you can't afford commercial protective software, there are free programs available.</p><p>No matter how cleverly you name your file, you have absolutely no assurance that a hacker will go after this file first, so it will not serve as a reliable early warning of an attack.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '12, 12:51</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-9706" class="comments-container"></div><div id="comment-tools-9706" class="comment-tools"></div><div class="clear"></div><div id="comment-9706-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9707"></span>

<div id="answer-container-9707" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9707-score" class="post-score" title="current number of votes">0</div><span id="post-9707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark does not have a built-in capability to launch arbitrary external programs (if it did, it could be abused by hackers attacking a system on which they knew wireshark to run). I doubt seriously the effectiveness of your honeypot. If your server's security is critical, and you anticipate it to be compromised so easily, I would very strongly recommend a different approach to network security. Moreover, Wireshark comes with it's own list of problems, not the least of which is the known <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">out of memory</a> memory problem that would certainly cripple your security setup.<br />
Wireshark is really intended for <em>manual</em> analysis of network activity to help determine what might be wrong with the network itself. It is not a security tool, even though it sometimes helps in analyzing the network state during/after a security event.</p><p>Why not try a tool that is actually intended for catching malicious packets (<a href="http://www.snort.org/">snort</a>, for example)?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '12, 12:55</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span> </br></p></div></div><div id="comments-container-9707" class="comments-container"></div><div id="comment-tools-9707" class="comment-tools"></div><div class="clear"></div><div id="comment-9707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

