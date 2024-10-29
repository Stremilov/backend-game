from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    player_id: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    first_login: Mapped[datetime | None] = mapped_column(DateTime, default=None)
    points: Mapped[int] = mapped_column(Integer, default=0)

    boosts: Mapped[list["Boost"]] = relationship("Boost", back_populates="player")

    def add_points(self, points: int) -> None:
        self.points += points

    def set_first_login(self) -> None:
        if self.first_login is None:
            self.first_login = datetime.now()


class Boost(Base):
    __tablename__ = "boosts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[str] = mapped_column(String(100), nullable=False)
    player_id: Mapped[int] = mapped_column(ForeignKey("players.id"))

    player: Mapped[Player] = relationship("Player", back_populates="boosts")

    def __repr__(self) -> str:
        return f"<Boost(type='{self.type}', player_id='{self.player.player_id}')>"
