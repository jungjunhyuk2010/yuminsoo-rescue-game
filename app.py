


import streamlit as st

# ==========================================
# 페이지 설정
# ==========================================

st.set_page_config(
    page_title="유민수 상병 구하기",
    page_icon="🎖️",
    layout="centered"
)

# ==========================================
# 디자인 CSS
# ==========================================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #101c2b, #263b50);
}

/* 기본 글씨 */
html, body, [class*="css"] {
    color: #111111;
}

/* 제목 */
h1, h2, h3 {
    color: #ffffff !important;
    font-weight: 900 !important;
}

/* 일반 설명 */
.stMarkdown p,
.stMarkdown li {
    color: #ffffff !important;
    font-size: 17px;
    line-height: 1.7;
}

/* 안내창 글씨 */
div[data-testid="stAlert"],
div[data-testid="stAlert"] p,
div[data-testid="stAlert"] span,
div[data-testid="stAlert"] div {
    color: #111111 !important;
    font-weight: bold !important;
}

/* 버튼 */
.stButton > button {
    width: 100%;
    min-height: 58px;
    border-radius: 13px;
    background: linear-gradient(135deg, #ffd166, #f0a928);
    color: #111111 !important;
    font-size: 17px !important;
    font-weight: 900 !important;
    border: 2px solid #d38b13;
    box-shadow: 0 5px 0 #93600d;
    transition: all 0.18s ease;
    margin: 5px 0 10px 0;
}

.stButton > button p,
.stButton > button span {
    color: #111111 !important;
    font-weight: 900 !important;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.01);
    background: #ffe08a;
    box-shadow: 0 8px 0 #93600d;
}

/* 입력창 */
.stTextInput input {
    background: #ffffff !important;
    color: #111111 !important;
    border: 2px solid #d6a84b !important;
    border-radius: 10px !important;
    font-weight: bold !important;
}

/* 작전 카드 */
.panel {
    background: #f3f6fa;
    color: #111111;
    padding: 20px;
    border-radius: 15px;
    border-left: 7px solid #f0ad32;
    margin: 15px 0;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    animation: appear 0.5s ease;
}

.panel h3, .panel p {
    color: #111111 !important;
}

/* 긴급 경고 */
.danger {
    background: #ffe2e2;
    color: #8b0000;
    border-left: 7px solid #d62828;
    padding: 18px;
    border-radius: 12px;
    font-weight: 900;
    animation: pulse 1.5s infinite;
}

/* 성공 */
.success-panel {
    background: #d9f8df;
    color: #075c21;
    padding: 20px;
    border-radius: 15px;
    border-left: 7px solid #159447;
}

/* 실패 */
.fail-panel {
    background: #ffe0e0;
    color: #8b0000;
    padding: 20px;
    border-radius: 15px;
    border-left: 7px solid #d62828;
}

