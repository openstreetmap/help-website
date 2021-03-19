+++
type = "question"
title = "LUA how to get multiple values from faststart items H225, H245"
description = '''I want to get all media address and port form H323 call from faststart. Faststart filed only returns number of items in the message. If I do Field.new(&quot;h245.network&quot;) or Field.new(&quot;h245.tsapIdentifier&quot;) I got null result. How can I get to all of the items and display? This is my code.  -- text_windo...'''
date = "2011-05-25T01:40:00Z"
lastmod = "2011-05-26T01:31:00Z"
weight = 4225
keywords = [ "lua", "h225", "h323", "h245" ]
aliases = [ "/questions/4225" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [LUA how to get multiple values from faststart items H225, H245](/questions/4225/lua-how-to-get-multiple-values-from-faststart-items-h225-h245)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4225-score" class="post-score" title="current number of votes">0</div><span id="post-4225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to get all media address and port form H323 call from faststart. Faststart filed only returns number of items in the message. If I do Field.new("h245.network") or Field.new("h245.tsapIdentifier") I got null result. How can I get to all of the items and display?</p><p>This is my code.</p><pre><code>-- text_window_tap.lua
-- an example of a tap that registers a menu
-- and prints to a text window

instances = 0 -- number of instances of the tap created so far

ip_addr_extractor = Field.new(&quot;ip.addr&quot;)
tcp_port_extractor = Field.new(&quot;tcp.port&quot;)
h225_faststart_extractor = Field.new(&quot;h225.fastStart&quot;)
h225_guid_extractor = Field.new(&quot;h225.guid&quot;)
h245_tsapidentifier_extractor = Field.new(&quot;h245.tsapIdentifier&quot;)
h245_network_extractor = Field.new(&quot;h245.network&quot;)

function sip_tap_menu()
    instances = instances + 1

local td = {}

td.win = TextWindow.new(&quot;h225 SIGNALING PARSE &quot; .. instances) -- the window we&#39;ll use
    td.text = &quot;&quot;
    td.instance = instances -- the instance number of this tap

-- h225 SDP Processing
    local h225 = Listener.new(&quot;h225&quot;, &quot;h225&quot;)
    -- retap_packets()
    reload()

function h225.reset()
    end

function h225.packet(pinfo,tvb,userdata)
       local ip_src, ip_dst = ip_addr_extractor()
       local tcp_src, tcp_dst = tcp_port_extractor()
       local h225_faststart = h225_faststart_extractor()
       local h225_guid = h225_guid_extractor()
       local h245_tsapidentifier = h245_tsapidentifier_extractor()
       local h245_network = h245_network_extractor()

if h225_faststart then
           td.win:append( &quot;faststart=&quot; ..  tostring(h225_faststart) ..  
           &quot;:IP_SRC=&quot; ..  tostring(ip_src) .. 
           &quot;:UDP_SRC=&quot; .. tostring(tcp_src) .. 
           &quot;:IP_DST=&quot; .. tostring(ip_dst) .. 
           &quot;:UDP_DST=&quot; .. tostring(tcp_dst) .. 
           &quot;:h225_guid=&quot; .. tostring(h225_guid) .. 
           &quot;:h245_tsapidentifier=&quot; .. 
           tostring(h245_tsapidentifier)  .. 
           &quot;:h245_network=&quot; .. tostring(h245_network) .. &quot;\n&quot;)
       end

end

function remove_tap()
        if h225 and h225.remove then
            h225:remove()
        end
    end

td.win:set_atclose(remove_tap)

end
register_menu(&quot;h225 Signaling Parse&quot;,sip_tap_menu,MENU_TOOLS_UNSORTED)
</code></pre><p>Sample capture of packet</p><pre><code>H.225.0 CS
    H323-UserInformation
        h323-uu-pdu
            h323-message-body: alerting (3)
                alerting
                    protocolIdentifier: 0.0.8.2250.0.4 (Version 4)
                    destinationInfo
                        vendor
                            vendor
                                t35CountryCode: United States (181)
                                t35Extension: 0
                                manufacturerCode: 23
                            H.221 Manufacturer: VocalTec Communications, Inc. (0xb5000017)
                            versionId: 1.00
                        gateway
                        terminal
                        .... .0.. mc: False
                        .... ..0. undefinedNode: False
                    callIdentifier
                        guid: e0f238a4-d056-11df-b14e-0015173704f0
                    fastStart: 2 items
                        Item 0
                            FastStart item: 22 octets
                            OpenLogicalChannel
                                forwardLogicalChannelNumber: 129
                                forwardLogicalChannelParameters
                                    dataType: nullData (1)
                                        nullData: NULL
                                    multiplexParameters: none (4)
                                        none: NULL
                                reverseLogicalChannelParameters
                                    dataType: audioData (3)
                                        audioData: g729 (10)
                                            g729: 2
                                    multiplexParameters: h2250LogicalChannelParameters (2)
                                        h2250LogicalChannelParameters
                                            sessionID: 1
                                            mediaControlChannel: unicastAddress (0)
                                                unicastAddress: iPAddress (0)
                                                    iPAddress
                                                        network: 81.15.5.10 (81.15.5.10)
                                                        tsapIdentifier: 10027
                        Item 1
                            FastStart item: 25 octets
                            OpenLogicalChannel
                                forwardLogicalChannelNumber: 4
                                forwardLogicalChannelParameters
                                    dataType: audioData (3)
                                        audioData: g729 (10)
                                            g729: 2
                                    multiplexParameters: h2250LogicalChannelParameters (3)
                                        h2250LogicalChannelParameters
                                            sessionID: 1
                                            mediaChannel: unicastAddress (0)
                                                unicastAddress: iPAddress (0)
                                                    iPAddress
                                                        network: 81.15.5.10 (81.15.5.10)
                                                        tsapIdentifier: 10026
                                            mediaControlChannel: unicastAddress (0)
                                                unicastAddress: iPAddress (0)
                                                    iPAddress
                                                        network: 81.15.5.10 (81.15.5.10)
                                                        tsapIdentifier: 10027
                    0... .... multipleCalls: False
                    1... .... maintainConnection: True
                    presentationIndicator: presentationAllowed (0)
                        presentationAllowed: NULL
                    screeningIndicator: userProvidedVerifiedAndFailed (2)
            0... .... h245Tunnelling: False</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-h225" rel="tag" title="see questions tagged &#39;h225&#39;">h225</span> <span class="post-tag tag-link-h323" rel="tag" title="see questions tagged &#39;h323&#39;">h323</span> <span class="post-tag tag-link-h245" rel="tag" title="see questions tagged &#39;h245&#39;">h245</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 May '11, 01:40</strong></p><img src="https://secure.gravatar.com/avatar/2bb36804afb054782c66c3ad2d8690f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jakan&#39;s gravatar image" /><p><span>jakan</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jakan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 May '11, 01:50</strong> </span></p></div></div><div id="comments-container-4225" class="comments-container"></div><div id="comment-tools-4225" class="comment-tools"></div><div class="clear"></div><div id="comment-4225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4236"></span>

<div id="answer-container-4236" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4236-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4236-score" class="post-score" title="current number of votes">1</div><span id="post-4236-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That question seems to be showing up quite often</p><p>Quick lua search on this site</p><p><a href="http://ask.wireshark.org/questions/1579/fetching-multiple-named-values-with-lua">fetching-multiple-named-values-with-lua</a></p><p><a href="http://ask.wireshark.org/questions/1023/fix-protocol-dissector">And another example for different protocol</a></p><p>in your case something like below might work</p><pre><code>my_h245_table = { h245_network_extractor() }
tostring(my_h245_table[0])..tostring(my_h245_table[1])</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '11, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p><span>izopizo</span><br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-4236" class="comments-container"><span id="4241"></span><div id="comment-4241" class="comment"><div id="post-4241-score" class="comment-score"></div><div class="comment-text"><p>It is not working. Now I tried with FastStart item: &lt;h225.faststart_item&gt; and it works. I got value 22 and 25 for both items. If I want to extract any other one there is nothing in the list. It looks like it is only working on first level items because I also tried with forwardLogicalChannelNumber: &lt;h245.forwardlogicalchannelnumber&gt; to and it is not working.</p></div><div id="comment-4241-info" class="comment-info"><span class="comment-age">(26 May '11, 01:31)</span> <span class="comment-user userinfo">jakan</span></div></div></div><div id="comment-tools-4236" class="comment-tools"></div><div class="clear"></div><div id="comment-4236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

