+++
type = "question"
title = "LUA &#92; Listener - Get ALL IEEE C37.118 within TCP&#92;UDP"
description = '''Hello, i am writing my first LUA script in order to display information about each Synchrophasor (IEEE C37.118) packet. I wrote this but the problem is that, not all the synchrophasor packet are seen. I think that only the first synchrophaseur packet is &quot;seen&quot;.  How write the function &quot;function tap....'''
date = "2016-03-15T13:26:00Z"
lastmod = "2016-03-15T13:26:00Z"
weight = 50956
keywords = [ "abc" ]
aliases = [ "/questions/50956" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [LUA \\ Listener - Get ALL IEEE C37.118 within TCP\\UDP](/questions/50956/lua-listener-get-all-ieee-c37118-within-tcpudp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50956-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>i am writing my first LUA script in order to display information about <strong>each</strong> Synchrophasor (IEEE C37.118) packet. I wrote this but the problem is that, not all the synchrophasor packet are seen. I think that only the first synchrophaseur packet is "seen".</p><p>How write the function "function tap.packet(pinfo,tvb)" in order to pass through all synchrophasor packet ?</p><p>Thanks</p><pre><code>local g_fracSec = Field.new(&quot;synphasor.fracsec&quot;)
local g_soc = Field.new(&quot;synphasor.soc&quot;)
local function menuable_tap()
    -- Declare the window we will use
    local tw = TextWindow.new(&quot;IEEE C37.118 Performances&quot;)
    -- this is our tap
    local tap = Listener.new(nill, &quot;synphasor&quot;);
    function remove()
            -- this way we remove the listener that otherwise will remain running indefinitely
            tap:remove();
    end
    -- we tell the window to call the remove() function when closed
    tw:set_atclose(remove)
    -- this function will be called once for each packet
    function tap.packet(pinfo,tvb)
            local soc = g_soc()
            local fracSec = g_fracSec()
            tw:append(tostring(soc) .. &quot;\n&quot;);
            tw:append(tostring(fracSec) .. &quot;\n&quot;);
    end
    -- this function will be called once every few seconds to update our window
    function tap.draw(t)
    end
    -- this function will be called whenever a reset is needed
    -- e.g. when reloading the capture file
    function tap.reset()
            tw:clear()
    end
end</code></pre><p><img src="https://osqa-ask.wireshark.org/upfiles/a.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">abc</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '16, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/52c3825749489f8e41ff11f522d9bdbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SebastienRolle&#39;s gravatar image" /><p>SebastienRolle<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SebastienRolle has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 15 Mar '16, 14:04</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-50956" class="comments-container"><span id="50962"></span><div id="comment-50962" class="comment"><div id="post-50962-score" class="comment-score"></div><div class="comment-text"><p>I've never written a Lua tap, but from the description it seems to me that the function <code>tap.packet</code> is called once per captured <em>frame</em> (there used to be some confusion between "packet" and "frame" so the documentation may mean a frame when talking about a packet). Αs a captured frame may contain more than one C37.118 <em>PDU</em>, you'd have to process these PDUs one by one, which may eventually mean full redissection.</p></div><div id="comment-50962-info" class="comment-info"><span class="comment-age">(15 Mar '16, 14:28)</span> sindy</div></div><span id="50964"></span><div id="comment-50964" class="comment"><div id="post-50964-score" class="comment-score"></div><div class="comment-text"><p>Or, to be more precise after reading <a href="https://wiki.wireshark.org/LuaAPI/Listener">the relevant wiki page</a>:</p><ul><li><p>the first argument to listener.new() must be one of supported tap types (actually, PDU types). Empty parameter or <code>nil</code> (not <code>nill</code>) means that the tap handling function will be called once per captured frame.</p></li><li><p>the second parameter is a filter (in display filter format), yet it is unclear whether the filter would take into account a single PDU or the whole frame.</p></li></ul><p>I am afraid that <code>synphasor</code> (IEEE C37.118) is not a supported tap type, so to obtain the individual values (or counts), your tap function will have to take the tvb and parse it. But before taking that adventure, try to change</p><pre><code>local tap = Listener.new(nill, &quot;synphasor&quot;);</code></pre><p>to</p><pre><code>local tap = Listener.new(&quot;synphasor&quot;);</code></pre><p>You may be lucky in terms that the documentation would be out of date and all known PDU types could be used as taps.</p></div><div id="comment-50964-info" class="comment-info"><span class="comment-age">(15 Mar '16, 14:52)</span> sindy</div></div><span id="50965"></span><div id="comment-50965" class="comment"><div id="post-50965-score" class="comment-score"></div><div class="comment-text"><p>Hm, you are <em>not</em> lucky.</p><pre><code>local mytable = Listener.list()
for i, v in ipairs(mytable) do print(i, v) end</code></pre><p>shows that synphasor is not an eligible tap type in 2.0.2.</p></div><div id="comment-50965-info" class="comment-info"><span class="comment-age">(15 Mar '16, 15:32)</span> sindy</div></div><span id="50966"></span><div id="comment-50966" class="comment"><div id="post-50966-score" class="comment-score"></div><div class="comment-text"><p>I am not lucky,local tap = Listener.new("synphasor"); not work (as you mentioned). So i need to parse the tvb.... :(</p><p>Thanks for all the need yoy gave me. Sébastien</p></div><div id="comment-50966-info" class="comment-info"><span class="comment-age">(15 Mar '16, 16:15)</span> SebastienRolle</div></div></div><div id="comment-tools-50956" class="comment-tools"></div><div class="clear"></div><div id="comment-50956-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