/* 애니메이션 */
@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(18px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes pulse {
    0%, 100% {
        box-shadow: 0 0 0 rgba(255,0,0,0);
    }
    50% {
        box-shadow: 0 0 15px rgba(255,0,0,0.35);
    }
}

/* 모바일 */
@media (max-width: 600px) {
    h1 {
        font-size: 27px !important;
    }

    .stButton > button {
        font-size: 15px !important;
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# 게임 상태 관리
# ==========================================

def restart():
    st.session_state.page = "intro"
    st.session_state.role = None
    st.session_state.gender = None
    st.session_state.message = ""
    st.session_state.ending = None


if "page" not in st.session_state:
    restart()


def go(page):
    st.session_state.page = page


def ending(title, message, success=False):
    st.session_state.ending = {
        "title": title,
        "message": message,
        "success": success
    }
    go("ending")


def panel(title, message):
    st.markdown(
        f"""
        <div class="panel">
            <h3>{title}</h3>
            <p>{message}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# 인트로
# ==========================================

if st.session_state.page == "intro":

    st.markdown("""
    <div class="panel" style="text-align:center;">
        <h1 style="color:#111111 !important;">
            🎖️ 유민수 상병 구하기
        </h1>
        <h3>OPERATION: RESCUE MIN-SOO</h3>
        <p>긴급 인질 구출 작전</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="danger">
        🚨 긴급 상황 발생!<br>
        유민수 상병이 정체불명의 무장 세력에게 납치되었습니다.
    </div>
    """, unsafe_allow_html=True)

    panel(
        "작전 목표",
        "올바른 판단을 내려 유민수 상병을 구출하세요."
    )

    if st.button("⚔️ 작전 시작"):
        go("role")
        st.rerun()


# ==========================================
# 역할 선택
# ==========================================

elif st.session_state.page == "role":

    st.title("🎯 작전 담당자 선택")

    panel(
        "당신의 임무",
        "어떤 역할을 맡아 유민수 상병을 구출하시겠습니까?"
    )

    if st.button("🤝 협상가 - 대화와 협상으로 해결"):
        st.session_state.role = "협상가"
        go("gender")
        st.rerun()

    if st.button("⭐ 장성 - 군사 작전 지휘"):
        st.session_state.role = "장성"
        go("gender")
        st.rerun()

    if st.button("🚔 경찰 - 경찰 작전 지휘"):
        st.session_state.role = "경찰"
        go("gender")
        st.rerun()


# ==========================================
# 성별 선택
# ==========================================

elif st.session_state.page == "gender":

    st.title("👤 지휘관 정보")

    panel(
        "성별 선택",
        "작전에 참여할 지휘관의 성별을 선택하세요."
    )

    if st.button("남자"):
        st.session_state.gender = "남자"
        go("situation")
        st.rerun()

    if st.button("여자"):
        st.session_state.gender = "여자"
        go("situation")
        st.rerun()


# ==========================================
# 납치 상황
# ==========================================

elif st.session_state.page == "situation":

    st.title("🚨 긴급 상황 발생")

    st.markdown("""
    <div class="danger">
        유민수 상병이 납치되었습니다!<br>
        즉시 구출 작전을 시작해야 합니다.
    </div>
    """, unsafe_allow_html=True)

    panel(
        "작전 정보",
        f"담당 역할: {st.session_state.role}<br>"
        f"성별: {st.session_state.gender}"
    )

    if st.button("📡 상황 확인"):

        if st.session_state.role == "협상가":
            go("negotiator")

        elif st.session_state.role == "장성":
            go("general")

        else:
            go("police")

        st.rerun()


# ==========================================
# 협상가
# ==========================================

elif st.session_state.page == "negotiator":

    st.title("🤝 협상 작전실")

    st.markdown("""
    <div class="danger">
        납치범의 요구: 몸값 100만 달러!
    </div>
    """, unsafe_allow_html=True)

    panel(
        "협상 상황",
        "어떤 선택을 하시겠습니까?"
    )

    if st.button("1번. 💰 몸값 100만 달러 지불"):

        ending(
            "임무 성공",
            "몸값을 지불하고 유민수 상병을 구출했습니다. "
            "하지만 독단적인 몸값 지불로 보직해임되었습니다.",
            True
        )
        st.rerun()

    if st.button("2번. ❌ 몸값 지불 거부"):

        go("kidney")
        st.rerun()

    if st.button("3번. 📉 몸값 인하 요청"):

        go("discount")
        st.rerun()

    st.divider()

    st.subheader("📡 직접 협상하기")

    custom = st.text_input(
        "납치범에게 전달할 협상 내용",
        placeholder="협상 내용을 입력하세요."
    )

    if st.button("협상 내용 전달"):

        if custom.strip():
            st.session_state.message = custom
            go("custom_result")
            st.rerun()
        else:
            st.warning("협상 내용을 입력하세요.")


# ==========================================
# 몸값 인하
# ==========================================

elif st.session_state.page == "discount":

    st.title("📉 몸값 인하 협상")

    panel(
        "협상 진행 중",
        "납치범에게 몸값 인하를 요청합니다."
    )

    if st.button("10% 인하 요청"):

        ending(
            "임무 성공",
            "납치범이 협상을 받아들였습니다. "
            "유민수 상병을 구출했지만 보직해임되었습니다.",
            True
        )
        st.rerun()

    if st.button("20% 인하 요청"):

        ending(
            "임무 성공",
            "협상이 타결되어 유민수 상병을 구출했습니다. "
            "하지만 몸값 지불로 보직해임되었습니다.",
            True
        )
        st.rerun()

    if st.button("70% 인하 요청"):

        go("kidney")
        st.rerun()


# ==========================================
# 콩팥 손상 이후 선택
# ==========================================

elif st.session_state.page == "kidney":

    st.title("🚨 협상 결렬")

    st.markdown("""
    <div class="danger">
        ⚠️ 긴급 의료 상황!<br>
        유민수 상병이 콩팥 하나를 잃었습니다.
    </div>
    """, unsafe_allow_html=True)

    panel(
        "긴급 대응 명령",
        "다음 네 가지 선택 중 하나를 결정하세요."
    )

    if st.button("1번. 🏥 의료 지원 및 후송"):

        ending(
            "구출 성공",
            "의료 지원팀이 도착했습니다. "
            "유민수 상병을 병원으로 안전하게 후송했습니다.",
            True
        )
        st.rerun()

    if st.button("2번. 📡 재협상 시도"):

        ending(
            "작전 실패",
            "재협상이 결렬되었습니다. "
            "결국 유민수 상병이 사망했습니다."
        )
        st.rerun()

    if st.button("3번. ⚔️ 군경 합동 대응"):

        ending(
            "구출 성공",
            "군경 합동 작전으로 유민수 상병을 구출했습니다. "
            "하지만 심각한 부상과 후유증이 남았습니다.",
            True
        )
        st.rerun()

    if st.button("4번. ⏳ 아무것도 하지 않는다"):

        ending(
            "작전 실패",
            "아무런 조치도 취하지 않은 결과, "
            "유민수 상병이 사망했습니다."
        )
        st.rerun()


# ==========================================
# 직접 협상 결과
# ==========================================

elif st.session_state.page == "custom_result":

    st.title("📡 협상 결과")

    panel(
        "전달한 협상 내용",
        st.session_state.message
    )

    message = st.session_state.message

    if any(word in message for word in [
        "구출", "석방", "협력", "협상"
    ]):

        st.success("납치범이 대화에 응했습니다.")

        if st.button("협상 계속하기"):

            ending(
                "구출 성공",
                "협상이 타결되어 유민수 상병을 구출했습니다.",
                True
            )
            st.rerun()

    elif any(word in message for word in [
        "공격", "죽여", "체포", "진압"
    ]):

        st.error("납치범이 협상을 중단했습니다.")

        if st.button("상황 확인"):
            go("kidney")
            st.rerun()

    else:

        st.warning("납치범이 답변을 이해하지 못했습니다.")

        if st.button("다시 협상하기"):
            go("negotiator")
            st.rerun()


# ==========================================
# 장성
# ==========================================

elif st.session_state.page == "general":

    st.title("⭐ 군 작전 지휘실")

    st.markdown("""
    <div class="danger">
        군대 투입 여부를 결정해야 합니다!
    </div>
    """, unsafe_allow_html=True)

    panel(
        "작전 정보",
        "군대를 투입하면 구출 가능성이 높아지지만 "
        "심각한 부상 위험이 있습니다."
    )

    if st.button("⚔️ 군대 투입"):

        ending(
            "구출 성공",
            "군 작전이 성공하여 유민수 상병을 구출했습니다. "
            "하지만 심각한 신체 부상과 장기적인 후유증이 남았습니다.",
            True
        )
        st.rerun()


# ==========================================
# 경찰
# ==========================================

elif st.session_state.page == "police":

    st.title("🚔 경찰 작전 지휘실")

    panel(
        "긴급 경찰 대응",
        "경찰은 어떤 조치를 취하시겠습니까?"
    )

    if st.button("1번. 🚨 구출 작전 실행"):

        ending(
            "구출 성공",
            "경찰 작전이 성공했습니다. "
            "유민수 상병을 무사히 구출했습니다.",
            True
        )
        st.rerun()

    if st.button("2번. ❌ 사건 무시"):

        ending(
            "작전 실패",
            "사건이 방치되는 동안 유민수 상병이 사망했습니다."
        )
        st.rerun()

    if st.button("3번. 📋 수배 명단 등록"):

        go("warrant")
        st.rerun()


# ==========================================
# 경찰 수배 명단 등록 이후
# ==========================================

elif st.session_state.page == "warrant":

    st.title("📋 수배 명단 등록 완료")

    st.markdown("""
    <div class="danger">
        🚨 수배 명단에 납치범이 등록되었습니다!<br>
        이제 추가 지원 또는 체포 작전을 선택해야 합니다.
    </div>
    """, unsafe_allow_html=True)

    panel(
        "다음 작전 선택",
        "어떤 방식으로 납치범을 추적하시겠습니까?"
    )

    if st.button("1번. 🤝 도움 받기"):

        ending(
            "작전 실패",
            "도움을 주겠다고 접근한 인물에게 배신당했습니다. "
            "결국 유민수 상병이 사망했습니다."
        )
        st.rerun()

    if st.button("2번. 🚔 체포 작전 시작"):

        go("capture")
        st.rerun()


# ==========================================
# 체포 작전 - D / L 선택
# ==========================================

elif st.session_state.page == "capture":

    st.title("🚔 체포 작전 시작")

    st.markdown("""
    <div class="danger">
        ⚠️ 최종 선택 단계!<br>
        체포 작전 중 마지막 판단을 내려야 합니다.
    </div>
    """, unsafe_allow_html=True)

    panel(
        "최종 작전 코드",
        "D 또는 L 중 하나를 선택하세요. "
        "선택에 따라 유민수 상병의 운명이 결정됩니다."
    )

    if st.button("D 선택"):

        ending(
            "🎉 구출 성공!",
            "D 작전이 성공적으로 마무리되었습니다. "
            "납치범이 체포되었고 유민수 상병을 구출했습니다.",
            True
        )
        st.rerun()

    if st.button("L 선택"):

        ending(
            "작전 실패",
            "L 작전을 선택한 결과 작전이 실패했습니다. "
            "유민수 상병이 사망했습니다."
        )
        st.rerun()


# ==========================================
# 엔딩
# ==========================================

elif st.session_state.page == "ending":

    result = st.session_state.ending

    st.title("🏁 작전 결과")

    if result["success"]:

        st.markdown(
            f"""
            <div class="success-panel">
                <h2 style="color:#075c21 !important;">
                    {result['title']}
                </h2>
                <p style="color:#075c21 !important;">
                    {result['message']}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.balloons()

    else:

        st.markdown(
            f"""
            <div class="fail-panel">
                <h2 style="color:#8b0000 !important;">
                    ❌ 실패입니다. 다시 시도하세요.
                </h2>
                <p style="color:#8b0000 !important;">
                    {result['message']}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    if st.button("🔄 처음부터 다시 시작"):

        restart()
        st.rerun()


# ==========================================
# 하단
# ==========================================

st.divider()

st.markdown("""
<p style="text-align:center; color:#dce5ef !important;">
🎖️ 유민수 상병 구하기<br>
OPERATION: RESCUE MIN-SOO
</p>
""", unsafe_allow_html=True)
