+++
type = "question"
title = "Getting the request URL for a reassembled PDU"
description = '''I am writing a lua script to process json responses. What I have so far follows below. My script runs for each json response returned from the server; it&#x27;s based off one of the examples. The problem I have is that some of the responses are identical to each other, but the interpretation of the data ...'''
date = "2011-12-06T02:17:00Z"
lastmod = "2011-12-06T02:17:00Z"
weight = 7794
keywords = [ "lua", "pdu" ]
aliases = [ "/questions/7794" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting the request URL for a reassembled PDU](/questions/7794/getting-the-request-url-for-a-reassembled-pdu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7794-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7794-score" class="post-score" title="current number of votes">1</div><span id="post-7794-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a lua script to process json responses. What I have so far follows below. My script runs for each json response returned from the server; it's based off one of the examples.</p><p>The problem I have is that some of the responses are identical to each other, but the interpretation of the data is context dependent. The context is the API URL that was used to make the request.</p><p>I haven't been able to figure out how to get the http request URL from the stream from which the reassembled PDU is gathered. Is that possible?</p><p>Here's an example stream:</p><pre><code>0.255611 192.168.1.156 -&gt; 192.168.1.4 HTTP 226 POST /api/stats.json HTTP/1.1  (application/x-www-form-urlencoded)
0.359587 192.168.1.4 -&gt; 192.168.1.156 TCP 60 http &gt; 5195 [ACK] Seq=1 Ack=787 Win=7982 Len=0
0.664189 192.168.1.4 -&gt; 192.168.1.156 TCP 1406 [TCP segment of a reassembled PDU]
...
1.107964 192.168.1.4 -&gt; 192.168.1.156 HTTP 1187 HTTP/1.1 200 OK  (application/json)</code></pre><p>At the time my script is called on the 200 OK packet, on the reassmebled PDU, the http fields for request uri are all empty. I need to discover that this json object is a result of /api/stats.json.</p><pre><code>do
    packets = 0;

local response_fe = Field.new(&quot;http.response&quot;)
    local request_version_fe = Field.new(&quot;http.request.version&quot;)
    local response_code_fe = Field.new(&quot;http.response.code&quot;)
    local response_phrase_fe = Field.new(&quot;http.response.phrase&quot;)

local function init_listener()
        local tap = Listener.new(&quot;http&quot;, &quot;http.content_type contains \&quot;json\&quot;&quot;)

local count = 0

function tap.reset()
            packets = 0;
        end

function tap.packet(pinfo, tvb, ip)
            local response = response_fe()
            local request_version = request_version_fe()
            local response_code = response_code_fe()
            local response_phrase = response_phrase_fe()

-- Get a table of fields
            fields = { all_field_infos() }

-- Print the name of every field
            for i, field in ipairs(fields) do
                count = count + 1
                print(count .. &quot; name: &quot; .. tostring(field.name) .. 
                               &quot; len: &quot; .. tostring(field.len) .. 
                               &quot; offset: &quot; .. tostring(field.offset) .. 
                               &quot; value: &quot; .. tostring(field.value):sub(1, 40))
            end

packets = packets + 1
        end

function tap.draw()
            print(&quot;Packets: &quot;, packets)
        end
    end
    init_listener()
end</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-pdu" rel="tag" title="see questions tagged &#39;pdu&#39;">pdu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '11, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/88d413834375dbc71f5d3146aca1cd3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="studog&#39;s gravatar image" /><p><span>studog</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="studog has no accepted answers">0%</span></p></div></div><div id="comments-container-7794" class="comments-container"></div><div id="comment-tools-7794" class="comment-tools"></div><div class="clear"></div><div id="comment-7794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

