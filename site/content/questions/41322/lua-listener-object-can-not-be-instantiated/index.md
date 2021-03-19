+++
type = "question"
title = "Lua: Listener object can not be instantiated"
description = '''Hi, I am using lates wireshark together with lua 5.2 dll and ZeroBrane Master from GIT  to debug lua scripts. I have set the Path to the ZeroBrane EduKit to fix a lua socket problem with lua 5.2. After copy the lua 5.2 dll into the wireshark folder, fixing the problem with the lua path and socket er...'''
date = "2015-04-09T06:28:00Z"
lastmod = "2015-04-09T06:28:00Z"
weight = 41322
keywords = [ "listener", "lua", "debug" ]
aliases = [ "/questions/41322" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua: Listener object can not be instantiated](/questions/41322/lua-listener-object-can-not-be-instantiated)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41322-score" class="post-score" title="current number of votes">0</div><span id="post-41322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am using lates wireshark together with lua 5.2 dll and ZeroBrane Master from GIT to debug lua scripts.</p><p>I have set the Path to the ZeroBrane EduKit to fix a lua socket problem with lua 5.2.</p><p>After copy the lua 5.2 dll into the wireshark folder, fixing the problem with the lua path and socket error I was able to start the script and debug. However the Listener object is not instantiated. The watch expression shows: Listener = "bad argument #1 to ? (userdata expected, got table)" I assume that is related to version missmatch between lua 5.2 dll and debugger mobdeug but I an not able to find a working setup.</p><p>Anyone have had the same problem and was able to fix it?</p><p>A Zip or portable with running wireshark, lua and ZeroBrane to debug lua scripts for wireshark would be very appreciated.</p><p>Thank you,</p><p>Markus</p><p>Code:</p><pre><code>_G.debug = require(&quot;debug&quot;)
require(&quot;mobdebug&quot;).start()

local function menuable_tap()
    -- Declare the window we will use
    local tw = TextWindow.new(&quot;Address Counter&quot;)

    -- This will contain a hash of counters of appearances of a certain address
    local ips = {}

    -- this is our tap
    local tap = Listener.new(nil, &quot;ip&quot;)

    function remove()
            -- this way we remove the listener that otherwise will remain running indefinitely
            tap:remove()
    end

    -- we tell the window to call the remove() function when closed
    tw:set_atclose(remove)

    -- this function will be called once for each packet
    function tap.packet(pinfo,tvb)
            local src = ips[tostring(pinfo.src)] or 0
            local dst = ips[tostring(pinfo.dst)] or 0
            ips[tostring(pinfo.src)] = src + 1
            ips[tostring(pinfo.dst)] = dst + 1
    end

    -- this function will be called once every few seconds to update our window
    function tap.draw(t)
            tw:clear()
            for ip,num in pairs(ips) do
                    tw:append(ip .. &quot;\t&quot; .. num .. &quot;\n&quot;);
            end
    end

    -- this function will be called whenever a reset is needed
    -- e.g. when reloading the capture file
    function tap.reset()
            tw:clear()
            ips = {}
    end
end

-- using this function we register our function
-- to be called when the user selects the Tools-&gt;Test-&gt;Packets menu
register_menu(&quot;Test/Packets&quot;, menuable_tap, MENU_TOOLS_UNSORTED)</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-listener" rel="tag" title="see questions tagged &#39;listener&#39;">listener</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-debug" rel="tag" title="see questions tagged &#39;debug&#39;">debug</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '15, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/61d79b0a4b4832bea7944286ff4997fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="supisupi&#39;s gravatar image" /><p><span>supisupi</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="supisupi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Apr '15, 06:42</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-41322" class="comments-container"></div><div id="comment-tools-41322" class="comment-tools"></div><div class="clear"></div><div id="comment-41322-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

